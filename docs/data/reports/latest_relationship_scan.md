# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T07:07:39.860498+00:00`
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

- `market_context_high->unknown_1h` score `1.4604` n `133` status `ready` deltaP `8.5375` edge `0.0875` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5899` n `133` status `ready` deltaP `20.7856` edge `-0.0455` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1367` n `133` status `ready` deltaP `9.8577` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1034` n `133` status `ready` deltaP `8.0575` edge `0.0098` maxDD `-0.3539`
- `market_context_high->equity_1h` score `-0.1765` n `133` status `ready` deltaP `7.0134` edge `0.0376` maxDD `-5.2257`
- `market_context_high->fx_1h` score `-0.186` n `133` status `ready` deltaP `1.1312` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2669` n `133` status `ready` deltaP `6.7761` edge `-0.0178` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.2717` n `133` status `ready` deltaP `1.73` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->commodity_1h` score `-0.655` n `133` status `ready` deltaP `-3.9721` edge `-0.0009` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.664` n `133` status `ready` deltaP `1.2494` edge `0.0101` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7036` n `133` status `ready` deltaP `-1.466` edge `0.0046` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.861` n `133` status `ready` deltaP `-0.3286` edge `0.0106` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.433` n `133` status `ready` deltaP `-1.999` edge `-0.0679` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5716` n `105` status `ready` deltaP `-5.4811` edge `0.0889` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.7922` n `133` status `ready` deltaP `-1.9726` edge `0.0639` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.2565` n `133` status `ready` deltaP `4.5079` edge `-0.0911` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.5247` n `105` status `ready` deltaP `-7.4405` edge `0.0002` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.2062` n `105` status `ready` deltaP `-5.0744` edge `-0.0552` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0577` n `105` status `ready` deltaP `-20.1935` edge `-0.183` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5563` n `133` status `ready` deltaP `-1.9542` edge `-0.3479` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
