# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T16:37:31.015757+00:00`
- Price records: `672`
- Market context records: `7791`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `7.8018` n `132` status `ready` deltaP `28.5507` edge `0.594` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.5096` n `133` status `ready` deltaP `14.231` edge `0.24` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.1469` n `133` status `ready` deltaP `14.5764` edge `0.1702` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.1029` n `133` status `ready` deltaP `3.8834` edge `0.3068` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.0334` n `133` status `ready` deltaP `13.0832` edge `0.043` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.9435` n `133` status `ready` deltaP `9.0363` edge `0.1301` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8093` n `132` status `ready` deltaP `25.2187` edge `0.0444` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6387` n `133` status `ready` deltaP `7.6721` edge `0.088` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.348` n `133` status `ready` deltaP `8.4173` edge `0.0159` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.3339` n `133` status `ready` deltaP `7.4821` edge `0.0373` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.207` n `133` status `ready` deltaP `4.5001` edge `0.0305` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0192` n `133` status `ready` deltaP `5.2801` edge `0.0123` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1266` n `133` status `ready` deltaP `12.0129` edge `0.0495` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3537` n `133` status `ready` deltaP `1.346` edge `0.0003` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.3953` n `132` status `ready` deltaP `11.7312` edge `0.0472` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9192` n `133` status `ready` deltaP `0.7407` edge `0.0188` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.339` n `133` status `ready` deltaP `-1.6541` edge `0.0022` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5475` n `133` status `ready` deltaP `0.2998` edge `0.0745` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.6705` n `132` status `ready` deltaP `-9.6614` edge `0.0605` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.3473` n `133` status `ready` deltaP `14.7431` edge `0.1303` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
