# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T15:22:35.023525+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10036`

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

- `market_context_high->unknown_1h` score `87.8143` n `47` status `ready` deltaP `10.116` edge `7.2575` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.0241` n `47` status `ready` deltaP `30.4226` edge `3.4218` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.8628` n `47` status `ready` deltaP `24.782` edge `2.278` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.1741` n `47` status `ready` deltaP `28.1656` edge `1.8623` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8437` n `47` status `ready` deltaP `34.9364` edge `0.4337` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.5905` n `95` status `ready` deltaP `2.0688` edge `1.6072` maxDD `-63.6743`
- `news_risk_high->crypto_alt_24h` score `3.6875` n `95` status `ready` deltaP `-0.4587` edge `1.1771` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.6056` n `47` status `ready` deltaP `31.0653` edge `0.1172` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.109` n `47` status `ready` deltaP `35.3983` edge `0.0385` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.8477` n `116` status `ready` deltaP `13.4318` edge `0.1968` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6661` n `47` status `ready` deltaP `17.9067` edge `0.1446` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.3868` n `116` status `ready` deltaP `15.9767` edge `0.1359` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6498` n `109` status `ready` deltaP `23.9818` edge `0.0412` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1942` n `95` status `ready` deltaP `28.9674` edge `0.1231` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `1.1548` n `95` status `ready` deltaP `25.0183` edge `0.1261` maxDD `-7.2536`
- `market_context_high->index_1h` score `0.993` n `47` status `ready` deltaP `14.9095` edge `0.0112` maxDD `-0.2275`
- `news_risk_high->commodity_24h` score `0.967` n `95` status `ready` deltaP `15.5354` edge `0.0949` maxDD `-2.431`
- `market_context_high->equity_1h` score `0.9403` n `47` status `ready` deltaP `11.167` edge `0.0442` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.7646` n `109` status `ready` deltaP `14.4118` edge `0.2151` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.4803` n `116` status `ready` deltaP `15.2488` edge `0.0176` maxDD `-0.6142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
