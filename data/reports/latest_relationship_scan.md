# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T14:22:30.592976+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5897`

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

- `market_context_high->unknown_24h` score `130.245` n `40` status `ready` deltaP `30.3819` edge `10.6512` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.259` n `40` status `ready` deltaP `50.9375` edge `0.6384` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.7951` n `40` status `ready` deltaP `51.1458` edge `0.5714` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.302` n `31` status `ready` deltaP `-6.9728` edge `0.2234` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9918` n `31` status `ready` deltaP `20.5862` edge `0.0111` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9401` n `31` status `ready` deltaP `12.192` edge `0.0623` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3899` n `47` status `ready` deltaP `8.1634` edge `0.033` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.3652` n `31` status `ready` deltaP `14.1621` edge `-0.0139` maxDD `-1.6728`
- `market_context_high->commodity_4h` score `0.3146` n `47` status `ready` deltaP `5.0338` edge `0.0914` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1959` n `31` status `ready` deltaP `0.0885` edge `0.0538` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1383` n `31` status `ready` deltaP `4.8928` edge `0.0354` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.0041` n `31` status `ready` deltaP `3.4914` edge `-0.004` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.024` n `47` status `ready` deltaP `6.6664` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.0458` n `31` status `ready` deltaP `10.9909` edge `-0.0151` maxDD `-3.1233`
- `market_context_high->fx_4h` score `-0.1509` n `47` status `ready` deltaP `11.8935` edge `-0.0062` maxDD `-1.8531`
- `news_risk_high->fx_1h` score `-0.235` n `31` status `ready` deltaP `-0.2656` edge `0.0028` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.572` n `31` status `ready` deltaP `-2.2117` edge `-0.001` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6719` n `40` status `ready` deltaP `0.6597` edge `0.0376` maxDD `-2.506`
- `market_context_high->crypto_alt_4h` score `-0.6817` n `47` status `ready` deltaP `0.0097` edge `0.0031` maxDD `-4.9116`
- `news_risk_high->crypto_major_1h` score `-0.8712` n `31` status `ready` deltaP `2.8105` edge `-0.0584` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
