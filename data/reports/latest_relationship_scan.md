# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T04:07:27.417770+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.5296` n `107` status `ready` deltaP `22.6593` edge `0.5382` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.5296` n `107` status `ready` deltaP `22.6593` edge `0.5382` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.0762` n `151` status `ready` deltaP `18.9519` edge `0.4495` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1525` n `107` status `ready` deltaP `5.3179` edge `0.2016` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1525` n `107` status `ready` deltaP `5.3179` edge `0.2016` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0217` n `151` status `ready` deltaP `4.6804` edge `0.2003` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.4914` n `107` status `ready` deltaP `13.4671` edge `0.1333` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.4914` n `107` status `ready` deltaP `13.4671` edge `0.1333` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.2465` n `61` status `ready` deltaP `2.4222` edge `0.1224` maxDD `-1.1072`
- `risk_on_high->crypto_alt_24h` score `1.1342` n `107` status `ready` deltaP `14.486` edge `0.7392` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.1342` n `107` status `ready` deltaP `14.486` edge `0.7392` maxDD `-42.8959`
- `market_context_high->commodity_24h` score `0.8953` n `151` status `ready` deltaP `12.8357` edge `0.1086` maxDD `-1.2314`
- `market_context_high->commodity_1h` score `0.1244` n `151` status `ready` deltaP `8.872` edge `0.0162` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1232` n `61` status `ready` deltaP `10.3484` edge `0.0006` maxDD `-0.7461`
- `news_risk_high->commodity_4h` score `0.0876` n `61` status `ready` deltaP `5.053` edge `0.0192` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `0.026` n `151` status `ready` deltaP `6.3015` edge `0.0499` maxDD `-2.1795`
- `risk_on_high->commodity_1h` score `0.0076` n `107` status `ready` deltaP `5.7712` edge `0.0147` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0076` n `107` status `ready` deltaP `5.7712` edge `0.0147` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0283` n `107` status `ready` deltaP `6.1475` edge `-0.0001` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0283` n `107` status `ready` deltaP `6.1475` edge `-0.0001` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
