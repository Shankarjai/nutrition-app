<div class="sidebar-container">
    
    <div class="sidebar-menus">

        <div class="sidebar-menu <?php echo($current_page == 'vitamins' ? 'sidebar-menu-active' : '') ?>">
            <a class="sidebar-link" href="vitamins.php" tab="vitamins">Vitamins</a>
        </div>
        <div class="sidebar-menu <?php echo($current_page == 'food' ? 'sidebar-menu-active' : '') ?>">
            <a class="sidebar-link" href="food.php" tab="food">Food</a>
        </div>

    </div>

</div>

<script>
    $('.sidebar-menu-active')[0].style.background = 'red'; 
</script>