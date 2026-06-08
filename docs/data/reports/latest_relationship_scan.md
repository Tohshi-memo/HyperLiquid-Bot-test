# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T03:07:25.873972+00:00`
- Price records: `672`
- Market context records: `3242`
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

- `market_context_high->crypto_alt_24h` score `14.1911` n `103` status `ready` deltaP `18.3033` edge `2.6815` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.6155` n `103` status `ready` deltaP `48.8623` edge `0.8517` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.5728` n `103` status `ready` deltaP `31.663` edge `0.8421` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.5003` n `103` status `ready` deltaP `19.0484` edge `1.548` maxDD `-53.663`
- `risk_on_high->crypto_major_1h` score `2.6164` n `31` status `ready` deltaP `10.677` edge `0.3712` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.6164` n `31` status `ready` deltaP `10.677` edge `0.3712` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.3832` n `103` status `ready` deltaP `22.3739` edge `2.2263` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `1.8847` n `140` status `ready` deltaP `17.3519` edge `0.1372` maxDD `-3.9989`
- `risk_on_high->crypto_alt_1h` score `0.7464` n `31` status `ready` deltaP `4.0081` edge `0.2127` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.7464` n `31` status `ready` deltaP `4.0081` edge `0.2127` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4639` n `31` status `ready` deltaP `7.9148` edge `0.0752` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4639` n `31` status `ready` deltaP `7.9148` edge `0.0752` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3212` n `31` status `ready` deltaP `2.5111` edge `0.1148` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3212` n `31` status `ready` deltaP `2.5111` edge `0.1148` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1087` n `31` status `ready` deltaP `0.1835` edge `0.0472` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1087` n `31` status `ready` deltaP `0.1835` edge `0.0472` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.3618` n `152` status `ready` deltaP `4.0971` edge `0.0241` maxDD `-2.5251`
- `market_context_high->index_1h` score `-0.4427` n `152` status `ready` deltaP `4.428` edge `0.02` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.6343` n `140` status `ready` deltaP `8.7979` edge `0.0866` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.7242` n `152` status `ready` deltaP `4.5225` edge `0.1033` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
