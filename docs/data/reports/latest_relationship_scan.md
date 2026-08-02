# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T21:22:29.845388+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5918`

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

- `news_risk_high->unknown_24h` score `4906.5642` n `62` status `ready` deltaP `23.9303` edge `408.7629` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.0925` n `40` status `ready` deltaP `54.2361` edge `1.0192` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0874` n `40` status `ready` deltaP `51.3194` edge `0.5946` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.3946` n `62` status `ready` deltaP `14.757` edge `0.3442` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.4281` n `62` status `ready` deltaP `13.69` edge `0.0658` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0265` n `40` status `ready` deltaP `13.4451` edge `0.1266` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7498` n `40` status `ready` deltaP `8.3537` edge `0.131` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.648` n `40` status `ready` deltaP `20.4573` edge `0.0263` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.5487` n `41` status `ready` deltaP `10.4827` edge `0.0379` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4887` n `41` status `ready` deltaP `14.4625` edge `0.004` maxDD `-0.6874`
- `news_risk_high->equity_1h` score `0.3773` n `62` status `ready` deltaP `7.0987` edge `0.0664` maxDD `-2.916`
- `news_risk_high->fx_4h` score `0.0405` n `62` status `ready` deltaP `11.3444` edge `0.0235` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.008` n `62` status `ready` deltaP `4.2737` edge `0.0048` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0766` n `62` status `ready` deltaP `2.4435` edge `0.0062` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.115` n `62` status `ready` deltaP `4.8387` edge `0.0212` maxDD `-3.1233`
- `news_risk_high->metal_4h` score `-0.1606` n `62` status `ready` deltaP `2.5521` edge `0.01` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.3226` n `62` status `ready` deltaP `-0.3332` edge `0.0012` maxDD `-0.5599`
- `market_context_high->crypto_alt_1h` score `-0.3385` n `41` status `ready` deltaP `1.2195` edge `0.0112` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.4221` n `62` status `ready` deltaP `5.1719` edge `-0.0196` maxDD `-2.1859`
- `news_risk_high->crypto_major_1h` score `-0.4573` n `62` status `ready` deltaP `0.5988` edge `0.0094` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
