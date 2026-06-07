# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T06:40:51.231536+00:00`
- Price records: `672`
- Market context records: `3153`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7978`

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

- `market_context_high->commodity_24h` score `14.1994` n `111` status `ready` deltaP `47.7618` edge `0.9077` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.0847` n `111` status `ready` deltaP `22.5835` edge `0.9053` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.9832` n `111` status `ready` deltaP `13.6824` edge `2.4427` maxDD `-71.142`
- `market_context_high->index_24h` score `6.7128` n `111` status `ready` deltaP `31.7192` edge `0.9046` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.0039` n `111` status `ready` deltaP `13.4478` edge `1.3935` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8812` n `145` status `ready` deltaP `18.9151` edge `0.1598` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1948` n `145` status `ready` deltaP `4.5736` edge `0.028` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.2976` n `111` status `ready` deltaP `6.6442` edge `-0.0005` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.418` n `145` status `ready` deltaP `5.8301` edge `0.1205` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.5249` n `145` status `ready` deltaP `3.4617` edge `0.0159` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.858` n `145` status `ready` deltaP `3.1623` edge `0.0175` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.0262` n `145` status `ready` deltaP `2.7937` edge `0.0761` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1415` n `145` status `ready` deltaP `-10.9034` edge `-0.0054` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1879` n `145` status `ready` deltaP `11.3866` edge `0.0627` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.4532` n `145` status `ready` deltaP `6.5885` edge `0.0572` maxDD `-14.7778`
- `market_context_high->fx_4h` score `-1.4686` n `145` status `ready` deltaP `-13.6954` edge `-0.0085` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.0925` n `145` status `ready` deltaP `-4.4559` edge `-0.0053` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.8237` n `145` status `ready` deltaP `13.6732` edge `0.0774` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.9536` n `145` status `ready` deltaP `18.9066` edge `0.4323` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0863` n `145` status `ready` deltaP `2.0019` edge `-0.0679` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
