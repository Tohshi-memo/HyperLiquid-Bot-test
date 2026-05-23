# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T20:37:12.642255+00:00`
- Price records: `672`
- Market context records: `1666`
- Flow alert records: `6702`
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

- `market_context_high->metal_24h` score `9.9788` n `167` status `ready` deltaP `28.7352` edge `0.8826` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.663` n `195` status `ready` deltaP `22.8901` edge `0.5024` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8095` n `167` status `ready` deltaP `20.3644` edge `0.3195` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.7666` n `195` status `ready` deltaP `18.9955` edge `0.3748` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.048` n `195` status `ready` deltaP `13.2028` edge `0.1921` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7878` n `167` status `ready` deltaP `19.6993` edge `0.5075` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.9095` n `167` status `ready` deltaP `25.5413` edge `0.7641` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.7074` n `167` status `ready` deltaP `26.2593` edge `1.0648` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.6027` n `207` status `ready` deltaP `6.644` edge `0.1083` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.2632` n `207` status `ready` deltaP `2.5681` edge `0.0418` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.2728` n `195` status `ready` deltaP `2.4335` edge `0.0577` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.3653` n `167` status `ready` deltaP `7.255` edge `0.0261` maxDD `-1.3925`
- `market_context_high->crypto_major_1h` score `-0.4656` n `207` status `ready` deltaP `3.9428` edge `0.0623` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.6507` n `207` status `ready` deltaP `-0.4122` edge `0.0117` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7064` n `207` status `ready` deltaP `5.3581` edge `0.0073` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.8666` n `207` status `ready` deltaP `-0.8541` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-1.1915` n `195` status `ready` deltaP `9.764` edge `0.1048` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.682` n `207` status `ready` deltaP `-0.9561` edge `-0.0228` maxDD `-11.251`
- `market_context_high->fx_4h` score `-1.9401` n `195` status `ready` deltaP `-8.3224` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.3861` n `195` status `ready` deltaP `11.927` edge `-0.2179` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
