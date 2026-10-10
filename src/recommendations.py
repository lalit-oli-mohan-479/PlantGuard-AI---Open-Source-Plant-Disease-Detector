"""
PlantGuard AI - Care Recommendations & Disease Knowledge Base
Provides transparent, cautious, and practical gardening care steps
mapped across all supported plant disease and healthy classes.
"""

from typing import Dict, Any, List

# Structured recommendations database for all 38 PlantVillage classes
DISEASE_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    # --- APPLE ---
    "Apple Scab": {
        "crop": "Apple",
        "category": "Fungal Disease",
        "symptoms": "Olive-green to velvety dark brown spots on leaves, puckered foliage, and scabby lesions on fruit.",
        "immediate_actions": [
            "Rake and remove fallen infected leaves from around the tree base to reduce overwintering fungal spores.",
            "Prune overcrowded branches during dry weather to increase sunlight and air circulation within the canopy.",
            "Avoid overhead irrigation; water strictly at the root zone.",
        ],
        "preventative_care": [
            "Apply organic neem oil or sulfur-based spray early in spring before bud break if scab recurs annually.",
            "Maintain a 2-3 inch layer of fresh organic mulch, keeping it 4 inches away from the trunk.",
            "Choose scab-resistant apple cultivars (e.g., Liberty, Freedom, Enterprise) for future plantings.",
        ],
        "outdoor_tasks": [
            "Inspect underside of leaves on lower branches for fuzzy olive spots.",
            "Gather and dispose of fallen leaf litter in trash (do not compost scab-infected leaves).",
            "Check soil moisture around the drip line with your finger.",
        ],
    },
    "Apple with Black Rot": {
        "crop": "Apple",
        "category": "Fungal Disease",
        "symptoms": "Purple flecks on leaves expanding into 'frog-eye' leaf spots with light centers, fruit rot, and bark cankers.",
        "immediate_actions": [
            "Prune out dead wood, cankered limbs, and mummified fruit hanging on the tree or lying below.",
            "Disinfect pruning shears between cuts using 70% isopropyl alcohol.",
            "Ensure the tree gets adequate airflow by thinning dense canopy sections.",
        ],
        "preventative_care": [
            "Avoid mechanical injuries to the bark with lawnmowers or string trimmers.",
            "Apply compost tea to support beneficial phyllosphere microbes.",
            "Consult local agricultural extension for optimal timing of organic copper or sulfur controls.",
        ],
        "outdoor_tasks": [
            "Search the tree for shriveled, blackened fruit mummies and remove them.",
            "Inspect main limbs and trunk for sunken, discolored bark cankers.",
            "Sterilize your pruning tool blades with alcohol wipes.",
        ],
    },
    "Cedar Apple Rust": {
        "crop": "Apple",
        "category": "Fungal Disease",
        "symptoms": "Bright yellow-orange or reddish spots on upper leaf surfaces; tube-like structures may develop underneath leaves.",
        "immediate_actions": [
            "Pick off heavily spotted individual leaves on young trees if infection is light.",
            "Check for nearby Eastern red cedar or juniper trees, which act as the alternate host for the fungus.",
            "Rinse pruning tools with sanitizing solution after trimming.",
        ],
        "preventative_care": [
            "Where possible, remove wild cedar/juniper galls within 500 feet of your apple trees.",
            "Plant resistant apple varieties (such as Honeycrisp, Gala, or Enterprise).",
            "Apply protective organic copper soap at bud break if alternate hosts cannot be removed.",
        ],
        "outdoor_tasks": [
            "Walk the perimeter of your yard to identify nearby junipers or cedar trees.",
            "Inspect upper surfaces of apple leaves for vibrant yellow-orange rings.",
            "Record how many branches show symptoms to monitor progression over the next 7 days.",
        ],
    },
    "Healthy Apple": {
        "crop": "Apple",
        "category": "Healthy",
        "symptoms": "Leaves are vibrant green, smooth, pliable, and show no signs of spotting, wilting, or lesions.",
        "immediate_actions": [
            "Maintain current balanced care schedule.",
            "Ensure steady deep watering during fruit development, providing 1-2 inches of water per week.",
        ],
        "preventative_care": [
            "Keep the root zone clear of tall grass and weeds.",
            "Replenish organic mulch around the drip line.",
            "Monitor weekly for early signs of pests or nutritional deficiencies.",
        ],
        "outdoor_tasks": [
            "Check soil moisture 3 inches deep beneath the canopy mulch.",
            "Inspect new growth shoots for aphid clusters or leaf-curling.",
            "Enjoy 10 minutes of sunshine and fresh air alongside your thriving tree!",
        ],
    },

    # --- BLUEBERRY ---
    "Healthy Blueberry Plant": {
        "crop": "Blueberry",
        "category": "Healthy",
        "symptoms": "Leaves are rich green and glossy, free from chlorosis (yellowing) or spots.",
        "immediate_actions": [
            "Continue standard watering and care.",
            "Keep soil consistently moist (blueberries have shallow fibrous roots).",
        ],
        "preventative_care": [
            "Ensure soil pH remains acidic (ideally 4.5 - 5.5) using elemental sulfur or pine needle mulch.",
            "Use rainwater or filtered water if tap water has high alkalinity.",
            "Prune older canes (over 4-5 years) in late winter to stimulate vigorous new growth.",
        ],
        "outdoor_tasks": [
            "Touch the soil surface under the mulch to verify it feels like a damp sponge.",
            "Check soil pH with a test kit if leaf veins ever begin to yellow.",
            "Top-dress with pine needle or cedar mulch around the shallow root zone.",
        ],
    },

    # --- CHERRY ---
    "Cherry with Powdery Mildew": {
        "crop": "Cherry",
        "category": "Fungal Disease",
        "symptoms": "White or powdery grey patches on young leaves, curling leaf margins, and stunted shoot tips.",
        "immediate_actions": [
            "Gently prune off heavily mildewed shoot tips to reduce fungal colonies.",
            "Switch watering method to drip or soaker hoses; do not spray leaves from overhead.",
            "Thin inner branches to allow maximum sunlight into the center of the tree.",
        ],
        "preventative_care": [
            "Apply potassium bicarbonate or horticultural oil early in the morning when temperatures are below 85°F (29°C).",
            "Avoid high-nitrogen fertilizers which cause excessive flush of tender susceptible foliage.",
            "Ensure proper tree spacing when planting new stone fruit varieties.",
        ],
        "outdoor_tasks": [
            "Inspect tender young branch tips for white powdery dust.",
            "Feel the foliage texture and check if leaves are curling upward.",
            "Verify that automatic sprinklers are not splashing tree leaves.",
        ],
    },
    "Healthy Cherry Plant": {
        "crop": "Cherry",
        "category": "Healthy",
        "symptoms": "Foliage is dark green, evenly shaped, and free from holes, blisters, or mildew.",
        "immediate_actions": [
            "Maintain routine watering schedule, adjusting for seasonal rainfall.",
            "Protect developing cherries from bird feeding using protective mesh netting if in season.",
        ],
        "preventative_care": [
            "Apply dormant organic spray during winter to prevent scale and fungal overwintering.",
            "Mulch around the base to preserve moisture and suppress weeds.",
        ],
        "outdoor_tasks": [
            "Feel the trunk base to ensure root flare is exposed and not buried in mulch.",
            "Inspect leaf undersides for any spider mite webbing.",
            "Breathe in the garden air and note overall blossom or canopy vigor.",
        ],
    },

    # --- CORN (MAIZE) ---
    "Corn (Maize) with Cercospora and Gray Leaf Spot": {
        "crop": "Corn (Maize)",
        "category": "Fungal Disease",
        "symptoms": "Narrow, rectangular tan or grey lesions running parallel to leaf veins, causing premature blighting.",
        "immediate_actions": [
            "Remove and discard severely affected lower leaves to decrease spore splash.",
            "Increase plant spacing in future rows to enhance canopy ventilation.",
            "Ensure soil has balanced potassium and avoid excessive nitrogen fertilizer.",
        ],
        "preventative_care": [
            "Practice minimum 2-year crop rotation with non-host crops (e.g., legumes).",
            "Incorporate crop residue deep into soil after harvest to decompose fungal mycelium.",
            "Select hybrid varieties resistant to Gray Leaf Spot (GLS).",
        ],
        "outdoor_tasks": [
            "Walk down corn rows and examine lower leaf tiers for rectangular tan streaks.",
            "Check soil moisture and root stability around stalk bases.",
            "Measure row distance to ensure adequate air channels between stalks.",
        ],
    },
    "Corn (Maize) with Common Rust": {
        "crop": "Corn (Maize)",
        "category": "Fungal Disease",
        "symptoms": "Small, powdery cinnamon-brown to reddish pustules on both upper and lower leaf surfaces.",
        "immediate_actions": [
            "Pustules rupture releasing spores; avoid brushing against plants when leaves are wet.",
            "Water only at ground level early in the day so dew evaporates promptly.",
        ],
        "preventative_care": [
            "Plant rust-resistant sweet corn varieties.",
            "Plant early in the season to allow ears to mature before peak rust spore migrations.",
            "Keep plot weed-free to improve cross-ventilation.",
        ],
        "outdoor_tasks": [
            "Rub a white tissue over suspect spots: rust leaves a rusty-orange powder mark.",
            "Check if rust pustules are restricted to lower or upper leaves.",
            "Check weather forecast for upcoming humid or rainy periods.",
        ],
    },
    "Corn (Maize) with Northern Leaf Blight": {
        "crop": "Corn (Maize)",
        "category": "Fungal Disease",
        "symptoms": "Large, cigar-shaped, grey-green to tan lesions (1-6 inches long) spreading across leaf blades.",
        "immediate_actions": [
            "Avoid overhead irrigation which spreads spores across leaves.",
            "Isolate infected residue after harvest and burn or discard in municipal waste.",
        ],
        "preventative_care": [
            "Rotate crops annually with non-grass crops.",
            "Choose resistant hybrids with known Ht gene resistance.",
            "Improve soil microbial diversity with finished organic compost.",
        ],
        "outdoor_tasks": [
            "Measure length of suspicious leaf lesions with a ruler or fingers.",
            "Check if lesions have started on lower leaves and are progressing upward.",
            "Inspect soil drainage after recent watering.",
        ],
    },
    "Healthy Corn (Maize) Plant": {
        "crop": "Corn (Maize)",
        "category": "Healthy",
        "symptoms": "Sturdy green stalks with broad, upright emerald leaves with no rust or blighting.",
        "immediate_actions": [
            "Maintain deep watering, particularly during tasseling and silking stages.",
            "Side-dress with balanced organic nitrogen or compost tea during active vegetative growth.",
        ],
        "preventative_care": [
            "Keep soil weeded to prevent competition for nutrients and moisture.",
            "Hill soil around bases if plants need extra brace root stability.",
        ],
        "outdoor_tasks": [
            "Check tassel and ear silk development.",
            "Inspect stalk firmness near the ground level.",
            "Enjoy the rustling sound of healthy corn leaves in the breeze!",
        ],
    },

    # --- GRAPE ---
    "Grape with Black Rot": {
        "crop": "Grape",
        "category": "Fungal Disease",
        "symptoms": "Small reddish-brown circular spots on leaves; berries shrivel into hard, black, wrinkled mummies.",
        "immediate_actions": [
            "Immediately pick and dispose of any mummified fruit clusters still on vines or on the ground.",
            "Prune away blighted canes and leaves during dry afternoon hours.",
            "Trellis vines to ensure maximum air penetration through foliage.",
        ],
        "preventative_care": [
            "Apply organic copper or sulfur fungicides prior to bloom and through berry touch if disease is endemic.",
            "Maintain rigorous weed management under the vine rows to reduce ground humidity.",
            "Prune dormant canes cleanly in winter.",
        ],
        "outdoor_tasks": [
            "Examine vine clusters closely for shriveled dark raisins.",
            "Clean ground directly under vines of any dried debris.",
            "Check vine tie tightness to prevent stem chafing.",
        ],
    },
    "Grape with Esca (Black Measles)": {
        "crop": "Grape",
        "category": "Fungal Disease",
        "symptoms": "'Tiger-stripe' leaf discoloration (yellow/brown areas between veins) and dark speckling on fruit skin.",
        "immediate_actions": [
            "Mark symptomatic vines with a garden tag to track and avoid pruning during wet conditions.",
            "Disinfect pruning tools between each grapevine with a bleach or alcohol solution.",
            "Cut away diseased wood several inches below visible cankers if possible.",
        ],
        "preventative_care": [
            "Seal large pruning wounds with pruning wound sealant to prevent fungal entry.",
            "Avoid excessive vine stress from prolonged drought or heavy overcropping.",
            "Renew older trunks by training a healthy sucker from the base if trunk is damaged.",
        ],
        "outdoor_tasks": [
            "Inspect the cross-section of old pruning wounds for dark vascular staining.",
            "Check if grape berries display small, dark-purple measles spots.",
            "Tie a bright marker ribbon on symptomatic canes for winter pruning attention.",
        ],
    },
    "Grape with Isariopsis Leaf Spot": {
        "crop": "Grape",
        "category": "Fungal Disease",
        "symptoms": "Irregular dark brown leaf spots with distinct halos, occasionally leading to premature defoliation.",
        "immediate_actions": [
            "Prune foliage to open up the canopy and allow morning dew to dry swiftly.",
            "Ensure leaves do not touch wet soil.",
        ],
        "preventative_care": [
            "Apply copper-based spray in late spring.",
            "Rake and bury or compost fallen leaves away from the vineyard row.",
        ],
        "outdoor_tasks": [
            "Check lower vine canopy for shaded leaves that stay wet past 10 AM.",
            "Check leaf underside for dark fungal sporulation.",
            "Adjust trellis wires to spread out dense leaf canopies.",
        ],
    },
    "Healthy Grape Plant": {
        "crop": "Grape",
        "category": "Healthy",
        "symptoms": "Vigorous green foliage, healthy tendrils, and clear fruit clusters without spotting or mildew.",
        "immediate_actions": [
            "Continue standard canopy management: tuck shoots into trellis wires.",
            "Water deeply every 10-14 days during dry spells depending on soil type.",
        ],
        "preventative_care": [
            "Thin excess grape clusters to maintain vine vigor and fruit quality.",
            "Ensure good airflow through routine summer leaf pulling around fruit zones.",
        ],
        "outdoor_tasks": [
            "Tuck runaway vine shoots into trellis wires.",
            "Check moisture at 6-inch depth near vine root zone.",
            "Feel the sturdy, waxy texture of healthy grape leaves.",
        ],
    },

    # --- ORANGE ---
    "Orange with Citrus Greening": {
        "crop": "Orange",
        "category": "Bacterial Disease",
        "symptoms": "Asymmetrical blotchy leaf yellowing, vein corking, small lopsided bitter fruit that stays green at base.",
        "immediate_actions": [
            "Inspect the plant for the Asian Citrus Psyllid insect vector (tiny aphid-like bugs feeding at a 45° angle).",
            "Contact your local agricultural extension service immediately; Citrus Greening (Huanglongbing) is federally quarantined in many citrus regions.",
            "Support tree health with balanced micronutrient foliar spray (zinc, iron, manganese).",
        ],
        "preventative_care": [
            "Source certified disease-free citrus nursery stock only.",
            "Control psyllid vectors with organic insecticidal soap or horticultural oils on flush growth.",
            "Keep trees well-nourished to help manage tree vigor.",
        ],
        "outdoor_tasks": [
            "Look closely at leaf patterns: asymmetrical blotchy mottle (not mirroring across the central vein) suggests greening.",
            "Check young tender leaf flushes for tiny jumpy psyllids or waxy honeydew secretions.",
            "Record plant location and contact county extension if confirmed.",
        ],
    },

    # --- PEACH ---
    "Peach with Bacterial Spot": {
        "crop": "Peach",
        "category": "Bacterial Disease",
        "symptoms": "Angular, water-soaked purplish-brown leaf spots that drop out, creating a 'shot-hole' appearance.",
        "immediate_actions": [
            "Avoid overhead sprinklers or wetting the canopy during warm weather.",
            "Prune trees to open vase shapes to optimize wind penetration and rapid drying.",
            "Do not prune or work in the orchard while foliage is wet.",
        ],
        "preventative_care": [
            "Plant bacterial spot-resistant peach cultivars (e.g., Candor, Dixired, Redhaven).",
            "Apply dormant copper sprays in autumn after leaf fall and before spring bud swell.",
            "Maintain moderate tree vigor; avoid over-fertilizing with nitrogen.",
        ],
        "outdoor_tasks": [
            "Hold leaves up to the light to see if leaf centers have dropped out ('shot-holes').",
            "Check fruit surfaces for cracked, pitted bacterial spots.",
            "Inspect sprinkler nozzles to ensure they aim low at the soil.",
        ],
    },
    "Healthy Peach Plant": {
        "crop": "Peach",
        "category": "Healthy",
        "symptoms": "Long, lance-shaped leaves are vibrant green and free from holes, curl, or gumming.",
        "immediate_actions": [
            "Maintain steady moisture during fruit swell.",
            "Thin crowded fruit to 6 inches apart for larger, healthier peaches.",
        ],
        "preventative_care": [
            "Apply dormant horticultural spray before bud break to ward off leaf curl.",
            "Mulch around drip line to retain soil humidity.",
        ],
        "outdoor_tasks": [
            "Inspect branch crotches for any clear sap oozing.",
            "Touch the soil to verify moisture 2 inches beneath tree mulch.",
            "Appreciate the graceful shape and fragrant foliage of your peach tree.",
        ],
    },

    # --- BELL PEPPER ---
    "Bell Pepper with Bacterial Spot": {
        "crop": "Bell Pepper",
        "category": "Bacterial Disease",
        "symptoms": "Small, water-soaked, dark spots on leaves with pale centers; leaves may yellow and drop prematurely.",
        "immediate_actions": [
            "Remove severely blighted lower leaves immediately to stop splash transmission.",
            "Water solely at the base using drip lines or watering cans without splashing soil.",
            "Sterilize hands and tools before handling neighboring nightshade plants.",
        ],
        "preventative_care": [
            "Use certified disease-free seed or transplant starts.",
            "Rotate peppers away from tomatoes, eggplants, and potatoes for at least 2 years.",
            "Apply organic copper bactericide early in the season according to label guidelines.",
        ],
        "outdoor_tasks": [
            "Inspect undersides of pepper leaves for water-soaked greasy spots.",
            "Check that soil mulch covers bare ground to stop soil splashing onto bottom leaves.",
            "Feel soil moisture around roots before watering.",
        ],
    },
    "Healthy Bell Pepper Plant": {
        "crop": "Bell Pepper",
        "category": "Healthy",
        "symptoms": "Glossy, uniform deep green leaves, sturdy stem, and crisp white flowers or firm peppers.",
        "immediate_actions": [
            "Water regularly (1-2 inches weekly) to prevent blossom end rot.",
            "Stake or cage plants as peppers develop to prevent stem snapping.",
        ],
        "preventative_care": [
            "Ensure 6-8 hours of direct daily sunlight.",
            "Feed with balanced organic vegetable fertilizer once flowering starts.",
        ],
        "outdoor_tasks": [
            "Check stake ties to confirm stems are supported without being strangled.",
            "Inspect flower blossoms for healthy set.",
            "Touch the soil to ensure even, steady moisture.",
        ],
    },

    # --- POTATO ---
    "Potato with Early Blight": {
        "crop": "Potato",
        "category": "Fungal Disease",
        "symptoms": "Dark brown circular spots with distinctive concentric rings ('target-board' pattern) on older leaves.",
        "immediate_actions": [
            "Prune off infected lower leaves touching or close to the ground.",
            "Mulch heavily with clean straw to prevent soil-borne spores from splashing onto foliage.",
            "Water plants in the morning so sun evaporates any moisture quickly.",
        ],
        "preventative_care": [
            "Practice a 3-year crop rotation avoiding all nightshade family members.",
            "Maintain soil organic matter and ensure plants receive adequate potassium and nitrogen.",
            "Ensure tubers are well-hilled with soil to prevent spore washing onto potatoes.",
        ],
        "outdoor_tasks": [
            "Look for 'target board' concentric rings on the lowest leaves.",
            "Add clean straw mulch around potato hills.",
            "Check that growing tubers are covered with soil and not turning green in sunlight.",
        ],
    },
    "Potato with Late Blight": {
        "crop": "Potato",
        "category": "Fungal Disease",
        "symptoms": "Water-soaked dark lesions that rapidly expand into greasy black patches; white fuzzy mold underneath in humid conditions.",
        "immediate_actions": [
            "CRITICAL: Late blight (Phytophthora infestans) spreads aggressively. Remove and bag infected foliage immediately.",
            "Do not compost infected plants; seal in trash bags.",
            "Keep tubers dry and well covered with soil to protect harvest.",
        ],
        "preventative_care": [
            "Plant certified disease-free seed potatoes only.",
            "Avoid planting near tomatoes affected by late blight.",
            "Notify neighboring gardeners or local community gardens if late blight is active in your area.",
        ],
        "outdoor_tasks": [
            "Examine underside of rapidly wilting leaves for delicate white downy mold.",
            "Check the potato hill to ensure no tubers are exposed to spore-laden rain.",
            "Wash and sanitize garden boots after walking through affected beds.",
        ],
    },
    "Healthy Potato Plant": {
        "crop": "Potato",
        "category": "Healthy",
        "symptoms": "Vigorous bushy green mounds of foliage, healthy leaf texture, and absence of target spots.",
        "immediate_actions": [
            "Keep soil hilled up around the base of the stems every 2 weeks.",
            "Maintain consistent soil moisture without waterlogging.",
        ],
        "preventative_care": [
            "Top-dress with clean straw or leaf compost to insulate root zone.",
            "Scout weekly for Colorado potato beetles under leaves.",
        ],
        "outdoor_tasks": [
            "Hill up 3 inches of loose soil or straw around the stem base.",
            "Inspect underside of leaves for bright orange beetle egg clusters.",
            "Feel the dampness of the potato mound beneath the mulch.",
        ],
    },

    # --- RASPBERRY ---
    "Healthy Raspberry Plant": {
        "crop": "Raspberry",
        "category": "Healthy",
        "symptoms": "Canes are strong with serrated, rich green leaves and bright silvery undersides.",
        "immediate_actions": [
            "Support canes on trellis wires to keep berries and leaves off the dirt.",
            "Ensure 1-2 inches of water per week during fruiting.",
        ],
        "preventative_care": [
            "Prune out spent floricanes (second-year brown woody canes) after fruiting to promote primocane growth.",
            "Thin cane density to 4-5 canes per linear foot for good airflow.",
        ],
        "outdoor_tasks": [
            "Distinguish green first-year primocanes from woody floricanes.",
            "Check soil moisture around the shallow root runners.",
            "Fasten loose canes to support wire with soft plant ties.",
        ],
    },

    # --- SOYBEAN ---
    "Healthy Soybean Plant": {
        "crop": "Soybean",
        "category": "Healthy",
        "symptoms": "Trifoliate leaves are clean, uniformly green, with healthy pod formation along stems.",
        "immediate_actions": [
            "Maintain moderate soil moisture.",
            "Keep plot weed-free during early growth stages.",
        ],
        "preventative_care": [
            "Inoculate seed with nitrogen-fixing rhizobia prior to planting.",
            "Rotate crops annually to break weed and pest cycles.",
        ],
        "outdoor_tasks": [
            "Examine nodules on root systems if a sample plant is uprooted.",
            "Check pod fill along the central stalk.",
            "Spend time walking the field rows inspecting general leaf vigor.",
        ],
    },

    # --- SQUASH ---
    "Squash with Powdery Mildew": {
        "crop": "Squash",
        "category": "Fungal Disease",
        "symptoms": "White talcum-powder-like spots on upper and lower surfaces of leaves and stems; leaves may turn yellow and crisp.",
        "immediate_actions": [
            "Snip off the oldest, heavily mildewed leaves near the base using clean pruners.",
            "Water solely at the soil level using soaker hoses; do not get squash leaves wet.",
            "Give vines room to breathe by repositioning stems or clearing nearby weeds.",
        ],
        "preventative_care": [
            "Spray leaves with a mild organic baking soda solution (1 tbsp baking soda + 1 tsp horticultural soap in 1 gal water) early in morning.",
            "Choose powdery mildew-resistant squash varieties (labeled PMR) next season.",
            "Ensure full sun exposure (at least 6-8 hours daily).",
        ],
        "outdoor_tasks": [
            "Check large, mature squash leaves for dusty white powder circles.",
            "Carefully cut away yellowing leaves that touch damp ground.",
            "Feel the top inch of soil around the root crown to test for dry crusting.",
        ],
    },

    # --- STRAWBERRY ---
    "Strawberry with Leaf Scorch": {
        "crop": "Strawberry",
        "category": "Fungal Disease",
        "symptoms": "Numerous small, dark purple or reddish spots on leaves that expand and turn brown, making foliage look burned.",
        "immediate_actions": [
            "Clip off badly scorched leaves and dispose of them in garbage.",
            "Avoid overhead sprinkler irrigation; wet foliage promotes rapid spore germination.",
            "Ensure strawberry crowns are not buried too deeply in soil.",
        ],
        "preventative_care": [
            "Renovate strawberry beds after harvest by mowing old foliage above crowns.",
            "Replace strawberry plants every 3 to 4 years to prevent chronic disease buildup.",
            "Space plants 12-18 inches apart to allow sun and air into the crown.",
        ],
        "outdoor_tasks": [
            "Inspect old runner leaves for purple margin scorch.",
            "Check that clean straw or pine mulch keeps berries off damp earth.",
            "Remove dead leaves from strawberry crown zone.",
        ],
    },
    "Healthy Strawberry Plant": {
        "crop": "Strawberry",
        "category": "Healthy",
        "symptoms": "Three-part leaflets are lustrous deep green, crowns are firm, and runners are vigorous.",
        "immediate_actions": [
            "Keep soil evenly moist, especially when flowering and setting fruit.",
            "Tuck straw mulch under leaves and berries to protect fruit.",
        ],
        "preventative_care": [
            "Trim excess runners if you want the plant to focus energy on berry size.",
            "Feed lightly with balanced organic fertilizer in early spring.",
        ],
        "outdoor_tasks": [
            "Feel the crown of the strawberry plant: it should sit flush with ground level, not buried.",
            "Check under foliage for any slugs or hidden berries.",
            "Bask in the sweet aroma of healthy strawberry foliage in the morning sun.",
        ],
    },

    # --- TOMATO ---
    "Tomato with Bacterial Spot": {
        "crop": "Tomato",
        "category": "Bacterial Disease",
        "symptoms": "Small, dark, greasy or water-soaked spots with yellow halos on leaves; leaves turn yellow and drop.",
        "immediate_actions": [
            "Prune off infected lower leaves with sanitized shears to reduce splash.",
            "Water only at ground level; do not splash soil onto foliage.",
            "Work with plants only when completely dry.",
        ],
        "preventative_care": [
            "Apply organic copper fungicide/bactericide at first sign of symptoms.",
            "Rotate tomato plots every 2-3 years away from all solanaceous plants.",
            "Mulch base of plants with 2 inches of clean straw.",
        ],
        "outdoor_tasks": [
            "Inspect leaf undersides for small water-soaked specks.",
            "Ensure mulch completely covers the soil around the tomato base.",
            "Disinfect your pruning shears with alcohol wipes.",
        ],
    },
    "Tomato with Early Blight": {
        "crop": "Tomato",
        "category": "Fungal Disease",
        "symptoms": "Dark brown spots with prominent concentric rings ('bullseye' or target pattern) surrounded by yellow halos.",
        "immediate_actions": [
            "Remove lower foliage showing concentric ring spots up to 12 inches above the soil.",
            "Apply fresh straw mulch underneath plants immediately to block soil splash.",
            "Stake or cage tomatoes to keep foliage elevated and dry.",
        ],
        "preventative_care": [
            "Water deeply at the base early in the morning.",
            "Spray with organic biofungicide (e.g., Bacillus subtilis) or copper soap preventively.",
            "Practice 3-year crop rotation.",
        ],
        "outdoor_tasks": [
            "Look for concentric 'bullseye' rings on the bottom leaves.",
            "Prune lowest leaves so none touch the ground or mulch.",
            "Check tie supports on stakes or cages.",
        ],
    },
    "Tomato with Late Blight": {
        "crop": "Tomato",
        "category": "Fungal Disease",
        "symptoms": "Large, irregular, water-soaked grey-green lesions turning brown and papery; white fuzz under leaves in high humidity.",
        "immediate_actions": [
            "Late blight is fast-moving. Prune and bag infected branches in plastic bags immediately.",
            "Keep foliage completely dry; stop all overhead watering.",
            "Harvest mature green fruit right away if weather is wet and cool.",
        ],
        "preventative_care": [
            "Plant late blight-resistant varieties (e.g., Defiant, Mountain Merit, Jasper).",
            "Ensure generous plant spacing (at least 3 feet apart).",
            "Clean and destroy all spent vines at season end; do not compost.",
        ],
        "outdoor_tasks": [
            "Look for fuzzy white mold on leaf undersides on cloudy, cool mornings.",
            "Inspect green tomatoes for firm, greasy olive-brown blotches.",
            "Check that airflow between adjacent plants is unobstructed.",
        ],
    },
    "Tomato with Leaf Mold": {
        "crop": "Tomato",
        "category": "Fungal Disease",
        "symptoms": "Pale greenish-yellow spots on upper leaf surfaces and velvety olive-green to brown mold on the undersides.",
        "immediate_actions": [
            "Common in high tunnels and greenhouses: immediately increase ventilation and open vents or fans.",
            "Prune suckers and dense internal foliage to lower relative humidity below 85%.",
            "Water early in the morning at the root zone.",
        ],
        "preventative_care": [
            "Choose leaf mold-resistant tomato varieties.",
            "Space plants generously in protected growing areas.",
            "Apply copper-based organic spray if disease recurs.",
        ],
        "outdoor_tasks": [
            "Turn leaves over to check for velvety olive-brown mold.",
            "Open greenhouse doors or greenhouse roll-up sides for ventilation.",
            "Check soil moisture at the base of the tomato root ball.",
        ],
    },
    "Tomato with Septoria Leaf Spot": {
        "crop": "Tomato",
        "category": "Fungal Disease",
        "symptoms": "Numerous small, circular spots with dark brown margins and sunken greyish-white centers containing tiny black speckles.",
        "immediate_actions": [
            "Strip off infected leaves starting from the bottom of the plant.",
            "Mulch soil generously to prevent rainwater splash from the dirt.",
            "Clean hands and pruners with rubbing alcohol after handling infected plants.",
        ],
        "preventative_care": [
            "Never work among wet tomato plants.",
            "Rotate garden beds away from peppers, eggplants, and tomatoes.",
            "Apply preventive organic copper spray on lower foliage.",
        ],
        "outdoor_tasks": [
            "Inspect lowest leaves for small circular spots with white centers and black pinpoints.",
            "Lay down fresh straw mulch under the tomato canopy.",
            "Feel the soil moisture 2 inches down to gauge watering needs.",
        ],
    },
    "Tomato with Spider Mites or Two-spotted Spider Mite": {
        "crop": "Tomato",
        "category": "Pest Infestation",
        "symptoms": "Fine yellow or bronze stippling on leaves, dusty appearance, and delicate silky webbing on leaf undersides and branch crotches.",
        "immediate_actions": [
            "Spray undersides of leaves with a firm stream of water to dislodge mite colonies and destroy webs.",
            "Apply insecticidal soap or neem oil spray early in morning or dusk (never in hot midday sun).",
            "Isolate heavily infested plants if grown in pots.",
        ],
        "preventative_care": [
            "Keep plants adequately watered; spider mites thrive in hot, dry, dusty conditions.",
            "Avoid broad-spectrum chemical insecticides that kill natural predatory mites and ladybugs.",
            "Introduce beneficial predatory mites (Phytoseiulus persimilis) in enclosed gardens.",
        ],
        "outdoor_tasks": [
            "Hold a white sheet of paper under suspect foliage and tap gently; look for tiny moving specks.",
            "Search branch nodes and leaf undersides for fine silky webbing.",
            "Mist soil surface and surrounding pathways to increase local humidity.",
        ],
    },
    "Tomato with Target Spot": {
        "crop": "Tomato",
        "category": "Fungal Disease",
        "symptoms": "Brown circular lesions on leaves with pale centers and concentric circles, progressing to defoliation.",
        "immediate_actions": [
            "Prune infected foliage cleanly and remove from garden.",
            "Ensure drip irrigation is used to keep foliage dry.",
            "Stake plants securely to keep branches elevated.",
        ],
        "preventative_care": [
            "Improve air movement by spacing plants at least 3 feet apart.",
            "Destroy old crop residue at end of season.",
            "Apply organic protective fungicide during humid, rainy spells.",
        ],
        "outdoor_tasks": [
            "Inspect middle and lower canopy leaves for circular target lesions.",
            "Verify stake ties are secure and uplifting heavy branches.",
            "Measure airflow and spacing between tomato rows.",
        ],
    },
    "Tomato Yellow Leaf Curl Virus": {
        "crop": "Tomato",
        "category": "Viral Disease",
        "symptoms": "Upward curling and cupping of leaves, prominent yellowing of leaf margins, severe stunting, and flower drop.",
        "immediate_actions": [
            "Viruses cannot be cured once inside the plant. Remove and destroy infected plants to prevent transmission to others.",
            "Control the insect vector: Silverleaf whiteflies. Inspect leaf undersides for tiny moth-like white insects.",
            "Use yellow sticky traps around remaining tomatoes to monitor whitefly activity.",
        ],
        "preventative_care": [
            "Plant virus-resistant tomato cultivars (labeled TYLCV-resistant).",
            "Use fine insect netting (floating row covers) over young transplants.",
            "Eliminate weed hosts (such as nightshades and mallow) around the garden perimeter.",
        ],
        "outdoor_tasks": [
            "Gently shake tomato plants to see if tiny whiteflies flutter up.",
            "Check if leaf margins are cupping upwards like tiny spoons.",
            "Set up yellow sticky cards near plant canopies to monitor insect vectors.",
        ],
    },
    "Tomato Mosaic Virus": {
        "crop": "Tomato",
        "category": "Viral Disease",
        "symptoms": "Mottled dark green and light green 'mosaic' leaf patterns, fern-like leaf distortion, and stunted growth.",
        "immediate_actions": [
            "Remove and discard infected plants; do not compost.",
            "Virus is mechanically transmitted by touch and tobacco products: wash hands thoroughly with soap.",
            "Sterilize all garden tools, stakes, and tomato cages in a 10% bleach solution.",
        ],
        "preventative_care": [
            "Plant mosaic virus-resistant tomato varieties (look for 'T' or 'ToMV' designations).",
            "Never smoke, vape, or handle tobacco before working in the garden.",
            "Disinfect stakes and trellis twine each season.",
        ],
        "outdoor_tasks": [
            "Look for alternating light and dark green mosaic patterns on younger leaves.",
            "Disinfect your pruning shears and garden gloves with soapy water or sanitizing solution.",
            "Check neighboring plants for similar leaf twisting or mottled colors.",
        ],
    },
    "Healthy Tomato Plant": {
        "crop": "Tomato",
        "category": "Healthy",
        "symptoms": "Robust green foliage with characteristic tomato aroma, stout stems, clear leaves, and healthy yellow blossoms.",
        "immediate_actions": [
            "Maintain deep, consistent watering at root level (1-2 inches weekly).",
            "Pinch out lower suckers if pruning to a single or double leader for better airflow.",
        ],
        "preventative_care": [
            "Keep lower 12 inches of stem free of leaves to stop soil pathogens from splashing up.",
            "Apply organic balanced fertilizer (high in potassium and phosphorus for fruiting).",
            "Mulch generously around base with organic straw or untreated grass clippings.",
        ],
        "outdoor_tasks": [
            "Gently prune any suckers growing in the branch crotches.",
            "Check that the main stem is loosely tied to its stake or cage.",
            "Breathe in the rich, earthy scent of healthy tomato leaves in the garden!",
        ],
    },
}

# Generic fallback for unlisted or uncertain classes
GENERIC_CARE_RECOMMENDATION = {
    "crop": "Unknown / General Plant",
    "category": "Uncertain Prediction",
    "symptoms": "Symptoms are not clearly matching a high-confidence diagnostic profile.",
    "immediate_actions": [
        "Take a clearer photo in bright, indirect natural daylight against a simple, uncluttered background.",
        "Inspect the plant in person: check both upper and lower leaf surfaces, stem, and soil.",
        "Do not apply harsh chemicals without confirming the specific disease or pest.",
    ],
    "preventative_care": [
        "Water at the soil line rather than overhead to minimize moisture on foliage.",
        "Ensure the pot or garden bed has adequate drainage to avoid root rot.",
        "Consult your local agricultural extension service or master gardener clinic with physical leaf samples.",
    ],
    "outdoor_tasks": [
        "Step outside and examine the real plant in natural daylight.",
        "Insert your finger 2 inches into the soil to check moisture level.",
        "Inspect nearby leaves and stems for discoloration, webbing, or insects.",
        "Take a clear, close-up photo of the leaf flat against a neutral card or palm.",
    ],
}


def get_recommendation(prediction_label: str) -> Dict[str, Any]:
    """
    Retrieve care recommendations and outdoor tasks for a given predicted class.
    Falls back gracefully if the label is unrecognized.
    """
    rec = DISEASE_KNOWLEDGE_BASE.get(prediction_label)
    if rec:
        return {
            "label": prediction_label,
            **rec
        }
    return {
        "label": prediction_label or "Unknown Condition",
        **GENERIC_CARE_RECOMMENDATION
    }


def get_all_supported_crops() -> List[str]:
    """Returns sorted list of distinct crops covered in the knowledge base."""
    crops = {info["crop"] for info in DISEASE_KNOWLEDGE_BASE.values()}
    return sorted(list(crops))


def get_all_classes() -> List[str]:
    """Returns all 38 supported class names."""
    return list(DISEASE_KNOWLEDGE_BASE.keys())
