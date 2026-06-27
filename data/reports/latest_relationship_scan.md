# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T01:37:31.081610+00:00`
- Price records: `672`
- Market context records: `4885`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7592`

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

- `market_context_high->unknown_1h` score `16.0051` n `110` status `ready` deltaP `9.5727` edge `1.3117` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5431` n `110` status `ready` deltaP `22.8575` edge `0.696` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4388` n `110` status `ready` deltaP `21.2084` edge `0.5304` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.2398` n `110` status `ready` deltaP `18.6447` edge `0.5181` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.0146` n `91` status `ready` deltaP `24.0804` edge `0.2916` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1211` n `110` status `ready` deltaP `8.0627` edge `0.1059` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8727` n `110` status `ready` deltaP `12.439` edge `0.1671` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5905` n `110` status `ready` deltaP `12.1452` edge `0.041` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4742` n `110` status `ready` deltaP `6.4698` edge `0.1215` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4113` n `110` status `ready` deltaP `7.8715` edge `0.1025` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1966` n `110` status `ready` deltaP `3.9358` edge `0.0587` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.2017` n `110` status `ready` deltaP `0.2449` edge `0.0305` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2339` n `110` status `ready` deltaP `3.1328` edge `0.0151` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5172` n `110` status `ready` deltaP `-0.2885` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6822` n `110` status `ready` deltaP `0.7622` edge `0.0045` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9302` n `110` status `ready` deltaP `5.6624` edge `0.0034` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3226` n `110` status `ready` deltaP `-6.7175` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.7288` n `91` status `ready` deltaP `-5.1206` edge `-0.0089` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5256` n `91` status `ready` deltaP `-5.0615` edge `-0.1379` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.8645` n `91` status `ready` deltaP `14.3257` edge `0.01` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
