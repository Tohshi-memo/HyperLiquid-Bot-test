# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T20:22:24.667403+00:00`
- Price records: `672`
- Market context records: `8021`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11816`

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

- `market_context_high->equity_24h` score `15.977` n `88` status `ready` deltaP `25.26` edge `1.2972` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.8356` n `88` status `ready` deltaP `35.8752` edge `0.4138` maxDD `0.0`
- `market_context_high->equity_4h` score `6.2895` n `101` status `ready` deltaP `24.7962` edge `0.4481` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.7576` n `88` status `ready` deltaP `23.0837` edge `0.2122` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.4917` n `101` status `ready` deltaP `22.5869` edge `0.1193` maxDD `-0.979`
- `market_context_high->index_4h` score `2.4823` n `101` status `ready` deltaP `25.9415` edge `0.0699` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.9816` n `88` status `ready` deltaP `11.6039` edge `0.1548` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.7053` n `101` status `ready` deltaP `14.2749` edge `0.1287` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3259` n `88` status `ready` deltaP `25.3899` edge `0.0361` maxDD `-2.5901`
- `market_context_high->index_1h` score `0.8621` n `101` status `ready` deltaP `14.0333` edge `0.0213` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6516` n `101` status `ready` deltaP `9.44` edge `0.0292` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6129` n `101` status `ready` deltaP `11.6277` edge `0.0421` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.5976` n `101` status `ready` deltaP `9.1806` edge `0.1604` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.5671` n `101` status `ready` deltaP `5.9059` edge `0.1196` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0557` n `101` status `ready` deltaP `2.2336` edge `0.0355` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3125` n `101` status `ready` deltaP `-0.621` edge `0.0008` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4008` n `101` status `ready` deltaP `5.6649` edge `0.0036` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.6074` n `101` status `ready` deltaP `-1.5089` edge `-0.0055` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2216` n `101` status `ready` deltaP `0.0406` edge `-0.0067` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8788` n `101` status `ready` deltaP `7.3916` edge `-0.1635` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
