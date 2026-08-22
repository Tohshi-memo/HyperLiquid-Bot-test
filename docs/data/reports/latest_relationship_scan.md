# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T20:37:25.100872+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.5199` n `148` status `ready` deltaP `6.4169` edge `0.1066` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8091` n `148` status `ready` deltaP `18.6511` edge `-0.013` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0686` n `148` status `ready` deltaP `7.4778` edge `0.0092` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0011` n `148` status `ready` deltaP `7.2827` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1593` n `148` status `ready` deltaP `1.6589` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3252` n `148` status `ready` deltaP `4.9644` edge `0.0322` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.338` n `148` status `ready` deltaP `0.53` edge `-0.005` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3434` n `148` status `ready` deltaP `7.5272` edge `-0.0172` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.522` n `148` status `ready` deltaP `3.7698` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8982` n `148` status `ready` deltaP `-4.4578` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1192` n `148` status `ready` deltaP `-8.3266` edge `-0.0026` maxDD `-1.1631`
- `market_context_high->fx_24h` score `-1.1728` n `132` status `ready` deltaP `0.0473` edge `0.0103` maxDD `-2.2112`
- `market_context_high->crypto_alt_1h` score `-1.6568` n `148` status `ready` deltaP `-2.824` edge `-0.0441` maxDD `-7.9582`
- `market_context_high->equity_4h` score `-1.72` n `148` status `ready` deltaP `-1.1536` edge `0.0688` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1175` n `132` status `ready` deltaP `-4.6244` edge `0.0377` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-2.4173` n `148` status `ready` deltaP `-6.1336` edge `-0.1213` maxDD `-7.8171`
- `market_context_high->crypto_alt_4h` score `-2.664` n `148` status `ready` deltaP `2.2371` edge `-0.0901` maxDD `-7.0785`
- `market_context_high->index_24h` score `-4.3293` n `132` status `ready` deltaP `-5.808` edge `-0.0356` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3535` n `132` status `ready` deltaP `-22.8536` edge `-0.2032` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.9027` n `148` status `ready` deltaP `-1.0342` edge `-0.352` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
