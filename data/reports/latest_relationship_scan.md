# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T22:07:33.790886+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_1h` score `12202.5001` n `105` status `ready` deltaP `-0.2966` edge `1016.8968` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `8123.384` n `100` status `ready` deltaP `-2.8354` edge `676.9981` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1380.1306` n `31` status `ready` deltaP `3.728` edge `115.0036` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1211.4685` n `31` status `ready` deltaP `3.9388` edge `100.9351` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.2158` n `31` status `ready` deltaP `40.4259` edge `0.7967` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0877` n `31` status `ready` deltaP `25.8457` edge `0.8387` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.825` n `31` status `ready` deltaP `15.5586` edge `0.913` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0038` n `31` status `ready` deltaP `19.688` edge `0.2211` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.6324` n `31` status `ready` deltaP `37.682` edge `0.0775` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7226` n `31` status `ready` deltaP `31.8428` edge `0.0231` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4759` n `31` status `ready` deltaP `9.7112` edge `0.2988` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0581` n `31` status `ready` deltaP `8.2142` edge `0.2448` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6993` n `31` status `ready` deltaP `22.7232` edge `0.1221` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5664` n `31` status `ready` deltaP `29.433` edge `0.0325` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.763` n `31` status `ready` deltaP `17.6682` edge `0.0198` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0789` n `31` status `ready` deltaP `1.2314` edge `0.0114` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3993` n `105` status `ready` deltaP `3.8109` edge `0.0078` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4352` n `105` status `ready` deltaP `1.6738` edge `0.0014` maxDD `-1.2394`
- `market_context_high->fx_4h` score `-1.3599` n `100` status `ready` deltaP `-0.0915` edge `0.005` maxDD `-1.2985`
- `market_context_high->fx_1h` score `-1.3909` n `105` status `ready` deltaP `-10.8155` edge `-0.0011` maxDD `-0.4163`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
