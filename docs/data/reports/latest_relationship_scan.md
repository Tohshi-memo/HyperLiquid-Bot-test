# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T16:37:29.511732+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10024`

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

- `market_context_high->unknown_1h` score `87.5683` n `47` status `ready` deltaP `10.116` edge `7.237` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.5557` n `47` status `ready` deltaP `30.4226` edge `3.4661` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.1952` n `47` status `ready` deltaP `24.782` edge `2.3057` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.4103` n `47` status `ready` deltaP `29.0337` edge `1.8762` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8497` n `47` status `ready` deltaP `34.9364` edge `0.4342` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.352` n `93` status `ready` deltaP `1.3217` edge `1.5816` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.7039` n `47` status `ready` deltaP `31.9334` edge `0.1196` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.3168` n `93` status `ready` deltaP `-1.0473` edge `1.1335` maxDD `-49.7699`
- `market_context_high->index_4h` score `3.1054` n `47` status `ready` deltaP `35.3983` edge `0.0382` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.8057` n `115` status `ready` deltaP `13.3416` edge `0.1939` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6313` n `47` status `ready` deltaP `17.9067` edge `0.1417` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.424` n `115` status `ready` deltaP `16.307` edge `0.1368` maxDD `-1.8141`
- `news_risk_high->crypto_major_4h` score `1.8882` n `111` status `ready` deltaP `15.4211` edge `0.2677` maxDD `-13.719`
- `news_risk_high->fx_4h` score `1.5682` n `111` status `ready` deltaP `23.0966` edge `0.0403` maxDD `-0.421`
- `news_risk_high->crypto_alt_4h` score `1.5099` n `111` status `ready` deltaP `7.8678` edge `0.3185` maxDD `-15.9436`
- `news_risk_high->metal_24h` score `1.174` n `93` status `ready` deltaP `25.2072` edge `0.1273` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `1.1425` n `93` status `ready` deltaP `28.1978` edge `0.1216` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.0266` n `47` status `ready` deltaP `15.3586` edge `0.011` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9415` n `47` status `ready` deltaP `11.3167` edge `0.0433` maxDD `-1.5564`
- `news_risk_high->commodity_24h` score `0.8004` n `93` status `ready` deltaP `14.8185` edge `0.0858` maxDD `-2.431`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
