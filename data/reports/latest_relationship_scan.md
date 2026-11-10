# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T15:07:39.360618+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11430`

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

- `market_context_high->unknown_4h` score `54.5965` n `88` status `ready` deltaP `7.6774` edge `4.5433` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.6572` n `88` status `ready` deltaP `32.6945` edge `2.9106` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.438` n `88` status `ready` deltaP `25.8783` edge `0.3269` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `5.0068` n `88` status `ready` deltaP `24.3343` edge `0.9891` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.7329` n `88` status `ready` deltaP `19.6766` edge `-0.0148` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.2958` n `88` status `ready` deltaP `4.3958` edge `0.0137` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3996` n `88` status `ready` deltaP `2.2387` edge `0.0021` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.5002` n `88` status `ready` deltaP `2.9518` edge `0.0268` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6108` n `88` status `ready` deltaP `3.5477` edge `-0.0042` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9963` n `88` status `ready` deltaP `-7.5054` edge `0.0054` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0408` n `88` status `ready` deltaP `-0.5959` edge `0.0089` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3163` n `88` status `ready` deltaP `-14.2079` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6182` n `88` status `ready` deltaP `-7.6551` edge `0.0282` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.882` n `88` status `ready` deltaP `1.2316` edge `-0.0516` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.9302` n `88` status `ready` deltaP `-3.4091` edge `-0.0066` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.1938` n `88` status `ready` deltaP `-0.6066` edge `-0.0188` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9819` n `88` status `ready` deltaP `-3.4635` edge `-0.0969` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.4164` n `88` status `ready` deltaP `0.6098` edge `-0.1576` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.6102` n `88` status `ready` deltaP `3.4645` edge `-0.2288` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.232` n `88` status `ready` deltaP `-23.4698` edge `-0.0605` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
