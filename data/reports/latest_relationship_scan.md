# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T10:07:35.188929+00:00`
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

- `market_context_high->unknown_4h` score `40.8877` n `88` status `ready` deltaP `7.6774` edge `3.4009` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.0762` n `88` status `ready` deltaP `33.0412` edge `2.9432` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4932` n `88` status `ready` deltaP `25.8783` edge `0.3315` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.4393` n `88` status `ready` deltaP `22.6012` edge `0.9279` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.0009` n `88` status `ready` deltaP `16.557` edge `-0.055` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3629` n `88` status `ready` deltaP `2.3884` edge `0.0058` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4166` n `88` status `ready` deltaP `3.1042` edge `0.0365` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.4863` n `88` status `ready` deltaP `2.5994` edge `0.0098` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.7845` n `88` status `ready` deltaP `0.9562` edge `-0.0092` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.068` n `88` status `ready` deltaP `-8.703` edge `0.0042` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2502` n `88` status `ready` deltaP `-2.8825` edge `-0.0027` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3086` n `88` status `ready` deltaP `-14.0582` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.813` n `88` status `ready` deltaP `-9.4515` edge `0.0152` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9701` n `88` status `ready` deltaP `0.4831` edge `-0.0579` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.026` n `88` status `ready` deltaP `-5.0859` edge `-0.0077` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.5503` n `88` status `ready` deltaP `-4.0728` edge `-0.0254` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1448` n `88` status `ready` deltaP `-4.8108` edge `-0.1088` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.2721` n `88` status `ready` deltaP `-2.2866` edge `-0.2096` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.0516` n `88` status `ready` deltaP `1.7877` edge `-0.2544` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2392` n `88` status `ready` deltaP `-23.4698` edge `-0.0611` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
