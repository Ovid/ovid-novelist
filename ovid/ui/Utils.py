from ovid.ui.OvidListWidgetChapter import OvidListWidgetChapter


def setNovel(ovid, novel):
    # Clear the current items in the sidebar
    ovid.novel = novel
    ovid.chapterList.clear()

    # Add each chapter of the loaded novel to the sidebar
    for chapter in novel.chapters:
        chapter_item = OvidListWidgetChapter(chapter)
        ovid.chapterList.addItem(chapter_item)

    # Select the first chapter and display its contents in the main window
    if ovid.novel.chapters:
        first_chapter = novel.chapters[0]
        ovid.chapterList.setCurrentItem(ovid.chapterList.item(0))
        ovid.textEditor.setText(first_chapter.contents)
