# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T21:52:22.796507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `55.4064` n `50` status `ready` deltaP `15.9445` edge `4.5109` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.2527` n `50` status `ready` deltaP `46.6066` edge `2.5878` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `8.7822` n `70` status `ready` deltaP `17.365` edge `0.6471` maxDD `-1.4812`
- `news_risk_high->crypto_major_24h` score `8.1415` n `50` status `ready` deltaP `25.7678` edge `0.556` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.3535` n `50` status `ready` deltaP `30.1005` edge `0.4216` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `4.7151` n `120` status `ready` deltaP `9.2778` edge `0.4043` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4082` n `50` status `ready` deltaP `43.4073` edge `0.0822` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.4585` n `71` status `ready` deltaP `9.1064` edge `0.2632` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2254` n `120` status `ready` deltaP `28.7406` edge `0.1791` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4094` n `50` status `ready` deltaP `26.9948` edge `0.0359` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2761` n `120` status `ready` deltaP `17.246` edge `0.1154` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.1959` n `70` status `ready` deltaP `32.3258` edge `0.0224` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.8711` n `120` status `ready` deltaP `8.9421` edge `0.058` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6081` n `71` status `ready` deltaP `12.5095` edge `0.006` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.358` n `71` status `ready` deltaP `11.1622` edge `0.0035` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0958` n `120` status `ready` deltaP `13.4553` edge `0.0143` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3873` n `120` status `ready` deltaP `3.6128` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4756` n `71` status `ready` deltaP `-1.1807` edge `-0.0097` maxDD `-0.8054`
- `news_risk_high->metal_1h` score `-0.6767` n `71` status `ready` deltaP `-0.4048` edge `-0.0265` maxDD `-2.605`
- `news_risk_high->index_4h` score `-0.7151` n `70` status `ready` deltaP `-1.1237` edge `-0.0204` maxDD `-1.7699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
