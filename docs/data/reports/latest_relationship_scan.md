# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T11:37:20.881156+00:00`
- Price records: `672`
- Market context records: `2557`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9198`

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

- `market_context_high->crypto_alt_4h` score `5.7247` n `149` status `ready` deltaP `25.0133` edge `0.5782` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.2105` n `118` status `ready` deltaP `19.1296` edge `0.3395` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.8673` n `118` status `ready` deltaP `12.1704` edge `0.5898` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.9617` n `149` status `ready` deltaP `17.6011` edge `0.3938` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.7127` n `149` status `ready` deltaP `10.0047` edge `0.181` maxDD `-3.7312`
- `market_context_high->equity_24h` score `1.1928` n `118` status `ready` deltaP `18.9972` edge `0.0311` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.1893` n `149` status `ready` deltaP `9.7265` edge `0.153` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.7063` n `118` status `ready` deltaP `6.7855` edge `0.1117` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.6634` n `149` status `ready` deltaP `8.0848` edge `0.1208` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1542` n `118` status `ready` deltaP `-0.9592` edge `0.6666` maxDD `-39.2351`
- `market_context_high->index_4h` score `0.027` n `149` status `ready` deltaP `6.9896` edge `0.0398` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1897` n `149` status `ready` deltaP `3.4492` edge `0.0106` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2916` n `149` status `ready` deltaP `2.4163` edge `0.0286` maxDD `-2.8543`
- `market_context_high->metal_1h` score `-0.4472` n `149` status `ready` deltaP `1.1614` edge `0.0097` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.5285` n `149` status `ready` deltaP `0.7847` edge `0.0042` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.541` n `149` status `ready` deltaP `4.2077` edge `0.0147` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.7546` n `118` status `ready` deltaP `1.0829` edge `0.0037` maxDD `-1.946`
- `market_context_high->equity_1h` score `-0.7866` n `149` status `ready` deltaP `-0.1487` edge `0.0193` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8624` n `149` status `ready` deltaP `3.6872` edge `0.0423` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.8695` n `149` status `ready` deltaP `0.1514` edge `0.0125` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
