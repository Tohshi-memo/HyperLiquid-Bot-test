# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T14:37:35.808967+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11756`

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

- `market_context_high->metal_24h` score `1.3395` n `110` status `ready` deltaP `4.7625` edge `0.1583` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.7759` n `121` status `ready` deltaP `10.9294` edge `0.0334` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.7304` n `112` status `ready` deltaP `11.3241` edge `0.07` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4438` n `110` status `ready` deltaP `19.6175` edge `0.0452` maxDD `-4.1933`
- `market_context_high->fx_1h` score `0.1531` n `121` status `ready` deltaP `9.2047` edge `-0.002` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.2456` n `112` status `ready` deltaP `7.8615` edge `0.0021` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4369` n `121` status `ready` deltaP `-1.5205` edge `-0.0066` maxDD `-1.1422`
- `market_context_high->crypto_alt_1h` score `-0.817` n `121` status `ready` deltaP `-4.5331` edge `-0.0116` maxDD `-2.3669`
- `market_context_high->index_24h` score `-0.8346` n `110` status `ready` deltaP `0.4189` edge `0.0873` maxDD `-5.7715`
- `market_context_high->metal_4h` score `-0.957` n `112` status `ready` deltaP `0.4791` edge `-0.0028` maxDD `-2.0783`
- `market_context_high->index_1h` score `-1.1099` n `121` status `ready` deltaP `-3.9281` edge `-0.0129` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.494` n `121` status `ready` deltaP `2.2406` edge `-0.05` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.7623` n `112` status `ready` deltaP `2.1341` edge `-0.0221` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.2885` n `112` status `ready` deltaP `-5.7274` edge `-0.0301` maxDD `-4.4604`
- `market_context_high->crypto_major_1h` score `-2.4518` n `121` status `ready` deltaP `-5.3719` edge `-0.0388` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-3.72` n `110` status `ready` deltaP `-10.0789` edge `-0.0985` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.7871` n `112` status `ready` deltaP `-6.5331` edge `-0.1766` maxDD `-25.1525`
- `market_context_high->crypto_major_24h` score `-6.5446` n `110` status `ready` deltaP `-5.8704` edge `-0.2987` maxDD `-29.7639`
- `market_context_high->unknown_1h` score `-8.2309` n `121` status `ready` deltaP `-0.1794` edge `-0.64` maxDD `-1.2437`
- `market_context_high->equity_4h` score `-9.2905` n `112` status `ready` deltaP `-0.4356` edge `-0.2615` maxDD `-34.1179`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
