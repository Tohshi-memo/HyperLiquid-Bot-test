# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T18:07:19.305789+00:00`
- Price records: `672`
- Market context records: `1141`
- Flow alert records: `5188`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `19.8802` n `151` status `ready` deltaP `42.9785` edge `1.4473` maxDD `-5.5043`
- `market_context_high->crypto_alt_24h` score `9.641` n `151` status `ready` deltaP `19.3352` edge `0.8364` maxDD `-12.2838`
- `market_context_high->equity_24h` score `7.7549` n `151` status `ready` deltaP `18.8144` edge `0.5894` maxDD `-4.8203`
- `market_context_high->index_24h` score `6.067` n `151` status `ready` deltaP `17.4255` edge `0.4311` maxDD `-2.668`
- `market_context_high->metal_24h` score `5.6848` n `151` status `ready` deltaP `-1.7477` edge `0.6521` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.3234` n `168` status `ready` deltaP `11.5564` edge `0.1829` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0767` n `168` status `ready` deltaP `8.8995` edge `0.0987` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5409` n `168` status `ready` deltaP `7.9448` edge `0.0238` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4647` n `168` status `ready` deltaP `3.6284` edge `0.0523` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.3143` n `168` status `ready` deltaP `9.6762` edge `0.1679` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1268` n `168` status `ready` deltaP `8.1658` edge `0.0017` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.1005` n `168` status `ready` deltaP `7.1322` edge `0.0374` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2088` n `168` status `ready` deltaP `6.9504` edge `-0.0027` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2154` n `168` status `ready` deltaP `3.0938` edge `0.0457` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.735` n `168` status `ready` deltaP `0.6315` edge `0.0012` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-0.8223` n `168` status `ready` deltaP `6.9106` edge `0.145` maxDD `-16.7194`
- `market_context_high->commodity_1h` score `-0.8229` n `168` status `ready` deltaP `-2.8229` edge `-0.0059` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-2.3145` n `168` status `ready` deltaP `7.3098` edge `-0.0462` maxDD `-9.2991`
- `market_context_high->unknown_24h` score `-3.0982` n `151` status `ready` deltaP `3.5068` edge `-0.0086` maxDD `-10.1706`
- `market_context_high->commodity_4h` score `-3.339` n `168` status `ready` deltaP `-12.7976` edge `-0.026` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
