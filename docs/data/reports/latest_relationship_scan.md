# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T06:37:17.115557+00:00`
- Price records: `672`
- Market context records: `2116`
- Flow alert records: `7988`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `12.704` n `165` status `ready` deltaP `36.0754` edge `0.9118` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7076` n `165` status `ready` deltaP `41.3738` edge `0.7528` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.2381` n `165` status `ready` deltaP `24.9991` edge `0.4281` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.8778` n `165` status `ready` deltaP `25.0998` edge `0.3486` maxDD `-5.0894`
- `market_context_high->metal_4h` score `2.9735` n `165` status `ready` deltaP `20.4813` edge `0.25` maxDD `-4.7664`
- `market_context_high->index_4h` score `2.9373` n `165` status `ready` deltaP `21.1549` edge `0.1721` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.7533` n `164` status `ready` deltaP `12.2964` edge `0.2703` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.4008` n `165` status `ready` deltaP `15.5679` edge `0.189` maxDD `-3.0845`
- `market_context_high->crypto_alt_1h` score `2.3614` n `165` status `ready` deltaP `12.8733` edge `0.214` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.9172` n `164` status `ready` deltaP `23.6412` edge `0.492` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.7609` n `164` status `ready` deltaP `24.0126` edge `0.5187` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.171` n `164` status `ready` deltaP `20.755` edge `0.8178` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.7562` n `165` status `ready` deltaP `9.7732` edge `0.0767` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.4498` n `165` status `ready` deltaP `8.1673` edge `0.0501` maxDD `-2.3654`
- `market_context_high->unknown_1h` score `0.1448` n `165` status `ready` deltaP `5.6297` edge `0.0465` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.0053` n `165` status `ready` deltaP `4.2896` edge `0.03` maxDD `-1.3898`
- `market_context_high->metal_24h` score `-0.0368` n `164` status `ready` deltaP `11.1149` edge `0.3113` maxDD `-23.2095`
- `market_context_high->fx_24h` score `-0.081` n `164` status `ready` deltaP `14.6426` edge `0.0313` maxDD `-2.811`
- `market_context_high->fx_1h` score `-0.6349` n `165` status `ready` deltaP `-2.8842` edge `0.0006` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.1083` n `165` status `ready` deltaP `-7.7467` edge `-0.0029` maxDD `-1.004`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
