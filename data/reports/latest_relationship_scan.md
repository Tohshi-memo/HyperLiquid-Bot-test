# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T08:07:25.664298+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_4h` score `14.7344` n `51` status `ready` deltaP `26.5453` edge `1.0555` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `5.0133` n `33` status `ready` deltaP `-8.0294` edge `0.7411` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.0133` n `33` status `ready` deltaP `-8.0294` edge `0.7411` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.7503` n `51` status `ready` deltaP `19.778` edge `0.2111` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `2.9586` n `51` status `ready` deltaP `25.0986` edge `0.1565` maxDD `-2.1818`
- `news_risk_high->fx_4h` score `2.844` n `51` status `ready` deltaP `33.8146` edge `0.025` maxDD `-0.0746`
- `market_context_high->unknown_1h` score `1.3232` n `135` status `ready` deltaP `8.5362` edge `0.0982` maxDD `-1.5876`
- `news_risk_high->fx_1h` score `1.193` n `51` status `ready` deltaP `16.5463` edge `0.0061` maxDD `-0.0257`
- `market_context_high->commodity_24h` score `0.9782` n `106` status `ready` deltaP `2.3356` edge `0.1131` maxDD `-1.1056`
- `news_risk_high->equity_1h` score `0.8563` n `51` status `ready` deltaP `18.4924` edge `0.023` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.8413` n `123` status `ready` deltaP `22.002` edge `-0.0594` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.7056` n `51` status `ready` deltaP `11.7198` edge `0.0204` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2403` n `51` status `ready` deltaP `9.4223` edge `0.0033` maxDD `-0.1583`
- `risk_on_high->fx_1h` score `0.2278` n `33` status `ready` deltaP `6.5642` edge `0.0031` maxDD `-0.0796`
- `risk_on_and_context->fx_1h` score `0.2278` n `33` status `ready` deltaP `6.5642` edge `0.0031` maxDD `-0.0796`
- `market_context_high->fx_4h` score `0.2168` n `123` status `ready` deltaP `8.1809` edge `0.0092` maxDD `-0.3204`
- `news_risk_high->commodity_1h` score `0.1488` n `51` status `ready` deltaP `8.0897` edge `-0.0107` maxDD `-0.4666`
- `news_risk_high->metal_4h` score `0.076` n `51` status `ready` deltaP `10.4167` edge `-0.01` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.0928` n `51` status `ready` deltaP `2.6418` edge `-0.0072` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.123` n `135` status `ready` deltaP `2.9951` edge `0.0055` maxDD `-0.1905`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
