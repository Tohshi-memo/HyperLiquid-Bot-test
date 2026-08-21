# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T12:00:57.497807+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.4639` n `117` status `ready` deltaP `12.0503` edge `0.0071` maxDD `-0.5685`
- `market_context_high->equity_1h` score `0.4619` n `117` status `ready` deltaP `9.7178` edge `0.0552` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.1507` n `105` status `ready` deltaP `9.1623` edge `0.0085` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1096` n `117` status `ready` deltaP `2.5859` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.1326` n `105` status `ready` deltaP `3.6731` edge `0.1274` maxDD `-8.3685`
- `market_context_high->metal_4h` score `-0.2562` n `105` status `ready` deltaP `6.5302` edge `-0.0188` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3327` n `105` status `ready` deltaP `4.971` edge `0.0166` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3415` n `117` status `ready` deltaP `2.0498` edge `-0.0025` maxDD `-0.503`
- `market_context_high->unknown_1h` score `-0.4259` n `117` status `ready` deltaP `10.0991` edge `-0.0801` maxDD `-0.4843`
- `market_context_high->commodity_24h` score `-0.4432` n `105` status `ready` deltaP `4.5883` edge `0.1158` maxDD `-4.666`
- `market_context_high->commodity_1h` score `-0.7129` n `117` status `ready` deltaP `-5.2805` edge `0.0004` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7718` n `105` status `ready` deltaP `-2.9573` edge `0.0058` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.2961` n `117` status `ready` deltaP `-2.5717` edge `-0.0107` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4726` n `117` status `ready` deltaP `-3.9574` edge `-0.0673` maxDD `-3.6092`
- `market_context_high->fx_24h` score `-3.1236` n `105` status `ready` deltaP `-13.5169` edge `-0.0092` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.7574` n `105` status `ready` deltaP `-1.9686` edge `-0.173` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-4.0041` n `105` status `ready` deltaP `-0.1771` edge `-0.2304` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.1042` n `105` status `ready` deltaP `-4.5536` edge `-0.0456` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.4138` n `105` status `ready` deltaP `-16.7212` edge `-0.1236` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.6127` n `105` status `ready` deltaP `9.3354` edge `-0.396` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
