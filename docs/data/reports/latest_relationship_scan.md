# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T15:37:30.501138+00:00`
- Price records: `672`
- Market context records: `2675`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_alt_24h` score `9.0221` n `111` status `ready` deltaP `16.0051` edge `0.9945` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.604` n `111` status `ready` deltaP `17.4784` edge `0.6333` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.2783` n `129` status `ready` deltaP `20.896` edge `0.399` maxDD `-15.2094`
- `market_context_high->unknown_4h` score `1.4225` n `129` status `ready` deltaP `7.5167` edge `0.1734` maxDD `-3.7312`
- `market_context_high->crypto_major_4h` score `0.7402` n `129` status `ready` deltaP `8.8628` edge `0.2352` maxDD `-11.6172`
- `market_context_high->index_4h` score `0.0129` n `129` status `ready` deltaP `9.2846` edge `0.0239` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1485` n `138` status `ready` deltaP `3.0548` edge `0.01` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.1928` n `111` status `ready` deltaP `10.473` edge `0.0013` maxDD `-0.6418`
- `market_context_high->index_24h` score `-0.3659` n `111` status `ready` deltaP `6.4471` edge `0.0246` maxDD `-2.5127`
- `market_context_high->commodity_1h` score `-0.4424` n `138` status `ready` deltaP `2.0719` edge `0.0048` maxDD `-4.3601`
- `market_context_high->commodity_24h` score `-0.5038` n `111` status `ready` deltaP `7.9627` edge `0.1917` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.5239` n `129` status `ready` deltaP `1.3673` edge `0.0126` maxDD `-0.5631`
- `market_context_high->fx_1h` score `-0.5285` n `138` status `ready` deltaP `-0.5207` edge `0.0038` maxDD `-0.2164`
- `market_context_high->unknown_1h` score `-0.6556` n `138` status `ready` deltaP `1.5274` edge `0.008` maxDD `-3.1587`
- `market_context_high->crypto_alt_1h` score `-0.685` n `138` status `ready` deltaP `6.372` edge `0.0457` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7129` n `138` status `ready` deltaP `-1.2996` edge `-0.0004` maxDD `-2.9203`
- `market_context_high->crypto_major_1h` score `-1.0809` n `138` status `ready` deltaP `3.1741` edge `0.0272` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.2601` n `138` status `ready` deltaP `-4.8077` edge `0.0109` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2676` n `129` status `ready` deltaP `3.2095` edge `0.0081` maxDD `-10.0279`
- `market_context_high->crypto_major_24h` score `-1.3432` n `111` status `ready` deltaP `5.9967` edge `0.5441` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
