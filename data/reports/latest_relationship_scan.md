# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T15:07:32.015083+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9286`

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

- `market_context_high->equity_24h` score `6.7845` n `34` status `ready` deltaP `11.0907` edge `0.7319` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.9512` n `34` status `ready` deltaP `4.1463` edge `0.1937` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.9294` n `34` status `ready` deltaP `10.3656` edge `0.0963` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.6385` n `34` status `ready` deltaP `10.1613` edge `-0.0039` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3305` n `88` status `ready` deltaP `3.9467` edge `0.0138` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5156` n `88` status `ready` deltaP `0.1429` edge `0.0012` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.539` n `88` status `ready` deltaP `3.5477` edge `0.005` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.787` n `88` status `ready` deltaP `-1.4689` edge `0.0195` maxDD `-4.182`
- `market_context_high->metal_4h` score `-0.9229` n `88` status `ready` deltaP `0.4712` edge `0.0169` maxDD `-4.0688`
- `market_context_high->index_1h` score `-0.9535` n `88` status `ready` deltaP `-6.9066` edge `0.0069` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2953` n `88` status `ready` deltaP `-13.7588` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.4592` n `88` status `ready` deltaP `-6.9066` edge `0.0436` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.882` n `88` status `ready` deltaP `0.9322` edge `-0.0496` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-2.0456` n `34` status `ready` deltaP `-3.4722` edge `-0.1838` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1012` n `88` status `ready` deltaP `-6.4579` edge `-0.0082` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1222` n `88` status `ready` deltaP `-4.8108` edge `-0.1059` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.5122` n `88` status `ready` deltaP `0.1524` edge `-0.0792` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-6.3537` n `34` status `ready` deltaP `-6.5257` edge `-0.0229` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.7148` n `88` status `ready` deltaP `2.3975` edge `-0.2304` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.8223` n `34` status `ready` deltaP `-21.0785` edge `-0.2519` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
