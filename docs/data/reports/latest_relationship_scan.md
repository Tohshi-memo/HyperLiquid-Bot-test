# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T10:52:25.318226+00:00`
- Price records: `672`
- Market context records: `2859`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->crypto_alt_24h` score `4.554` n `142` status `ready` deltaP `4.0909` edge `0.7439` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.4695` n `142` status `ready` deltaP `6.0739` edge `0.2951` maxDD `-1.7175`
- `market_context_high->equity_24h` score `1.8548` n `142` status `ready` deltaP `5.4357` edge `0.3187` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `1.3667` n `142` status `ready` deltaP `14.3364` edge `0.3277` maxDD `-12.4171`
- `market_context_high->index_24h` score `1.0946` n `142` status `ready` deltaP `7.634` edge `0.1384` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.896` n `142` status `ready` deltaP `5.8807` edge `0.1408` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.4242` n `142` status `ready` deltaP `13.9106` edge `0.0458` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1378` n `142` status `ready` deltaP `4.6302` edge `0.0537` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0727` n `142` status `ready` deltaP `4.198` edge `0.0121` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.5969` n `142` status `ready` deltaP `5.0962` edge `0.0655` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6171` n `142` status `ready` deltaP `-0.5819` edge `0.0001` maxDD `-4.3601`
- `market_context_high->equity_4h` score `-0.6736` n `142` status `ready` deltaP `3.3343` edge `0.0596` maxDD `-5.7037`
- `market_context_high->fx_1h` score `-0.6832` n `142` status `ready` deltaP `-2.1843` edge `0.002` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7697` n `142` status `ready` deltaP `-0.6157` edge `-0.01` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.779` n `142` status `ready` deltaP `4.5248` edge `0.0569` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.8248` n `142` status `ready` deltaP `-2.1506` edge `0.0289` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-0.8767` n `142` status `ready` deltaP `13.7281` edge `0.2695` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2381` n `142` status `ready` deltaP `-4.5152` edge `0.0048` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.269` n `142` status `ready` deltaP `2.4476` edge `0.013` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3951` n `142` status `ready` deltaP `-1.8852` edge `-0.0165` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
