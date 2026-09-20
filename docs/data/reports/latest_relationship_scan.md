# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T21:22:23.772255+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10612`

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

- `news_risk_high->crypto_major_24h` score `24.3622` n `98` status `ready` deltaP `12.617` edge `2.6319` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.389` n `98` status `ready` deltaP `15.2671` edge `2.0854` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `7.3` n `44` status `ready` deltaP `-0.4158` edge `0.6261` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.6634` n `101` status `ready` deltaP `21.0532` edge `0.3692` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7381` n `101` status `ready` deltaP `20.4434` edge `0.301` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.5504` n `44` status `ready` deltaP `36.0587` edge `0.0688` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `2.8529` n `101` status `ready` deltaP `16.6805` edge `0.1731` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1875` n `101` status `ready` deltaP `18.7763` edge `0.1094` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.0222` n `98` status `ready` deltaP `22.775` edge `0.1098` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.9802` n `54` status `ready` deltaP `14.1772` edge `0.0051` maxDD `-0.1012`
- `market_context_high->fx_4h` score `0.6515` n `44` status `ready` deltaP `15.8813` edge `0.005` maxDD `-0.1876`
- `news_risk_high->metal_1h` score `0.6401` n `101` status `ready` deltaP `14.7477` edge `0.0152` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6228` n `101` status `ready` deltaP `17.2512` edge `0.0423` maxDD `-2.0994`
- `market_context_high->commodity_1h` score `0.4859` n `54` status `ready` deltaP `9.6141` edge `0.0257` maxDD `-0.1998`
- `news_risk_high->equity_24h` score `0.4546` n `98` status `ready` deltaP `16.3974` edge `0.0695` maxDD `-4.941`
- `news_risk_high->fx_4h` score `0.2151` n `101` status `ready` deltaP `8.7931` edge `0.0229` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.2113` n `101` status `ready` deltaP `5.2143` edge `0.0234` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.1004` n `98` status `ready` deltaP `14.9837` edge `-0.0026` maxDD `-2.4203`
- `market_context_high->metal_1h` score `0.0684` n `54` status `ready` deltaP `4.9568` edge `0.0081` maxDD `-0.2563`
- `news_risk_high->fx_1h` score `-0.2903` n `101` status `ready` deltaP `2.0943` edge `0.0062` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
