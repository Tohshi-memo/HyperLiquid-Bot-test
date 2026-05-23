# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T13:22:14.666217+00:00`
- Price records: `672`
- Market context records: `1633`
- Flow alert records: `6612`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `10.1593` n `182` status `ready` deltaP `27.0764` edge `0.9087` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.3015` n `182` status `ready` deltaP `19.1888` edge `0.285` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `1.4872` n `186` status `ready` deltaP `17.1282` edge `0.3429` maxDD `-16.3135`
- `market_context_high->equity_4h` score `1.4289` n `186` status `ready` deltaP `11.7494` edge `0.1502` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.7386` n `182` status `ready` deltaP `17.6843` edge `0.4335` maxDD `-33.1875`
- `market_context_high->crypto_major_4h` score `0.6752` n `186` status `ready` deltaP `12.9082` edge `0.2714` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2093` n `196` status `ready` deltaP `1.775` edge `0.0637` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.3418` n `182` status `ready` deltaP `7.2638` edge `0.028` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.5159` n `182` status `ready` deltaP `23.234` edge `0.6607` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.5404` n `196` status `ready` deltaP `0.9777` edge `0.0293` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6507` n `196` status `ready` deltaP `0.5622` edge `0.0052` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8025` n `196` status `ready` deltaP `-0.0825` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8447` n `186` status `ready` deltaP `0.2258` edge `0.037` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.8721` n `196` status `ready` deltaP `-1.3198` edge `0.0301` maxDD `-5.9819`
- `market_context_high->commodity_1h` score `-0.8933` n `196` status `ready` deltaP `1.7139` edge `0.0021` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.4059` n `196` status `ready` deltaP `2.0133` edge `0.003` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.5097` n `186` status `ready` deltaP `7.4213` edge `0.0939` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-1.689` n `182` status `ready` deltaP `23.4997` edge `0.8835` maxDD `-88.8062`
- `market_context_high->fx_4h` score `-1.9658` n `186` status `ready` deltaP `-8.6291` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.1298` n `186` status `ready` deltaP `7.7651` edge `-0.1688` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
