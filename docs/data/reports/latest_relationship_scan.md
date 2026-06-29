# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T13:37:27.656919+00:00`
- Price records: `672`
- Market context records: `5148`
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

- `market_context_high->unknown_24h` score `28.2051` n `65` status `ready` deltaP `32.4359` edge `2.1683` maxDD `-1.3955`
- `market_context_high->unknown_4h` score `6.4603` n `128` status `ready` deltaP `18.8072` edge `0.5152` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.7985` n `139` status `ready` deltaP `9.9535` edge `0.481` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.4278` n `128` status `ready` deltaP `17.2256` edge `0.4974` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3212` n `128` status `ready` deltaP `15.1867` edge `0.4881` maxDD `-14.0065`
- `market_context_high->crypto_alt_24h` score `3.1922` n `65` status `ready` deltaP `18.5016` edge `0.74` maxDD `-31.994`
- `market_context_high->crypto_major_24h` score `2.8944` n `65` status `ready` deltaP `16.8376` edge `0.7477` maxDD `-32.4437`
- `market_context_high->commodity_24h` score `1.6709` n `65` status `ready` deltaP `18.3333` edge `0.1403` maxDD `-5.1955`
- `market_context_high->equity_4h` score `1.3339` n `128` status `ready` deltaP `11.7188` edge `0.1969` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `1.0039` n `139` status `ready` deltaP `8.6557` edge `0.1505` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.9719` n `139` status `ready` deltaP `6.2314` edge `0.1356` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.6964` n `139` status `ready` deltaP `7.4915` edge `0.0674` maxDD `-2.745`
- `market_context_high->metal_24h` score `0.6114` n `65` status `ready` deltaP `-0.2297` edge `0.2192` maxDD `-6.1426`
- `market_context_high->metal_1h` score `0.027` n `139` status `ready` deltaP `6.1399` edge `0.0191` maxDD `-1.8592`
- `market_context_high->index_1h` score `-0.1057` n `139` status `ready` deltaP `4.1647` edge `0.0138` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3648` n `139` status `ready` deltaP `0.6591` edge `-0.0005` maxDD `-0.7196`
- `market_context_high->index_4h` score `-0.3718` n `128` status `ready` deltaP `6.593` edge `0.0368` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.5032` n `65` status `ready` deltaP `6.1806` edge `0.0064` maxDD `-0.8294`
- `market_context_high->commodity_1h` score `-0.6799` n `139` status `ready` deltaP `-0.7507` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7147` n `128` status `ready` deltaP `1.3147` edge `0.0041` maxDD `-1.6932`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
