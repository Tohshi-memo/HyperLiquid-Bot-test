# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T01:22:27.827423+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.3343` n `50` status `ready` deltaP `10.4251` edge `30.2966` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.7065` n `50` status `ready` deltaP `10.3659` edge `24.3231` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.1018` n `70` status `ready` deltaP `34.1915` edge `1.0878` maxDD `-2.2476`
- `market_context_high->crypto_alt_24h` score `10.825` n `50` status `ready` deltaP `21.0486` edge `0.9321` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.7334` n `70` status `ready` deltaP `33.7351` edge `0.6347` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9381` n `50` status `ready` deltaP `31.4792` edge `0.6766` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.5681` n `50` status `ready` deltaP `18.1524` edge `0.58` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `7.4505` n `104` status `ready` deltaP `30.1477` edge `0.5543` maxDD `-6.4195`
- `news_risk_high->crypto_major_24h` score `6.0212` n `70` status `ready` deltaP `10.9078` edge `0.5855` maxDD `-7.1825`
- `market_context_high->crypto_alt_4h` score `5.9789` n `50` status `ready` deltaP `16.4939` edge `0.5172` maxDD `-7.6465`
- `news_risk_high->crypto_major_4h` score `4.9991` n `104` status `ready` deltaP `22.2678` edge `0.3955` maxDD `-6.1885`
- `market_context_high->crypto_alt_1h` score `3.2278` n `50` status `ready` deltaP `14.8024` edge `0.2366` maxDD `-3.6376`
- `news_risk_high->equity_4h` score `3.0866` n `104` status `ready` deltaP `25.5277` edge `0.1483` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0085` n `50` status `ready` deltaP `13.4012` edge `0.2064` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8409` n `50` status `ready` deltaP `31.7744` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `1.7668` n `70` status `ready` deltaP `10.8879` edge `0.2006` maxDD `-2.0759`
- `news_risk_high->index_24h` score `1.7412` n `70` status `ready` deltaP `19.2361` edge `0.0619` maxDD `-0.2696`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.2561` n `50` status `ready` deltaP `6.0208` edge `0.3071` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.1881` n `104` status `ready` deltaP `4.5716` edge `0.1246` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
