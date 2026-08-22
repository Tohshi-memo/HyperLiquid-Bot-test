# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T06:52:26.202247+00:00`
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

- `market_context_high->unknown_1h` score `1.4748` n `133` status `ready` deltaP `8.5375` edge `0.0887` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.6128` n `133` status `ready` deltaP `20.938` edge `-0.0446` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1367` n `133` status `ready` deltaP `9.8577` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1034` n `133` status `ready` deltaP `8.0575` edge `0.0098` maxDD `-0.3539`
- `market_context_high->equity_1h` score `-0.175` n `133` status `ready` deltaP `7.0134` edge `0.0378` maxDD `-5.2257`
- `market_context_high->fx_1h` score `-0.1868` n `133` status `ready` deltaP `1.1312` edge `0.0044` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2717` n `133` status `ready` deltaP `1.73` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2764` n `133` status `ready` deltaP `6.6236` edge `-0.018` maxDD `-1.5942`
- `market_context_high->commodity_1h` score `-0.6534` n `133` status `ready` deltaP `-3.9721` edge `-0.0007` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6727` n `133` status `ready` deltaP `1.0969` edge `0.01` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6933` n `133` status `ready` deltaP `-1.3135` edge `0.0049` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8227` n `133` status `ready` deltaP `-0.1789` edge `0.0128` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4065` n `133` status `ready` deltaP `-1.8493` edge `-0.0655` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.568` n `105` status `ready` deltaP `-5.4811` edge `0.0892` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.8048` n `133` status `ready` deltaP `-2.125` edge `0.0633` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.3107` n `133` status `ready` deltaP `4.3554` edge `-0.0946` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.5096` n `105` status `ready` deltaP `-7.2669` edge `0.0003` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.2176` n `105` status `ready` deltaP `-5.248` edge `-0.0555` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0675` n `105` status `ready` deltaP `-20.3671` edge `-0.1831` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5635` n `133` status `ready` deltaP `-1.9542` edge `-0.3485` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
