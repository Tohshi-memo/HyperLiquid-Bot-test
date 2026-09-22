# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T00:07:23.989592+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9940`

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

- `market_context_high->unknown_4h` score `31.9274` n `55` status `ready` deltaP `3.9856` edge `2.6417` maxDD `-0.2787`
- `market_context_high->crypto_major_24h` score `13.3004` n `51` status `ready` deltaP `8.4661` edge `1.555` maxDD `-36.5794`
- `news_risk_high->crypto_major_24h` score `11.2642` n `101` status `ready` deltaP `0.3317` edge `1.6223` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `6.6897` n `101` status `ready` deltaP `0.7168` edge `1.0408` maxDD `-32.7147`
- `market_context_high->equity_24h` score `6.6456` n `51` status `ready` deltaP `1.6953` edge `0.761` maxDD `-13.8137`
- `news_risk_high->crypto_alt_4h` score `3.144` n `101` status `ready` deltaP `15.2605` edge `0.2812` maxDD `-7.675`
- `market_context_high->index_24h` score `2.6543` n `51` status `ready` deltaP `5.6883` edge `0.2466` maxDD `-1.3995`
- `news_risk_high->commodity_24h` score `2.4897` n `101` status `ready` deltaP `30.8357` edge `0.2442` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3841` n `101` status `ready` deltaP `14.5847` edge `0.148` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1742` n `101` status `ready` deltaP `16.48` edge `0.1971` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.6276` n `101` status `ready` deltaP `15.932` edge `0.0817` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `0.4972` n `101` status `ready` deltaP `11.6895` edge `0.0271` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.4244` n `101` status `ready` deltaP `12.6519` edge `0.0112` maxDD `-0.8144`
- `market_context_high->equity_1h` score `0.337` n `55` status `ready` deltaP `2.2374` edge `0.0385` maxDD `-0.36`
- `market_context_high->fx_1h` score `0.3328` n `55` status `ready` deltaP `8.6527` edge `0.0057` maxDD `-0.1854`
- `market_context_high->index_1h` score `0.3116` n `55` status `ready` deltaP `6.3011` edge `0.0095` maxDD `-0.0435`
- `market_context_high->metal_1h` score `0.2733` n `55` status `ready` deltaP `5.4872` edge `0.017` maxDD `-0.1314`
- `market_context_high->metal_24h` score `0.2281` n `51` status `ready` deltaP `17.0241` edge `-0.0711` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.1955` n `101` status `ready` deltaP `13.4403` edge `0.0321` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.0213` n `55` status `ready` deltaP `10.0526` edge `-0.0006` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
