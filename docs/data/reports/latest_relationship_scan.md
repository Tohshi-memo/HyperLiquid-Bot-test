# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T10:22:33.022060+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11130`

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

- `market_context_high->unknown_4h` score `43.5409` n `88` status `ready` deltaP `7.6774` edge `3.622` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.0378` n `88` status `ready` deltaP `33.0412` edge `2.94` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4872` n `88` status `ready` deltaP `25.8783` edge `0.331` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.465` n `88` status `ready` deltaP `22.6012` edge `0.9312` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.0375` n `88` status `ready` deltaP `16.7303` edge `-0.0531` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3637` n `88` status `ready` deltaP `2.3884` edge `0.0057` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4135` n `88` status `ready` deltaP `3.1042` edge `0.0369` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.4719` n `88` status `ready` deltaP `2.7491` edge `0.01` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.7758` n `88` status `ready` deltaP `1.1086` edge `-0.0091` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0594` n `88` status `ready` deltaP `-8.5533` edge `0.0043` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2352` n `88` status `ready` deltaP `-2.73` edge `-0.0018` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3086` n `88` status `ready` deltaP `-14.0582` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8006` n `88` status `ready` deltaP `-9.3018` edge `0.0158` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9553` n `88` status `ready` deltaP `0.6328` edge `-0.057` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0173` n `88` status `ready` deltaP `-4.9335` edge `-0.0076` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.5328` n `88` status `ready` deltaP `-3.8995` edge `-0.0251` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1316` n `88` status `ready` deltaP `-4.6611` edge `-0.1081` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.2467` n `88` status `ready` deltaP `-2.1341` edge `-0.2085` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.007` n `88` status `ready` deltaP `1.9402` edge `-0.2517` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2284` n `88` status `ready` deltaP `-23.4698` edge `-0.0602` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
