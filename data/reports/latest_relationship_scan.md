# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T17:07:32.039164+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `news_risk_high->equity_4h` score `7.3519` n `30` status `ready` deltaP `40.8537` edge `0.3403` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.6475` n `32` status `ready` deltaP `18.2292` edge `0.3335` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.6475` n `32` status `ready` deltaP `18.2292` edge `0.3335` maxDD `-6.2481`
- `news_risk_high->index_4h` score `2.5718` n `30` status `ready` deltaP `27.6931` edge `0.0426` maxDD `-0.0323`
- `risk_on_high->commodity_4h` score `2.2485` n `32` status `ready` deltaP `15.1677` edge `0.1045` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2485` n `32` status `ready` deltaP `15.1677` edge `0.1045` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `1.8013` n `32` status `ready` deltaP `16.6667` edge `0.039` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.8013` n `32` status `ready` deltaP `16.6667` edge `0.039` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7681` n `36` status `ready` deltaP `8.8823` edge `0.12` maxDD `-0.5496`
- `risk_on_high->fx_24h` score `1.7121` n `32` status `ready` deltaP `19.0972` edge `0.0338` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.7121` n `32` status `ready` deltaP `19.0972` edge `0.0338` maxDD `-0.1418`
- `risk_on_high->equity_24h` score `1.3919` n `32` status `ready` deltaP `4.1667` edge `0.3286` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `1.3919` n `32` status `ready` deltaP `4.1667` edge `0.3286` maxDD `-11.2348`
- `risk_on_high->index_24h` score `1.1687` n `32` status `ready` deltaP `11.2847` edge `0.0526` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.1687` n `32` status `ready` deltaP `11.2847` edge `0.0526` maxDD `-0.4355`
- `risk_on_high->commodity_1h` score `1.158` n `32` status `ready` deltaP `12.6123` edge `0.0357` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.158` n `32` status `ready` deltaP `12.6123` edge `0.0357` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9511` n `32` status `ready` deltaP `10.8994` edge `0.0207` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9511` n `32` status `ready` deltaP `10.8994` edge `0.0207` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.7774` n `172` status `ready` deltaP `10.8799` edge `0.0561` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
