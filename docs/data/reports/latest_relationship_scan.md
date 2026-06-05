# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T10:52:22.151473+00:00`
- Price records: `672`
- Market context records: `2962`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.201` n `120` status `ready` deltaP `12.0139` edge `1.745` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.87` n `120` status `ready` deltaP `16.9097` edge `0.6729` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.8171` n `120` status `ready` deltaP `17.5347` edge `0.7349` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `7.3001` n `120` status `ready` deltaP `28.1597` edge `0.5257` maxDD `-3.4069`
- `market_context_high->equity_4h` score `3.4618` n `121` status `ready` deltaP `17.3441` edge `0.2118` maxDD `-0.7819`
- `market_context_high->index_24h` score `3.2626` n `120` status `ready` deltaP `13.1944` edge `0.282` maxDD `-2.5127`
- `market_context_high->crypto_alt_4h` score `2.9514` n `121` status `ready` deltaP `24.0425` edge `0.5418` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.7977` n `121` status `ready` deltaP `14.3104` edge `0.0857` maxDD `-1.9733`
- `market_context_high->equity_1h` score `0.5602` n `121` status `ready` deltaP `4.1149` edge `0.0562` maxDD `-1.2892`
- `market_context_high->unknown_4h` score `0.424` n `121` status `ready` deltaP `5.5004` edge `0.104` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0051` n `121` status `ready` deltaP `4.5516` edge `0.0184` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.1941` n `121` status `ready` deltaP `1.5515` edge `0.0042` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.2872` n `121` status `ready` deltaP `6.7254` edge `0.0989` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.2942` n `121` status `ready` deltaP `6.4136` edge `0.0773` maxDD `-9.622`
- `market_context_high->crypto_major_4h` score `-0.4397` n `121` status `ready` deltaP `12.8653` edge `0.3704` maxDD `-33.6701`
- `market_context_high->commodity_1h` score `-0.5596` n `121` status `ready` deltaP `-1.3052` edge `-0.0005` maxDD `-3.3365`
- `market_context_high->commodity_4h` score `-0.7984` n `121` status `ready` deltaP `5.5811` edge `0.0394` maxDD `-8.9839`
- `market_context_high->metal_1h` score `-0.8025` n `121` status `ready` deltaP `-1.7012` edge `-0.0028` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.8371` n `121` status `ready` deltaP `1.4735` edge `-0.0065` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-0.9519` n `121` status `ready` deltaP `-1.5685` edge `0.009` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
