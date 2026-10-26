# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T13:07:33.556797+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8396`

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

- `market_context_high->unknown_4h` score `15.6842` n `143` status `ready` deltaP `-0.2931` edge `1.3425` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.585` n `113` status `ready` deltaP `28.4445` edge `0.1524` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.2402` n `143` status `ready` deltaP `10.6601` edge `0.0088` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1095` n `151` status `ready` deltaP `6.4411` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0208` n `113` status `ready` deltaP `19.6196` edge `0.0291` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.2643` n `151` status `ready` deltaP `6.5095` edge `0.0019` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2984` n `151` status `ready` deltaP `2.1454` edge `0.0109` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.4213` n `113` status `ready` deltaP `11.4768` edge `-0.0023` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.507` n `143` status `ready` deltaP `5.7821` edge `0.0421` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5658` n `151` status `ready` deltaP `-0.9071` edge `-0.0013` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.0202` n `143` status `ready` deltaP `6.573` edge `-0.0036` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.2085` n `151` status `ready` deltaP `1.955` edge `-0.0099` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.9009` n `143` status `ready` deltaP `-5.5763` edge `-0.0191` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.2593` n `151` status `ready` deltaP `-1.3106` edge `-0.0523` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.3454` n `151` status `ready` deltaP `-2.6758` edge `-0.0344` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.415` n `113` status `ready` deltaP `-2.0726` edge `-0.0665` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.9913` n `143` status `ready` deltaP `-2.6896` edge `-0.118` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.1782` n `113` status `ready` deltaP `-2.9914` edge `-0.2146` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4763` n `113` status `ready` deltaP `-18.8191` edge `-0.1459` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.7852` n `143` status `ready` deltaP `-4.5359` edge `-0.2417` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
