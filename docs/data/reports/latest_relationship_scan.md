# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T16:07:33.702986+00:00`
- Price records: `672`
- Market context records: `2678`
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

- `market_context_high->crypto_alt_24h` score `9.0929` n `111` status `ready` deltaP `16.0051` edge `1.0004` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6965` n `111` status `ready` deltaP `17.8256` edge `0.6387` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `2.9459` n `130` status `ready` deltaP `20.4011` edge `0.3746` maxDD `-15.2094`
- `market_context_high->unknown_4h` score `1.3526` n `130` status `ready` deltaP `7.228` edge `0.1695` maxDD `-3.7312`
- `market_context_high->crypto_major_4h` score `0.2898` n `130` status `ready` deltaP `8.4334` edge `0.2157` maxDD `-14.4477`
- `market_context_high->index_4h` score `0.0457` n `130` status `ready` deltaP `9.5708` edge `0.0262` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.15` n `138` status `ready` deltaP `3.0548` edge `0.0098` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.229` n `111` status `ready` deltaP `10.1258` edge `0.0006` maxDD `-0.6418`
- `market_context_high->index_24h` score `-0.4489` n `111` status `ready` deltaP `6.0999` edge `0.02` maxDD `-2.5127`
- `market_context_high->commodity_1h` score `-0.4681` n `138` status `ready` deltaP `1.7725` edge `0.0035` maxDD `-4.3601`
- `market_context_high->commodity_24h` score `-0.5132` n `111` status `ready` deltaP `7.9627` edge `0.1905` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5165` n `138` status `ready` deltaP `-0.371` edge `0.0038` maxDD `-0.2164`
- `market_context_high->fx_4h` score `-0.5463` n `130` status `ready` deltaP `1.1023` edge `0.0125` maxDD `-0.5631`
- `market_context_high->unknown_1h` score `-0.5921` n `138` status `ready` deltaP `1.8268` edge `0.0113` maxDD `-3.1587`
- `market_context_high->crypto_alt_1h` score `-0.6593` n `138` status `ready` deltaP `6.372` edge `0.049` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7215` n `138` status `ready` deltaP `-1.4493` edge `-0.0005` maxDD `-2.9203`
- `market_context_high->crypto_major_1h` score `-1.0544` n `138` status `ready` deltaP `3.3238` edge `0.0296` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.2686` n `130` status `ready` deltaP `3.2505` edge `0.0077` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2793` n `138` status `ready` deltaP `-4.9574` edge `0.0103` maxDD `-2.7085`
- `market_context_high->crypto_major_24h` score `-1.2956` n `111` status `ready` deltaP `5.9967` edge `0.5502` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
