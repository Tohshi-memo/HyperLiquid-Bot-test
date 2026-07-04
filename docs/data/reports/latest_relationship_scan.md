# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T05:22:25.292926+00:00`
- Price records: `672`
- Market context records: `5630`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8743`

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

- `market_context_high->equity_24h` score `2.9551` n `174` status `ready` deltaP `15.0084` edge `0.6541` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.358` n `174` status `ready` deltaP `22.1325` edge `0.063` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.797` n `237` status `ready` deltaP `11.0045` edge `0.2223` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4673` n `237` status `ready` deltaP `7.3814` edge `0.1536` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.191` n `237` status `ready` deltaP `5.4596` edge `0.1326` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2883` n `237` status `ready` deltaP `1.4496` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4361` n `237` status `ready` deltaP `4.7172` edge `0.0329` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.541` n `237` status `ready` deltaP `-0.3064` edge `0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6537` n `237` status `ready` deltaP `1.137` edge `0.0341` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6733` n `237` status `ready` deltaP `3.9813` edge `0.0419` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9801` n `237` status `ready` deltaP `-0.0202` edge `0.0053` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0453` n `237` status `ready` deltaP `-0.7283` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3256` n `237` status `ready` deltaP `1.0658` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9454` n `237` status `ready` deltaP `-0.6219` edge `0.0092` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3613` n `174` status `ready` deltaP `10.0874` edge `0.0287` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9261` n `237` status `ready` deltaP `-12.3874` edge `-0.0542` maxDD `-11.7351`
- `market_context_high->crypto_major_24h` score `-3.6722` n `174` status `ready` deltaP `5.9866` edge `0.1081` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-3.982` n `237` status `ready` deltaP `-4.0168` edge `-0.0375` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2615` n `174` status `ready` deltaP `-10.9315` edge `-0.2502` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-13.1963` n `174` status `ready` deltaP `-4.2265` edge `-0.2018` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
