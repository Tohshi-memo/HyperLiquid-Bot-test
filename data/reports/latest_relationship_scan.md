# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T14:52:31.827192+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11136`

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

- `market_context_high->unknown_4h` score `46.4461` n `88` status `ready` deltaP `7.6774` edge `3.8641` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.7071` n `88` status `ready` deltaP `32.8678` edge `2.9136` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4404` n `88` status `ready` deltaP `25.8783` edge `0.3271` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `5.0052` n `88` status `ready` deltaP `24.3343` edge `0.9889` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.7034` n `88` status `ready` deltaP `19.5033` edge `-0.0161` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.2934` n `88` status `ready` deltaP `4.3958` edge `0.0139` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3988` n `88` status `ready` deltaP `2.2387` edge `0.0022` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.5136` n `88` status `ready` deltaP `2.7993` edge `0.0261` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6021` n `88` status `ready` deltaP `3.7001` edge `-0.0041` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9854` n `88` status `ready` deltaP `-7.3557` edge `0.0058` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0377` n `88` status `ready` deltaP `-0.5959` edge `0.0093` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3249` n `88` status `ready` deltaP `-14.3576` edge `-0.0057` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.598` n `88` status `ready` deltaP `-7.6551` edge `0.0308` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8703` n `88` status `ready` deltaP `1.2316` edge `-0.0501` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.9389` n `88` status `ready` deltaP `-3.5615` edge `-0.0067` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.2136` n `88` status `ready` deltaP `-0.7799` edge `-0.0193` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9788` n `88` status `ready` deltaP `-3.4635` edge `-0.0965` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.4056` n `88` status `ready` deltaP `0.6098` edge `-0.1567` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.5704` n `88` status `ready` deltaP `3.617` edge `-0.2265` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2392` n `88` status `ready` deltaP `-23.4698` edge `-0.0611` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
