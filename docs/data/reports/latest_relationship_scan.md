# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T00:07:23.021648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14774`

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

- `market_context_high->unknown_1h` score `1.405` n `133` status `ready` deltaP `9.286` edge `0.0779` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.47` n `133` status `ready` deltaP `22.7673` edge `-0.0687` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.185` n `133` status `ready` deltaP `9.5819` edge `0.0101` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1429` n `133` status `ready` deltaP `10.0074` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0856` n `133` status `ready` deltaP `3.0773` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2248` n `133` status `ready` deltaP `6.4146` edge `0.0354` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2997` n `133` status `ready` deltaP `1.2809` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3459` n `133` status `ready` deltaP `5.5565` edge `-0.0198` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.6006` n `133` status `ready` deltaP `2.4689` edge `0.0101` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6225` n `133` status `ready` deltaP `-0.5513` edge `0.0089` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6503` n `133` status `ready` deltaP `-4.1218` edge `0.0007` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7425` n `133` status `ready` deltaP `1.0187` edge `0.0115` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.1827` n `105` status `ready` deltaP `-1.8353` edge `0.097` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.3122` n `133` status `ready` deltaP `-1.1008` edge `-0.0584` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.7076` n `133` status `ready` deltaP `3.8981` edge `-0.0413` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8374` n `133` status `ready` deltaP `-1.9726` edge `0.0581` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.3213` n `105` status `ready` deltaP `-5.1836` edge `0.0021` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3788` n `105` status `ready` deltaP `-8.1994` edge `-0.0565` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.5255` n `133` status `ready` deltaP `-0.1249` edge `-0.2742` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.9` n `105` status `ready` deltaP `-18.631` edge `-0.1732` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
