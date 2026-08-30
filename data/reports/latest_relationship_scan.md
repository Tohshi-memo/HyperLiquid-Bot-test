# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T06:52:21.866908+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `9.0166` n `59` status `ready` deltaP `22.6849` edge `0.643` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.0166` n `59` status `ready` deltaP `22.6849` edge `0.643` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.1971` n `158` status `ready` deltaP `19.3809` edge `0.3509` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6214` n `94` status `ready` deltaP `32.1956` edge `0.2724` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.059` n `59` status `ready` deltaP `22.7651` edge `0.2148` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.059` n `59` status `ready` deltaP `22.7651` edge `0.2148` maxDD `-0.5985`
- `risk_on_high->unknown_1h` score `3.7549` n `59` status `ready` deltaP `9.4616` edge `0.2701` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.7549` n `59` status `ready` deltaP `9.4616` edge `0.2701` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.2296` n `59` status `ready` deltaP `29.4285` edge `0.0916` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.2296` n `59` status `ready` deltaP `29.4285` edge `0.0916` maxDD `-0.1594`
- `risk_on_high->index_4h` score `2.6446` n `59` status `ready` deltaP `32.1905` edge `0.0143` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.6446` n `59` status `ready` deltaP `32.1905` edge `0.0143` maxDD `-0.0147`
- `market_context_high->unknown_1h` score `2.5729` n `158` status `ready` deltaP `11.4891` edge `0.1787` maxDD `-0.9372`
- `risk_on_high->metal_4h` score `1.7796` n `59` status `ready` deltaP `22.362` edge `0.029` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.7796` n `59` status `ready` deltaP `22.362` edge `0.029` maxDD `-0.0488`
- `risk_on_high->crypto_alt_4h` score `1.7321` n `59` status `ready` deltaP `11.7973` edge `0.1917` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `1.7321` n `59` status `ready` deltaP `11.7973` edge `0.1917` maxDD `-1.5298`
- `risk_on_high->metal_1h` score `1.7011` n `59` status `ready` deltaP `22.5287` edge `0.0086` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7011` n `59` status `ready` deltaP `22.5287` edge `0.0086` maxDD `-0.0291`
- `risk_on_high->equity_1h` score `1.2087` n `59` status `ready` deltaP `15.9952` edge `0.0175` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
