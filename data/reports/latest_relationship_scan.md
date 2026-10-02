# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T17:52:28.144440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4888`

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

- `market_context_high->unknown_1h` score `359.0686` n `50` status `ready` deltaP `11.024` edge `29.8538` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.6215` n `50` status `ready` deltaP `10.5183` edge `24.315` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5761` n `73` status `ready` deltaP `39.795` edge `1.0536` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.2507` n `50` status `ready` deltaP `16.5347` edge `0.831` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.0007` n `73` status `ready` deltaP `32.4058` edge `0.5825` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9869` n `50` status `ready` deltaP `32.0` edge `0.6772` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.1015` n `50` status `ready` deltaP `17.3902` edge `0.5462` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.0764` n `50` status `ready` deltaP `15.4268` edge `0.4491` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.8974` n `116` status `ready` deltaP `21.2889` edge `0.4006` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.0658` n `50` status `ready` deltaP `14.3533` edge `0.2261` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.0132` n `50` status `ready` deltaP `14.1497` edge `0.2018` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7653` n `50` status `ready` deltaP `30.8598` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4459` n `116` status `ready` deltaP `22.0984` edge `0.1261` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.677` n `50` status `ready` deltaP `8.625` edge `0.3437` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5063` n `73` status `ready` deltaP `6.1644` edge `0.4674` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3348` n `73` status `ready` deltaP `13.009` edge `0.2118` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.1854` n `116` status `ready` deltaP `14.0454` edge `0.2893` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.9184` n `116` status `ready` deltaP `5.2499` edge `0.0976` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.7594` n `50` status `ready` deltaP `16.6875` edge `0.0879` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
