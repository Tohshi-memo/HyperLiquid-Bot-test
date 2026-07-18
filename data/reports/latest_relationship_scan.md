# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T05:52:27.874503+00:00`
- Price records: `672`
- Market context records: `7108`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->fx_4h` score `0.376` n `149` status `ready` deltaP `15.6449` edge `0.0139` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1107` n `149` status `ready` deltaP `4.2177` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.166` n `149` status `ready` deltaP `-0.3255` edge `0.0442` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3445` n `149` status `ready` deltaP `1.6005` edge `0.0316` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5464` n `149` status `ready` deltaP `4.063` edge `0.0381` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.5916` n `149` status `ready` deltaP `-1.064` edge `-0.0068` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8184` n `149` status `ready` deltaP `-3.629` edge `-0.0191` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3798` n `149` status `ready` deltaP `-4.5701` edge `-0.0429` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.5401` n `149` status `ready` deltaP `-6.4434` edge `0.0057` maxDD `-4.4825`
- `market_context_high->metal_1h` score `-1.5563` n `149` status `ready` deltaP `-7.0992` edge `-0.0058` maxDD `-2.1249`
- `market_context_high->equity_1h` score `-2.1037` n `149` status `ready` deltaP `2.7408` edge `-0.0457` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.6029` n `149` status `ready` deltaP `-2.4442` edge `-0.0475` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-3.0247` n `149` status `ready` deltaP `4.2396` edge `0.0124` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.0411` n `149` status `ready` deltaP `0.6384` edge `-0.0156` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.5117` n `149` status `ready` deltaP `-8.6945` edge `-0.1038` maxDD `-4.4704`
- `market_context_high->metal_4h` score `-4.3556` n `149` status `ready` deltaP `-8.156` edge `-0.0116` maxDD `-5.426`
- `market_context_high->fx_24h` score `-4.5456` n `149` status `ready` deltaP `-11.1437` edge `-0.0218` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-8.8351` n `149` status `ready` deltaP `-2.2006` edge `-0.231` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-9.231` n `149` status `ready` deltaP `-26.531` edge `-0.0777` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.7875` n `149` status `ready` deltaP `-26.1477` edge `-0.1517` maxDD `-42.502`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
