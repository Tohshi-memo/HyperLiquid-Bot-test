# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T12:37:27.444183+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3915`

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

- `news_risk_high->equity_24h` score `-0.0654` n `120` status `ready` deltaP `21.9983` edge `1.0036` maxDD `-86.0244`
- `news_risk_high->index_4h` score `-0.2559` n `120` status `ready` deltaP `8.1809` edge `0.0116` maxDD `-2.2494`
- `news_risk_high->index_1h` score `-0.2572` n `120` status `ready` deltaP `5.8782` edge `0.002` maxDD `-0.9325`
- `news_risk_high->fx_1h` score `-0.4918` n `120` status `ready` deltaP `-2.8243` edge `-0.002` maxDD `-0.378`
- `news_risk_high->crypto_alt_4h` score `-0.4958` n `120` status `ready` deltaP `5.1423` edge `0.1658` maxDD `-14.0916`
- `news_risk_high->index_24h` score `-0.69` n `120` status `ready` deltaP `-3.8523` edge `0.1207` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.7412` n `120` status `ready` deltaP `0.5788` edge `0.0239` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.8161` n `120` status `ready` deltaP `-3.1504` edge `-0.0027` maxDD `-0.4745`
- `news_risk_high->metal_1h` score `-1.1621` n `120` status `ready` deltaP `-4.017` edge `-0.0134` maxDD `-1.5332`
- `news_risk_high->fx_24h` score `-1.4214` n `120` status `ready` deltaP `-16.7532` edge `-0.0071` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.4979` n `120` status `ready` deltaP `-1.8164` edge `0.0135` maxDD `-10.4741`
- `news_risk_high->crypto_major_1h` score `-1.6834` n `120` status `ready` deltaP `-4.506` edge `-0.0097` maxDD `-4.7103`
- `news_risk_high->crypto_major_4h` score `-1.8438` n `120` status `ready` deltaP `-4.1463` edge `0.0551` maxDD `-9.1553`
- `news_risk_high->commodity_1h` score `-2.836` n `120` status `ready` deltaP `-13.9321` edge `-0.0068` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-2.8604` n `120` status `ready` deltaP `-7.5305` edge `-0.0497` maxDD `-3.4101`
- `news_risk_high->equity_4h` score `-3.2476` n `120` status `ready` deltaP `8.6382` edge `0.0851` maxDD `-27.066`
- `news_risk_high->metal_24h` score `-3.517` n `120` status `ready` deltaP `-5.6978` edge `-0.2233` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.6457` n `120` status `ready` deltaP `-21.0467` edge `-0.0114` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.5622` n `120` status `ready` deltaP `-17.8921` edge `0.1283` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.2648` n `120` status `ready` deltaP `-23.2324` edge `0.0142` maxDD `-39.8442`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
