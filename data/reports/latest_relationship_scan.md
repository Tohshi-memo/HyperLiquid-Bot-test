# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T08:07:31.048873+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4490`

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

- `news_risk_high->crypto_alt_4h` score `0.216` n `146` status `ready` deltaP `5.7802` edge `0.2528` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4137` n `146` status `ready` deltaP `2.1819` edge `0.0552` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6117` n `146` status `ready` deltaP `-0.8756` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8927` n `146` status `ready` deltaP `1.3473` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2602` n `146` status `ready` deltaP `-3.811` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2736` n `146` status `ready` deltaP `-4.7986` edge `-0.0091` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.6661` n `140` status `ready` deltaP `10.0149` edge `0.12` maxDD `-14.0483`
- `news_risk_high->index_4h` score `-2.0332` n `146` status `ready` deltaP `-2.6646` edge `-0.0128` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2404` n `140` status `ready` deltaP `-3.5764` edge `0.0208` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3888` n `146` status `ready` deltaP `-9.0764` edge `-0.0019` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4186` n `140` status `ready` deltaP `-17.9415` edge `-0.0196` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6906` n `146` status `ready` deltaP `-6.7857` edge `-0.0321` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2367` n `146` status `ready` deltaP `-8.3053` edge `-0.0418` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9319` n `146` status `ready` deltaP `-13.0847` edge `-0.005` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7339` n `146` status `ready` deltaP `-6.6906` edge `-0.0294` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-4.8636` n `140` status `ready` deltaP `19.489` edge `0.7455` maxDD `-104.5842`
- `news_risk_high->equity_24h` score `-6.9943` n `140` status `ready` deltaP `14.6279` edge `0.4746` maxDD `-78.7317`
- `news_risk_high->crypto_major_4h` score `-7.002` n `146` status `ready` deltaP `-14.0787` edge `-0.0877` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.4096` n `146` status `ready` deltaP `-1.1402` edge `-0.1071` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.7668` n `140` status `ready` deltaP `-24.0476` edge `-0.0976` maxDD `-42.145`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
