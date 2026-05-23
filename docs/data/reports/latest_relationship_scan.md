# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T20:22:18.720408+00:00`
- Price records: `672`
- Market context records: `1665`
- Flow alert records: `6699`
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

- `market_context_high->metal_24h` score `10.0768` n `168` status `ready` deltaP `28.835` edge `0.8901` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.6126` n `195` status `ready` deltaP `22.8901` edge `0.4982` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8028` n `168` status `ready` deltaP `20.4749` edge `0.3182` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.7066` n `195` status `ready` deltaP `18.9955` edge `0.3698` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.0168` n `195` status `ready` deltaP `13.2028` edge `0.1895` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7702` n `168` status `ready` deltaP `19.8241` edge `0.5052` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.9706` n `168` status `ready` deltaP `25.6447` edge `0.7685` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.7287` n `168` status `ready` deltaP `26.3305` edge `1.0661` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.5895` n `207` status `ready` deltaP `6.644` edge `0.1072` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.2716` n `207` status `ready` deltaP `2.5681` edge `0.0411` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3087` n `195` status `ready` deltaP `2.0732` edge `0.0555` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.3651` n `168` status `ready` deltaP `7.1676` edge `0.0267` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.4299` n `207` status `ready` deltaP `-0.4122` edge `0.0108` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.5199` n `207` status `ready` deltaP `3.6095` edge `0.06` maxDD `-5.5244`
- `market_context_high->metal_1h` score `-0.7126` n `207` status `ready` deltaP `5.3581` edge `0.0065` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.8654` n `207` status `ready` deltaP `-0.8541` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-1.2107` n `195` status `ready` deltaP `9.764` edge `0.1032` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.5253` n `207` status `ready` deltaP `-0.6227` edge `-0.0199` maxDD `-10.3862`
- `market_context_high->fx_4h` score `-1.9413` n `195` status `ready` deltaP `-8.3224` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.5469` n `195` status `ready` deltaP `11.5666` edge `-0.2289` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
