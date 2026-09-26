# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T15:22:29.236091+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11838`

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

- `news_risk_high->unknown_24h` score `4395.4468` n `85` status `ready` deltaP `0.6944` edge `366.2826` maxDD `0.0`
- `market_context_high->unknown_1h` score `68.4346` n `47` status `ready` deltaP `8.1698` edge `5.6555` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.7554` n `47` status `ready` deltaP `22.0892` edge `3.7883` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `26.2641` n `47` status `ready` deltaP `16.4487` edge `2.117` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5118` n `47` status `ready` deltaP `32.3323` edge `1.946` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.8568` n `47` status `ready` deltaP `26.9503` edge `0.4047` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2497` n `47` status `ready` deltaP `27.2459` edge `0.113` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7699` n `47` status `ready` deltaP `32.0446` edge `0.0326` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7351` n `47` status `ready` deltaP `17.4494` edge `0.1534` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.1515` n `85` status `ready` deltaP `25.098` edge `0.069` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `2.0251` n `85` status `ready` deltaP `10.3411` edge `0.495` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `1.4162` n `85` status `ready` deltaP `30.4249` edge `0.1435` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.1986` n `47` status `ready` deltaP `10.2977` edge `0.098` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0218` n `47` status `ready` deltaP `11.7658` edge `0.047` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8193` n `47` status `ready` deltaP `12.9634` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.7524` n `47` status `ready` deltaP `6.3667` edge `0.1107` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4578` n `47` status `ready` deltaP `9.9598` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4201` n `47` status `ready` deltaP `5.8001` edge `0.0781` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0289` n `47` status `ready` deltaP `3.7266` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0591` n `139` status `ready` deltaP `3.1211` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
