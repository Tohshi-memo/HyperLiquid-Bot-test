# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T07:22:23.991430+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14742`

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

- `market_context_high->unknown_1h` score `1.4496` n `133` status `ready` deltaP `8.5375` edge `0.0866` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5669` n `133` status `ready` deltaP `20.6331` edge `-0.0464` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1367` n `133` status `ready` deltaP `9.8577` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1034` n `133` status `ready` deltaP `8.0575` edge `0.0098` maxDD `-0.3539`
- `market_context_high->equity_1h` score `-0.1773` n `133` status `ready` deltaP `7.0134` edge `0.0375` maxDD `-5.2257`
- `market_context_high->fx_1h` score `-0.186` n `133` status `ready` deltaP `1.1312` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2582` n `133` status `ready` deltaP `6.9285` edge `-0.0177` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.2794` n `133` status `ready` deltaP `1.5803` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->commodity_1h` score `-0.6566` n `133` status `ready` deltaP `-3.9721` edge `-0.0011` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6632` n `133` status `ready` deltaP `1.2494` edge `0.0102` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7139` n `133` status `ready` deltaP `-1.6184` edge `0.0043` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8874` n `133` status `ready` deltaP `-0.4783` edge `0.0094` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4502` n `133` status `ready` deltaP `-2.1487` edge `-0.0691` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5891` n `105` status `ready` deltaP `-5.6547` edge `0.0886` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.7796` n `133` status `ready` deltaP `-1.8201` edge `0.0645` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.1989` n `133` status `ready` deltaP `4.5079` edge `-0.0863` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.5385` n `105` status `ready` deltaP `-7.6141` edge `0.0002` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1956` n `105` status `ready` deltaP `-4.9008` edge `-0.055` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0478` n `105` status `ready` deltaP `-20.0199` edge `-0.1829` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5251` n `133` status `ready` deltaP `-1.9542` edge `-0.3453` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
