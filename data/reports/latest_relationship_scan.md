# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T13:52:29.839086+00:00`
- Price records: `672`
- Market context records: `5149`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `29.2945` n `64` status `ready` deltaP `33.6806` edge `2.2426` maxDD `-1.0743`
- `market_context_high->unknown_4h` score `6.5071` n `128` status `ready` deltaP `18.8072` edge `0.5191` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.8177` n `139` status `ready` deltaP `9.9535` edge `0.4826` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.5274` n `128` status `ready` deltaP `17.2256` edge `0.5057` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.5071` n `128` status `ready` deltaP `15.8155` edge `0.4994` maxDD `-14.0065`
- `market_context_high->crypto_alt_24h` score `4.182` n `64` status `ready` deltaP `19.0972` edge `0.8028` maxDD `-27.5167`
- `market_context_high->crypto_major_24h` score `3.9816` n `64` status `ready` deltaP `17.3611` edge `0.8183` maxDD `-27.2194`
- `market_context_high->commodity_24h` score `1.8179` n `64` status `ready` deltaP `19.2708` edge `0.1463` maxDD `-5.1955`
- `market_context_high->equity_4h` score `1.4203` n `128` status `ready` deltaP `11.7188` edge `0.2041` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `1.0603` n `139` status `ready` deltaP `8.6557` edge `0.1552` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `1.0067` n `139` status `ready` deltaP `6.2314` edge `0.1385` maxDD `-5.0257`
- `market_context_high->metal_24h` score `0.8438` n `64` status `ready` deltaP `0.3472` edge `0.2367` maxDD `-5.4668`
- `market_context_high->equity_1h` score `0.7648` n `139` status `ready` deltaP `7.4915` edge `0.0731` maxDD `-2.745`
- `market_context_high->metal_1h` score `0.0285` n `139` status `ready` deltaP `6.1399` edge `0.0193` maxDD `-1.8592`
- `market_context_high->index_1h` score `-0.1021` n `139` status `ready` deltaP `4.1647` edge `0.0141` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2924` n `139` status `ready` deltaP `1.2288` edge `-0.0001` maxDD `-0.646`
- `market_context_high->index_4h` score `-0.3682` n `128` status `ready` deltaP `6.593` edge `0.0371` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4145` n `64` status `ready` deltaP `6.9444` edge `0.0087` maxDD `-0.8294`
- `market_context_high->fx_4h` score `-0.6712` n `128` status `ready` deltaP `1.9436` edge `0.0048` maxDD `-1.638`
- `market_context_high->commodity_1h` score `-0.6807` n `139` status `ready` deltaP `-0.7507` edge `-0.0014` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
