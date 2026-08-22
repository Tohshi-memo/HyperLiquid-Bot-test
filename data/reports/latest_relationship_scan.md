# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T09:07:26.991212+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.2619` n `135` status `ready` deltaP `7.6769` edge `0.0767` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4821` n `133` status `ready` deltaP `20.0234` edge `-0.0494` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1047` n `135` status `ready` deltaP `9.2437` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1034` n `133` status `ready` deltaP `8.0575` edge `0.0098` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1404` n `135` status `ready` deltaP `1.9938` edge `0.0046` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2218` n `133` status `ready` deltaP `7.5382` edge `-0.0171` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.224` n `135` status `ready` deltaP `6.2497` edge `0.0366` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2739` n `135` status `ready` deltaP `1.7022` edge `-0.0046` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6363` n `133` status `ready` deltaP `1.7067` edge `0.0106` maxDD `-2.618`
- `market_context_high->commodity_1h` score `-0.6701` n `135` status `ready` deltaP `-4.2471` edge `-0.001` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7115` n `133` status `ready` deltaP `-1.6184` edge `0.0046` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.2041` n `135` status `ready` deltaP `-0.7706` edge `-0.0056` maxDD `-3.1684`
- `market_context_high->commodity_24h` score `-1.5712` n `109` status `ready` deltaP `-4.6062` edge `0.0831` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.611` n `135` status `ready` deltaP `-3.1115` edge `-0.0833` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.6823` n `133` status `ready` deltaP `4.9652` edge `-0.0463` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.7285` n `133` status `ready` deltaP `-1.3628` edge `0.068` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.3833` n `109` status `ready` deltaP `-6.0334` edge `0.0026` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.2342` n `109` status `ready` deltaP `-5.4679` edge `-0.0516` maxDD `-19.0506`
- `market_context_high->metal_24h` score `-5.1511` n `109` status `ready` deltaP `-20.9703` edge `-0.1898` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.1997` n `133` status `ready` deltaP `-1.8017` edge `-0.3192` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
