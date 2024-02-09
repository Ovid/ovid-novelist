from ovid.ui.OvidListWidgetChapter import OvidListWidgetChapter


def setNovel(ovid, novel):

    # Must set the central widget. Otherwise, very bad things happen (the
    # program crashes when it tries to update something that's not there)
    ovid.setCentralWidget(ovid.textEditor)

    # Clear the current items in the sidebar
    ovid.novel = novel
    ovid.chapterList.clear()

    # Add each chapter of the loaded novel to the sidebar
    for chapter in novel.chapters:
        chapter_item = OvidListWidgetChapter(chapter)
        ovid.chapterList.addItem(chapter_item)

    # Select the first chapter and display its contents in the main window
    if ovid.novel.chapters:
        # check if novel has a currentChapter attribute
        has_current_chapter = hasattr(novel, "currentChapter")
        current_chapter = (
            novel.chapters[0]
            if (not has_current_chapter or not novel.currentChapter)
            else novel.currentChapter
        )

        # Set the current chapter in the sidebar
        for i in range(ovid.chapterList.count()):
            chapter_item = ovid.chapterList.item(i)
            if chapter_item.chapter == current_chapter:
                ovid.chapterList.setCurrentItem(chapter_item)
                break
        ovid.textEditor.setText(current_chapter.contents)
