# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T08:37:14.942375+00:00`
- Price records: `672`
- Market context records: `995`
- Flow alert records: `4772`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `12.8654` n `211` status `ready` deltaP `31.5408` edge `0.9207` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1378` n `211` status `ready` deltaP `10.7874` edge `0.3963` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3444` n `211` status `ready` deltaP `2.132` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5236` n `211` status `ready` deltaP `2.6322` edge `0.0196` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6275` n `211` status `ready` deltaP `1.2557` edge `0.0162` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.7027` n `211` status `ready` deltaP `3.0678` edge `0.1205` maxDD `-5.9609`
- `market_context_high->index_1h` score `-0.744` n `211` status `ready` deltaP `2.7527` edge `0.005` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7516` n `211` status `ready` deltaP `0.3872` edge `0.0007` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-1.2124` n `211` status `ready` deltaP `4.5366` edge `0.1292` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2277` n `211` status `ready` deltaP `4.6514` edge `-0.0161` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.5128` n `211` status `ready` deltaP `1.8054` edge `0.0771` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7504` n `211` status `ready` deltaP `-1.7093` edge `0.0178` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8897` n `211` status `ready` deltaP `-1.1614` edge `-0.0386` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0675` n `211` status `ready` deltaP `-0.7378` edge `-0.0234` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.956` n `211` status `ready` deltaP `6.9097` edge `0.0782` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.2803` n `211` status `ready` deltaP `-1.964` edge `0.0565` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3432` n `211` status `ready` deltaP `-2.0381` edge `0.0128` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5997` n `211` status `ready` deltaP `-1.6915` edge `-0.0223` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.6051` n `211` status `ready` deltaP `-4.8305` edge `-0.1625` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.2329` n `211` status `ready` deltaP `2.6821` edge `0.3914` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
