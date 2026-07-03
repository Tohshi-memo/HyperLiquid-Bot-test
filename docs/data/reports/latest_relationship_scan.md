# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T15:52:28.479473+00:00`
- Price records: `672`
- Market context records: `5572`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `market_context_high->equity_24h` score `4.3853` n `176` status `ready` deltaP `15.2304` edge `0.7718` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2455` n `190` status `ready` deltaP `11.1361` edge `0.2588` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `0.9725` n `176` status `ready` deltaP `14.1256` edge `0.4409` maxDD `-29.6555`
- `market_context_high->fx_24h` score `0.7945` n `176` status `ready` deltaP `16.9034` edge `0.0509` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.7368` n `190` status `ready` deltaP `6.5196` edge `0.1818` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.668` n `190` status `ready` deltaP `6.5774` edge `0.1759` maxDD `-9.46`
- `market_context_high->index_1h` score `-0.1656` n `202` status `ready` deltaP `4.0404` edge `0.0086` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.2341` n `202` status `ready` deltaP `5.8472` edge `0.0422` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.2604` n `190` status `ready` deltaP `6.2981` edge `0.0097` maxDD `-0.8712`
- `market_context_high->fx_1h` score `-0.4056` n `202` status `ready` deltaP `1.7727` edge `0.0012` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.5142` n `202` status `ready` deltaP `-0.0459` edge `0.0019` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5185` n `202` status `ready` deltaP `1.3117` edge `0.0442` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6643` n `202` status `ready` deltaP `2.8784` edge `0.05` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.3302` n `202` status `ready` deltaP `-3.7647` edge `-0.0092` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5358` n `190` status `ready` deltaP `2.4358` edge `0.0167` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.998` n `176` status `ready` deltaP `13.084` edge `0.0553` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.1096` n `190` status `ready` deltaP `-13.9746` edge `-0.0622` maxDD `-12.1312`
- `market_context_high->commodity_4h` score `-4.5718` n `190` status `ready` deltaP `-8.5847` edge `-0.0562` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.8411` n `176` status `ready` deltaP `-7.5758` edge `-0.2178` maxDD `-32.9569`
- `market_context_high->crypto_alt_24h` score `-8.921` n `176` status `ready` deltaP `4.2298` edge `0.0981` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
