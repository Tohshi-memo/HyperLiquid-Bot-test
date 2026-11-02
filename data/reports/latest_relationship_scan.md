# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T05:22:27.610122+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5066`

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

- `market_context_high->unknown_24h` score `6814.9723` n `39` status `ready` deltaP `1.3889` edge `567.9051` maxDD `0.0`
- `market_context_high->unknown_4h` score `525.5169` n `42` status `ready` deltaP `9.1463` edge `43.7321` maxDD `0.0`
- `market_context_high->unknown_1h` score `103.378` n `44` status `ready` deltaP `6.3283` edge `8.5837` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.0231` n `39` status `ready` deltaP `42.054` edge `1.3285` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.8958` n `94` status `ready` deltaP `34.2605` edge `1.0652` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `7.0378` n `39` status `ready` deltaP `43.9904` edge `0.3243` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.9637` n `42` status `ready` deltaP `31.2354` edge `0.4015` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.5874` n `39` status `ready` deltaP `49.1319` edge `0.2214` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.5345` n `42` status `ready` deltaP `29.6748` edge `0.297` maxDD `-1.6901`
- `market_context_high->equity_4h` score `5.1285` n `42` status `ready` deltaP `10.0174` edge `0.4308` maxDD `-2.283`
- `market_context_high->commodity_4h` score `2.7902` n `42` status `ready` deltaP `29.0287` edge `0.0647` maxDD `-1.0567`
- `news_risk_high->crypto_alt_4h` score `2.2614` n `126` status `ready` deltaP `9.0132` edge `0.267` maxDD `-7.4246`
- `market_context_high->equity_1h` score `2.0287` n `44` status `ready` deltaP `4.2461` edge `0.1862` maxDD `-1.3028`
- `market_context_high->metal_4h` score `1.6962` n `42` status `ready` deltaP `19.9259` edge `0.051` maxDD `-0.7323`
- `market_context_high->crypto_alt_24h` score `1.6182` n `39` status `ready` deltaP `-8.32` edge `0.3421` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.2166` n `44` status `ready` deltaP `2.5721` edge `0.1381` maxDD `-1.9756`
- `market_context_high->crypto_major_1h` score `1.1139` n `44` status `ready` deltaP `4.2461` edge `0.1112` maxDD `-1.4011`
- `market_context_high->fx_1h` score `0.9639` n `44` status `ready` deltaP `13.337` edge `0.009` maxDD `-0.0736`
- `market_context_high->metal_1h` score `0.5934` n `44` status `ready` deltaP `8.5874` edge `0.0179` maxDD `-0.3895`
- `market_context_high->crypto_major_24h` score `0.38` n `39` status `ready` deltaP `-4.0599` edge `0.1264` maxDD `-3.0799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
