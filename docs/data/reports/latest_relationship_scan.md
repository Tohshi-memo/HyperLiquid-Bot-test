# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T04:52:17.661439+00:00`
- Price records: `672`
- Market context records: `2010`
- Flow alert records: `7676`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9107`

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

- `market_context_high->crypto_major_4h` score `8.8679` n `210` status `ready` deltaP `30.7781` edge `0.5868` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.306` n `210` status `ready` deltaP `24.4555` edge `0.6436` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.7331` n `210` status `ready` deltaP `18.8357` edge `0.4271` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.7698` n `210` status `ready` deltaP `15.8798` edge `0.2344` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.543` n `210` status `ready` deltaP `12.5848` edge `0.1433` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2559` n `210` status `ready` deltaP `10.1896` edge `0.1481` maxDD `-4.9097`
- `market_context_high->index_4h` score `1.2056` n `210` status `ready` deltaP `11.4793` edge `0.0923` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `0.8803` n `185` status `ready` deltaP `15.6599` edge `0.501` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.666` n `185` status `ready` deltaP `14.1596` edge `0.2037` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.4636` n `185` status `ready` deltaP `14.4715` edge `0.432` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.3524` n `185` status `ready` deltaP `15.1564` edge `0.0275` maxDD `-1.9342`
- `market_context_high->equity_1h` score `0.1168` n `210` status `ready` deltaP `6.1606` edge `0.0475` maxDD `-2.6402`
- `market_context_high->index_24h` score `-0.0987` n `185` status `ready` deltaP `2.7472` edge `0.0963` maxDD `-4.1604`
- `market_context_high->index_1h` score `-0.4077` n `210` status `ready` deltaP `1.4942` edge `0.0151` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8047` n `210` status `ready` deltaP `-0.7485` edge `0.0007` maxDD `-0.3548`
- `market_context_high->unknown_1h` score `-0.9448` n `210` status `ready` deltaP `3.6042` edge `-0.0308` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-1.0347` n `210` status `ready` deltaP `-6.4213` edge `-0.0017` maxDD `-1.0513`
- `market_context_high->metal_1h` score `-1.0782` n `210` status `ready` deltaP `2.7887` edge `0.0103` maxDD `-5.166`
- `market_context_high->crypto_major_24h` score `-1.4501` n `185` status `ready` deltaP `17.4666` edge `0.6213` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.6278` n `210` status `ready` deltaP `6.8568` edge `0.0809` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
