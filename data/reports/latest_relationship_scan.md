# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T05:22:16.447352+00:00`
- Price records: `672`
- Market context records: `2012`
- Flow alert records: `7682`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9107`

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

- `market_context_high->crypto_major_4h` score `8.9319` n `210` status `ready` deltaP `31.083` edge `0.5901` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4036` n `210` status `ready` deltaP `24.7604` edge `0.6497` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.7657` n `210` status `ready` deltaP `18.9881` edge `0.4288` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.8278` n `210` status `ready` deltaP `16.1847` edge `0.2372` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5334` n `210` status `ready` deltaP `12.5848` edge `0.1425` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2475` n `210` status `ready` deltaP `10.1896` edge `0.1474` maxDD `-4.9097`
- `market_context_high->index_4h` score `1.2456` n `210` status `ready` deltaP `11.7842` edge `0.0936` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `0.9753` n `187` status `ready` deltaP `15.8276` edge `0.5078` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.6818` n `187` status `ready` deltaP `14.1025` edge `0.2054` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.5026` n `187` status `ready` deltaP `14.6738` edge `0.4339` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.1799` n `187` status `ready` deltaP `14.6317` edge `0.0266` maxDD `-2.0659`
- `market_context_high->equity_1h` score `0.1492` n `210` status `ready` deltaP `6.46` edge `0.0482` maxDD `-2.6402`
- `market_context_high->index_24h` score `-0.0187` n `187` status `ready` deltaP `2.9668` edge `0.1015` maxDD `-4.1604`
- `market_context_high->unknown_1h` score `-0.316` n `210` status `ready` deltaP `3.7539` edge `0.0206` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.3934` n `210` status `ready` deltaP `1.6439` edge `0.0153` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.7915` n `210` status `ready` deltaP `-0.5988` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0339` n `210` status `ready` deltaP `-6.4213` edge `-0.0016` maxDD `-1.0513`
- `market_context_high->metal_1h` score `-1.0758` n `210` status `ready` deltaP `2.7887` edge `0.0105` maxDD `-5.166`
- `market_context_high->crypto_major_24h` score `-1.4774` n `187` status `ready` deltaP `17.0345` edge `0.6219` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.5626` n `210` status `ready` deltaP `7.1617` edge `0.0843` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
