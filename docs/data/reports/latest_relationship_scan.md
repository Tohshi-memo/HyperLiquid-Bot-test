# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T03:22:23.661846+00:00`
- Price records: `672`
- Market context records: `3243`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10598`

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

- `market_context_high->crypto_alt_24h` score `14.1493` n `103` status `ready` deltaP `18.1297` edge `2.6773` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.5824` n `103` status `ready` deltaP `48.6887` edge `0.8501` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.5302` n `103` status `ready` deltaP `31.4893` edge `0.8397` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.4593` n `103` status `ready` deltaP `18.8748` edge `1.5439` maxDD `-53.663`
- `risk_on_high->crypto_major_1h` score `2.597` n `31` status `ready` deltaP `10.5273` edge `0.3697` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.597` n `31` status `ready` deltaP `10.5273` edge `0.3697` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.3087` n `103` status `ready` deltaP `22.2003` edge `2.2179` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `1.9205` n `141` status `ready` deltaP `17.5748` edge `0.1387` maxDD `-3.9989`
- `risk_on_high->crypto_alt_1h` score `0.73` n `31` status `ready` deltaP `3.8584` edge `0.2116` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.73` n `31` status `ready` deltaP `3.8584` edge `0.2116` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4639` n `31` status `ready` deltaP `7.9148` edge `0.0752` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4639` n `31` status `ready` deltaP `7.9148` edge `0.0752` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3087` n `31` status `ready` deltaP `2.3614` edge `0.1142` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3087` n `31` status `ready` deltaP `2.3614` edge `0.1142` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.111` n `31` status `ready` deltaP `0.1835` edge `0.0469` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.111` n `31` status `ready` deltaP `0.1835` edge `0.0469` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.3377` n `153` status `ready` deltaP `4.3981` edge `0.0241` maxDD `-2.5251`
- `market_context_high->index_1h` score `-0.418` n `153` status `ready` deltaP `4.7376` edge `0.0211` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.6853` n `141` status `ready` deltaP `8.342` edge `0.0831` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.709` n `153` status `ready` deltaP `4.7082` edge `0.104` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
