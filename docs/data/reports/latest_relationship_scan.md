# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T21:22:24.951322+00:00`
- Price records: `672`
- Market context records: `6019`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11126`

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

- `news_risk_high->fx_24h` score `7.7078` n `30` status `ready` deltaP `69.6181` edge `0.1782` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2321` n `30` status `ready` deltaP `43.811` edge `0.0652` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3446` n `30` status `ready` deltaP `28.8542` edge `0.1069` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.243` n `30` status `ready` deltaP `26.9261` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4042` n `209` status `ready` deltaP `8.3944` edge `0.1597` maxDD `-3.2247`
- `market_context_high->equity_24h` score `1.2087` n `183` status `ready` deltaP `28.4836` edge `0.5102` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8302` n `30` status `ready` deltaP `10.3393` edge `0.0842` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2208` n `30` status `ready` deltaP `5.4691` edge `0.038` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1382` n `30` status `ready` deltaP `9.2361` edge `0.0433` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3594` n `209` status `ready` deltaP `4.1845` edge `0.0059` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.404` n `30` status `ready` deltaP `1.5369` edge `-0.0254` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.6665` n `209` status `ready` deltaP `-1.4662` edge `-0.0005` maxDD `-0.6214`
- `market_context_high->index_24h` score `-0.6892` n `183` status `ready` deltaP `4.5367` edge `0.07` maxDD `-7.0886`
- `market_context_high->fx_1h` score `-0.6979` n `209` status `ready` deltaP `-0.9527` edge `-0.0016` maxDD `-0.6829`
- `market_context_high->equity_1h` score `-0.9993` n `209` status `ready` deltaP `0.6855` edge `0.025` maxDD `-4.3608`
- `market_context_high->index_4h` score `-1.0156` n `209` status `ready` deltaP `2.0853` edge `0.0168` maxDD `-2.5393`
- `news_risk_high->index_1h` score `-1.036` n `30` status `ready` deltaP `-9.4012` edge `-0.0187` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.0387` n `209` status `ready` deltaP `4.3632` edge `0.0031` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.0477` n `209` status `ready` deltaP `-1.954` edge `-0.0109` maxDD `-2.8312`
- `market_context_high->crypto_alt_1h` score `-1.0485` n `209` status `ready` deltaP `2.8694` edge `0.0217` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
