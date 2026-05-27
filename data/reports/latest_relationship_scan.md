# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T05:37:16.036380+00:00`
- Price records: `672`
- Market context records: `2013`
- Flow alert records: `7685`
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

- `market_context_high->crypto_major_4h` score `8.9475` n `210` status `ready` deltaP `31.083` edge `0.5914` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4506` n `210` status `ready` deltaP `24.9129` edge `0.6526` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.7971` n `210` status `ready` deltaP `19.1405` edge `0.4304` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.8604` n `210` status `ready` deltaP `16.3371` edge `0.2389` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5238` n `210` status `ready` deltaP `12.5848` edge `0.1417` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.2674` n `210` status `ready` deltaP `11.9367` edge `0.0944` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2379` n `210` status `ready` deltaP `10.1896` edge `0.1466` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `1.0467` n `188` status `ready` deltaP `15.9101` edge `0.5132` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.6592` n `188` status `ready` deltaP `13.8954` edge `0.2049` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.5201` n `188` status `ready` deltaP `14.7734` edge `0.4347` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.1516` n `210` status `ready` deltaP `6.46` edge `0.0484` maxDD `-2.6402`
- `market_context_high->fx_24h` score `0.0979` n `188` status `ready` deltaP `14.3762` edge `0.0262` maxDD `-2.1109`
- `market_context_high->index_24h` score `0.0223` n `188` status `ready` deltaP `3.0749` edge `0.1042` maxDD `-4.1604`
- `market_context_high->unknown_1h` score `-0.0076` n `210` status `ready` deltaP `3.7539` edge `0.0463` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.391` n `210` status `ready` deltaP `1.6439` edge `0.0155` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.7915` n `210` status `ready` deltaP `-0.5988` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0339` n `210` status `ready` deltaP `-6.4213` edge `-0.0016` maxDD `-1.0513`
- `market_context_high->metal_1h` score `-1.0542` n `210` status `ready` deltaP `2.9384` edge `0.0113` maxDD `-5.166`
- `market_context_high->crypto_major_24h` score `-1.4966` n `188` status `ready` deltaP `16.8245` edge `0.6217` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.5193` n `210` status `ready` deltaP `7.3141` edge `0.0869` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
