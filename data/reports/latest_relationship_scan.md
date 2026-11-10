# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T01:22:36.648344+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9942`

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

- `market_context_high->unknown_4h` score `38.1683` n `88` status `ready` deltaP `7.525` edge `3.1753` maxDD `-0.9153`
- `market_context_high->equity_24h` score `20.6461` n `65` status `ready` deltaP `29.6094` edge `2.69` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.4644` n `65` status `ready` deltaP `24.3461` edge `0.3281` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.1407` n `65` status `ready` deltaP `14.7873` edge `0.6853` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.3224` n `65` status `ready` deltaP `13.3609` edge `-0.0069` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3581` n `88` status `ready` deltaP `3.797` edge `0.0125` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5639` n `88` status `ready` deltaP `-0.4559` edge `-0.001` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8264` n `88` status `ready` deltaP `0.3464` edge `-0.0105` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8285` n `88` status `ready` deltaP `-1.6214` edge `0.0152` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.0672` n `88` status `ready` deltaP `-8.703` edge `0.0043` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1735` n `88` status `ready` deltaP `-2.5776` edge `0.0051` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3693` n `88` status `ready` deltaP `-15.1061` edge `-0.0064` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7492` n `88` status `ready` deltaP `-8.4036` edge `0.0164` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9109` n `88` status `ready` deltaP `0.9322` edge `-0.0533` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.192` n `88` status `ready` deltaP `-7.8298` edge `-0.0107` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.4844` n `65` status `ready` deltaP `-16.4991` edge `-0.0489` maxDD `-3.4362`
- `market_context_high->commodity_24h` score `-2.8475` n `65` status `ready` deltaP `-17.563` edge `0.0317` maxDD `-11.3747`
- `market_context_high->crypto_major_1h` score `-3.1931` n `88` status `ready` deltaP `-5.2599` edge `-0.112` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.3995` n `88` status `ready` deltaP `-2.439` edge `-0.2192` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1146` n `88` status `ready` deltaP `2.245` edge `-0.2627` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
