# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T21:22:18.007212+00:00`
- Price records: `672`
- Market context records: `1257`
- Flow alert records: `5526`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_major_24h` score `17.9533` n `128` status `ready` deltaP `41.5798` edge `1.3321` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.7412` n `128` status `ready` deltaP `3.4722` edge `0.872` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `8.0143` n `128` status `ready` deltaP `5.221` edge `0.7547` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.7948` n `128` status `ready` deltaP `22.8298` edge `0.699` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.3243` n `128` status `ready` deltaP `24.4792` edge `0.3058` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.4142` n `128` status `ready` deltaP `18.0068` edge `0.2308` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.3616` n `128` status `ready` deltaP `22.5694` edge `0.5132` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.9594` n `128` status `ready` deltaP `-9.7222` edge `0.4596` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.1858` n `128` status `ready` deltaP `1.5625` edge `0.4447` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5759` n `128` status `ready` deltaP `14.0434` edge `0.106` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.8278` n `128` status `ready` deltaP `11.2463` edge `0.0257` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7788` n `128` status `ready` deltaP `7.1061` edge `0.0544` maxDD `-1.2834`
- `market_context_high->metal_4h` score `0.4881` n `128` status `ready` deltaP `16.8255` edge `0.0716` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.3912` n `128` status `ready` deltaP `11.9152` edge `0.0142` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.2061` n `128` status `ready` deltaP `4.7744` edge `0.0318` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `0.0854` n `128` status `ready` deltaP `7.3743` edge `0.1539` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1157` n `128` status `ready` deltaP `5.5998` edge `-0.0014` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2814` n `128` status `ready` deltaP `0.945` edge `0.0419` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4159` n `128` status `ready` deltaP `2.2268` edge `0.0084` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.5425` n `128` status `ready` deltaP `8.5556` edge `0.1699` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
