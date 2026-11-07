# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T09:37:26.450776+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3905`

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

- `news_risk_high->equity_4h` score `1.3047` n `62` status `ready` deltaP `12.4459` edge `0.1582` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6897` n `62` status `ready` deltaP `12.6229` edge `0.0211` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.305` n `62` status `ready` deltaP `9.4086` edge `0.1432` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.1273` n `62` status `ready` deltaP `-1.8762` edge `0.0673` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0466` n `62` status `ready` deltaP `7.2001` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.1072` n `62` status `ready` deltaP `-0.7485` edge `0.0462` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1238` n `62` status `ready` deltaP `3.0085` edge `0.0026` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2025` n `62` status `ready` deltaP `2.1194` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5556` n `62` status `ready` deltaP `-4.2737` edge `-0.007` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9728` n `62` status `ready` deltaP `0.9638` edge `-0.0406` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2062` n `62` status `ready` deltaP `-2.2938` edge `-0.0238` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.3131` n `62` status `ready` deltaP `-3.6192` edge `0.0162` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5967` n `62` status `ready` deltaP `-11.1744` edge `-0.0026` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-2.0038` n `62` status `ready` deltaP `-8.1804` edge `-0.0307` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2214` n `62` status `ready` deltaP `-3.0094` edge `-0.0027` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.7918` n `62` status `ready` deltaP `-5.2532` edge `-0.2615` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5299` n `62` status `ready` deltaP `-31.2795` edge `-0.0118` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.8963` n `62` status `ready` deltaP `20.8669` edge `0.3918` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6088` n `62` status `ready` deltaP `-28.7915` edge `-0.1261` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.487` n `62` status `ready` deltaP `-31.1436` edge `-0.1493` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
