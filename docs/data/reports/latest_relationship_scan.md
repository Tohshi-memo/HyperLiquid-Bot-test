# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T05:22:31.248336+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2478`

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

- `market_context_high->unknown_24h` score `1349.1567` n `98` status `ready` deltaP `5.2083` edge `112.395` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.0215` n `98` status `ready` deltaP `39.594` edge `1.7325` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.9878` n `98` status `ready` deltaP `23.5722` edge `1.4639` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2329` n `98` status `ready` deltaP `15.3557` edge `0.2007` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.4941` n `107` status `ready` deltaP `2.1909` edge `0.0107` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.6712` n `98` status `ready` deltaP `10.8574` edge `0.0024` maxDD `-6.1238`
- `market_context_high->crypto_major_1h` score `-0.8666` n `107` status `ready` deltaP `2.0412` edge `0.062` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8829` n `107` status `ready` deltaP `-2.5183` edge `0.0023` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.9558` n `107` status `ready` deltaP `-0.8758` edge `0.0336` maxDD `-7.6911`
- `market_context_high->crypto_alt_4h` score `-1.1229` n `98` status `ready` deltaP `-1.8666` edge `0.1495` maxDD `-17.1476`
- `market_context_high->fx_1h` score `-1.328` n `107` status `ready` deltaP `-8.2755` edge `-0.0006` maxDD `-0.392`
- `market_context_high->crypto_major_4h` score `-1.3519` n `98` status `ready` deltaP `-4.2123` edge `0.213` maxDD `-22.3259`
- `market_context_high->commodity_1h` score `-2.7485` n `107` status `ready` deltaP `-13.4745` edge `-0.0314` maxDD `-3.9584`
- `market_context_high->index_4h` score `-2.765` n `98` status `ready` deltaP `-10.8263` edge `-0.0239` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.9029` n `107` status `ready` deltaP `0.3218` edge `-0.0263` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.6044` n `98` status `ready` deltaP `-25.1493` edge `-0.0118` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7336` n `98` status `ready` deltaP `-18.8138` edge `-0.0048` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5152` n `98` status `ready` deltaP `-25.1244` edge `-0.1127` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0599` n `98` status `ready` deltaP `-16.075` edge `-0.1056` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.8458` n `98` status `ready` deltaP `-16.7154` edge `-0.277` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
