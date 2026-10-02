# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T00:07:26.900530+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6574`

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

- `market_context_high->unknown_1h` score `338.5824` n `50` status `ready` deltaP `9.5269` edge `28.1566` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.1693` n `50` status `ready` deltaP `8.2317` edge `23.8759` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.5803` n `86` status `ready` deltaP `37.4313` edge `1.4031` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.8134` n `50` status `ready` deltaP `35.6458` edge `0.8051` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2789` n `50` status `ready` deltaP `19.0671` edge `0.5498` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.6546` n `50` status `ready` deltaP `13.7569` edge `0.6338` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0152` n `50` status `ready` deltaP `16.4939` edge `0.4373` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `3.69` n `86` status `ready` deltaP `16.4365` edge `0.5133` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.6765` n `50` status `ready` deltaP `19.0417` edge `0.5306` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `3.0563` n `50` status `ready` deltaP `14.8982` edge `0.2004` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0033` n `50` status `ready` deltaP `14.0539` edge `0.2229` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9798` n `50` status `ready` deltaP `33.4512` edge `0.0388` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.8633` n `99` status `ready` deltaP `25.1863` edge `0.1403` maxDD `-2.9013`
- `news_risk_high->crypto_alt_4h` score `2.2589` n `99` status `ready` deltaP `9.1202` edge `0.2618` maxDD `-6.4152`
- `news_risk_high->equity_24h` score `2.2587` n `86` status `ready` deltaP `14.9952` edge `0.4245` maxDD `-9.4579`
- `news_risk_high->commodity_24h` score `1.7563` n `86` status `ready` deltaP `27.5799` edge `0.1537` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.6772` n `86` status `ready` deltaP `18.3341` edge `0.2202` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.5895` n `86` status `ready` deltaP `19.2103` edge `0.0522` maxDD `-0.4916`
- `market_context_high->fx_1h` score `1.5023` n `50` status `ready` deltaP `20.9401` edge `0.012` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9198` n `50` status `ready` deltaP `14.7917` edge `0.0764` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
