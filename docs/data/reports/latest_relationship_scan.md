# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T14:37:32.261880+00:00`
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

- `market_context_high->unknown_4h` score `42.5953` n `88` status `ready` deltaP `7.6774` edge `3.5432` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.7282` n `88` status `ready` deltaP `33.0412` edge `2.9142` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4416` n `88` status `ready` deltaP `25.8783` edge `0.3272` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.9853` n `88` status `ready` deltaP `24.161` edge `0.9875` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.6667` n `88` status `ready` deltaP `19.33` edge `-0.018` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.2946` n `88` status `ready` deltaP `4.3958` edge `0.0138` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3996` n `88` status `ready` deltaP `2.2387` edge `0.0021` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.527` n `88` status `ready` deltaP `2.6469` edge `0.0254` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6013` n `88` status `ready` deltaP `3.7001` edge `-0.004` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9769` n `88` status `ready` deltaP `-7.206` edge `0.0059` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0377` n `88` status `ready` deltaP `-0.5959` edge `0.0093` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3249` n `88` status `ready` deltaP `-14.3576` edge `-0.0057` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5863` n `88` status `ready` deltaP `-7.6551` edge `0.0323` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8516` n `88` status `ready` deltaP `1.3813` edge `-0.0487` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.9484` n `88` status `ready` deltaP `-3.714` edge `-0.0069` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.2311` n `88` status `ready` deltaP `-0.9532` edge `-0.0196` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9889` n `88` status `ready` deltaP `-3.6132` edge `-0.0968` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.4274` n `88` status `ready` deltaP `0.4573` edge `-0.1575` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.5403` n `88` status `ready` deltaP `3.7694` edge `-0.225` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.25` n `88` status `ready` deltaP `-23.4698` edge `-0.062` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
