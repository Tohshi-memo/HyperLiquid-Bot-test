# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T17:22:25.942093+00:00`
- Price records: `672`
- Market context records: `2060`
- Flow alert records: `7823`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.629` n `205` status `ready` deltaP `33.8415` edge `0.6298` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.9306` n `205` status `ready` deltaP `26.0671` edge `0.6849` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.4861` n `205` status `ready` deltaP `20.8231` edge `0.4766` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.4123` n `205` status `ready` deltaP `18.3797` edge `0.7772` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5256` n `205` status `ready` deltaP `19.2378` edge `0.275` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0421` n `205` status `ready` deltaP `15.3659` edge `0.1361` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.7838` n `206` status `ready` deltaP `13.8553` edge `0.1549` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.4082` n `205` status `ready` deltaP `19.259` edge `0.4788` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.3985` n `206` status `ready` deltaP `10.7116` edge `0.1565` maxDD `-4.9097`
- `market_context_high->index_24h` score `1.2264` n `205` status `ready` deltaP `7.761` edge `0.1733` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4453` n `206` status `ready` deltaP `8.4211` edge `0.0598` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.3252` n `206` status `ready` deltaP `5.1087` edge `0.065` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.0792` n `206` status `ready` deltaP `4.0565` edge `0.0254` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `-0.1592` n `205` status `ready` deltaP `19.4725` edge `0.7155` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3332` n `205` status `ready` deltaP `13.0255` edge `0.0247` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.6129` n `205` status `ready` deltaP `11.1586` edge `0.1368` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7584` n `206` status `ready` deltaP `4.1466` edge `0.0279` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8167` n `206` status `ready` deltaP `-0.8982` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4174` n `205` status `ready` deltaP `-4.4512` edge `-0.0003` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9629` n `206` status `ready` deltaP `1.9417` edge `-0.0088` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
