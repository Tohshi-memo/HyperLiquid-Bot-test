# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T09:37:29.312719+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `49.3239` n `51` status `ready` deltaP `17.0139` edge `3.9969` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.1091` n `51` status `ready` deltaP `40.237` edge `1.0006` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0551` n `51` status `ready` deltaP `24.2587` edge `0.9308` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.6896` n `51` status `ready` deltaP `48.9481` edge `0.163` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.745` n `51` status `ready` deltaP `27.0804` edge `0.2086` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5921` n `51` status `ready` deltaP `16.784` edge `0.2179` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.209` n `51` status `ready` deltaP `37.778` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `1.8625` n `83` status `ready` deltaP `3.7609` edge `0.1808` maxDD `-1.0533`
- `market_context_high->unknown_4h` score `1.8493` n `139` status `ready` deltaP `19.7447` edge `0.0633` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.5345` n `51` status `ready` deltaP `32.7614` edge `-0.0863` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2446` n `51` status `ready` deltaP `16.9954` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9646` n `51` status `ready` deltaP `18.6421` edge `0.0358` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9605` n `51` status `ready` deltaP `14.0064` edge `0.0264` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2504` n `51` status `ready` deltaP `9.4223` edge `0.0046` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2219` n `51` status `ready` deltaP `8.8382` edge `-0.0096` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.2115` n `139` status `ready` deltaP `11.162` edge `-0.0109` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.08` n `139` status `ready` deltaP `11.4095` edge `-0.0245` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1061` n `51` status `ready` deltaP `2.3424` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2349` n `51` status `ready` deltaP `6.6057` edge `-0.0105` maxDD `-0.249`
- `news_risk_high->crypto_alt_24h` score `-0.4295` n `51` status `ready` deltaP `22.3958` edge `-0.1851` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
