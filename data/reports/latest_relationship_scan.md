# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T05:07:28.780855+00:00`
- Price records: `672`
- Market context records: `5320`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9648`

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

- `market_context_high->unknown_24h` score `19.0209` n `153` status `ready` deltaP `22.8247` edge `1.4419` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.063` n `153` status `ready` deltaP `24.8673` edge `0.8378` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.116` n `153` status `ready` deltaP `19.0972` edge `0.8619` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.0739` n `194` status `ready` deltaP `12.0364` edge `0.34` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.0463` n `194` status `ready` deltaP `13.3361` edge `0.3942` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.2058` n `194` status `ready` deltaP `11.9216` edge `0.2682` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5302` n `194` status `ready` deltaP `8.462` edge `0.0843` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.5157` n `153` status `ready` deltaP `13.3068` edge `0.0438` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.4896` n `153` status `ready` deltaP `21.8648` edge `0.0805` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.0482` n `194` status `ready` deltaP `2.2455` edge `0.0852` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.037` n `194` status `ready` deltaP `6.218` edge `0.012` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.0121` n `194` status `ready` deltaP `4.491` edge `0.0936` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.2976` n `194` status `ready` deltaP `2.8443` edge `0.0104` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3454` n `194` status `ready` deltaP `0.7146` edge `-0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4236` n `194` status `ready` deltaP `5.4595` edge `0.0252` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6114` n `194` status `ready` deltaP `3.0503` edge `0.0042` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-0.9783` n `194` status `ready` deltaP `9.7372` edge `-0.0282` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4084` n `194` status `ready` deltaP `-2.8767` edge `-0.0064` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.2723` n `194` status `ready` deltaP `-5.3951` edge `-0.0029` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2375` n `153` status `ready` deltaP `12.8268` edge `0.3404` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
