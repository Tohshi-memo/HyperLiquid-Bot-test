# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T22:52:14.122650+00:00`
- Price records: `672`
- Market context records: `1675`
- Flow alert records: `6732`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `9.0288` n `158` status `ready` deltaP `27.7802` edge `0.8098` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.1574` n `195` status `ready` deltaP `22.8901` edge `0.5436` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.869` n `158` status `ready` deltaP `19.307` edge `0.3315` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.2442` n `195` status `ready` deltaP `18.9955` edge `0.4146` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.5197` n `195` status `ready` deltaP `13.9236` edge `0.2266` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8723` n `158` status `ready` deltaP `18.5055` edge `0.5225` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7057` n `204` status `ready` deltaP `6.7013` edge `0.1165` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.5352` n `158` status `ready` deltaP `25.5771` edge `1.055` maxDD `-88.8062`
- `market_context_high->crypto_major_24h` score `0.2059` n `158` status `ready` deltaP `24.5522` edge `0.7213` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.0474` n `195` status `ready` deltaP `5.677` edge `0.075` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1674` n `204` status `ready` deltaP `2.9999` edge `0.0469` maxDD `-2.8014`
- `market_context_high->unknown_24h` score `-0.1875` n `158` status `ready` deltaP `12.6319` edge `0.4322` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `-0.3662` n `204` status `ready` deltaP `3.5958` edge `0.0729` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.5076` n `158` status `ready` deltaP `6.4364` edge `0.0197` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6372` n `204` status `ready` deltaP `-0.3493` edge `0.0124` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6462` n `204` status `ready` deltaP `5.7062` edge `0.0127` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.7557` n `195` status `ready` deltaP `12.2866` edge `0.1243` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.8582` n `204` status `ready` deltaP `-0.8835` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.2525` n `195` status `ready` deltaP `-8.3224` edge `-0.0122` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.2048` n `204` status `ready` deltaP `-0.5577` edge `-0.0335` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
