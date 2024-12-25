<div class="sidebar-container">
    
    <div class="sidebar-menus">

        <div class="sidebar-menu <?php echo($current_page == 'nutrients' ? 'sidebar-menu-active' : '') ?>">
            <a class="sidebar-link" href="nutrients.php" tab="nutrients">Nutrients</a>
        </div>
        <div class="sidebar-menu <?php echo($current_page == 'food' ? 'sidebar-menu-active' : '') ?>">
            <a class="sidebar-link" href="food.php" tab="food">Food</a>
        </div>

    </div>

</div>

<script>
    $('.sidebar-menu-active')[0].style.background = 'red'; 
</script>