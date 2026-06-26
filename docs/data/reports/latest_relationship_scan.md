# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T22:37:30.358219+00:00`
- Price records: `672`
- Market context records: `4872`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7594`

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

- `market_context_high->unknown_1h` score `15.3054` n `110` status `ready` deltaP `10.1715` edge `1.2494` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6708` n `110` status `ready` deltaP `23.3148` edge `0.7036` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4484` n `110` status `ready` deltaP `21.2084` edge `0.5312` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.1554` n `110` status `ready` deltaP `18.3398` edge `0.5131` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2602` n `91` status `ready` deltaP `25.8166` edge `0.3005` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2644` n `110` status `ready` deltaP `9.4346` edge `0.1087` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.882` n `110` status `ready` deltaP `12.439` edge `0.1683` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5462` n `110` status `ready` deltaP `11.383` edge `0.0404` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4804` n `110` status `ready` deltaP `6.6195` edge `0.1213` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4448` n `110` status `ready` deltaP `8.3206` edge `0.1038` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2153` n `110` status `ready` deltaP `4.2352` edge `0.0591` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1511` n `110` status `ready` deltaP `1.1431` edge `0.031` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2098` n `110` status `ready` deltaP `3.5819` edge `0.0152` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4868` n `110` status `ready` deltaP `0.3103` edge `0.011` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6253` n `110` status `ready` deltaP `1.6768` edge `0.0057` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9132` n `110` status `ready` deltaP `5.8148` edge `0.0038` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3609` n `110` status `ready` deltaP `-7.1666` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8404` n `91` status `ready` deltaP `-6.3359` edge `-0.0101` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.6763` n `91` status `ready` deltaP `-6.9712` edge `-0.1445` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.168` n `91` status `ready` deltaP `12.2424` edge `-0.0014` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
