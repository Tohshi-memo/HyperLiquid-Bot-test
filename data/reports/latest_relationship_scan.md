# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T03:22:30.636191+00:00`
- Price records: `672`
- Market context records: `5313`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `19.3103` n `153` status `ready` deltaP `23.172` edge `1.4637` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.3868` n `153` status `ready` deltaP `25.7353` edge `0.859` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.1743` n `153` status `ready` deltaP `19.2708` edge `0.8656` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.2555` n `194` status `ready` deltaP `12.3412` edge `0.3531` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.1989` n `194` status `ready` deltaP `13.4885` edge `0.4059` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0282` n `194` status `ready` deltaP `11.007` edge `0.2595` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5289` n `153` status `ready` deltaP `13.3068` edge `0.0449` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.5122` n `194` status `ready` deltaP `8.6117` edge `0.0818` maxDD `-5.0555`
- `market_context_high->index_24h` score `0.3813` n `153` status `ready` deltaP `20.9967` edge `0.0724` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.1141` n `194` status `ready` deltaP `2.5449` edge `0.0887` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0394` n `194` status `ready` deltaP `6.3677` edge `0.0112` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0178` n `194` status `ready` deltaP `4.7904` edge `0.0941` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.335` n `194` status `ready` deltaP `2.3952` edge `0.0086` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3874` n `194` status `ready` deltaP `-0.0339` edge `-0.0005` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.5048` n `194` status `ready` deltaP `4.3924` edge `0.0219` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6296` n `194` status `ready` deltaP `2.7454` edge `0.0039` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-0.6391` n `194` status `ready` deltaP `10.347` edge `-0.004` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4359` n `194` status `ready` deltaP `-3.1761` edge `-0.0067` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3645` n `194` status `ready` deltaP `-6.4622` edge `-0.0076` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.0622` n `153` status `ready` deltaP `13.3476` edge `0.3594` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
