# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T06:22:25.188111+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11824`

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

- `news_risk_high->unknown_24h` score `3400.8176` n `101` status `ready` deltaP `-0.6429` edge `283.4102` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8661` n `47` status `ready` deltaP `8.4693` edge `5.7728` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.439` n `47` status `ready` deltaP `24.5198` edge `3.9124` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.8457` n `47` status `ready` deltaP `22.6987` edge `2.3738` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3299` n `47` status `ready` deltaP `33.3739` edge `1.9239` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.2792` n `47` status `ready` deltaP `31.4642` edge `0.4098` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4401` n `47` status `ready` deltaP `28.982` edge `0.1173` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7009` n `47` status `ready` deltaP `16.992` edge `0.1536` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.492` n `47` status `ready` deltaP `28.691` edge `0.0318` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.2973` n `47` status `ready` deltaP `11.5172` edge `0.0981` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.2099` n `101` status `ready` deltaP `27.7812` edge `0.136` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0506` n `47` status `ready` deltaP `12.0652` edge `0.0474` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.769` n `47` status `ready` deltaP `12.3646` edge `0.0095` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5464` n `47` status `ready` deltaP `11.0077` edge `0.0078` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4274` n `47` status `ready` deltaP `4.6899` edge `0.0948` maxDD `-5.2359`
- `news_risk_high->index_24h` score `0.4088` n `101` status `ready` deltaP `14.0848` edge `0.0403` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3542` n `47` status `ready` deltaP `5.351` edge `0.0756` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.0866` n `130` status `ready` deltaP `4.8687` edge `0.004` maxDD `-0.3395`
- `market_context_high->fx_4h` score `0.0615` n `47` status `ready` deltaP `9.6264` edge `0.0077` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
