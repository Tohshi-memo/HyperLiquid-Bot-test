# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T02:22:18.289872+00:00`
- Price records: `672`
- Market context records: `1691`
- Flow alert records: `6776`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `7.0478` n `144` status `ready` deltaP `26.0573` edge `0.6562` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `6.2997` n `144` status `ready` deltaP `17.5822` edge `0.9398` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `5.3112` n `192` status `ready` deltaP `22.8024` edge `0.557` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.9623` n `192` status `ready` deltaP `22.1671` edge `0.4533` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.8771` n `144` status `ready` deltaP `17.3995` edge `0.3449` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9667` n `192` status `ready` deltaP `15.7012` edge `0.252` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.898` n `144` status `ready` deltaP `16.3518` edge `0.539` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.6774` n `200` status `ready` deltaP `6.5569` edge `0.1151` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4092` n `144` status `ready` deltaP `24.3464` edge `1.0527` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.2975` n `192` status `ready` deltaP `6.9741` edge `0.0872` maxDD `-3.7119`
- `market_context_high->equity_1h` score `0.0176` n `200` status `ready` deltaP `4.6677` edge `0.0512` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.1241` n `200` status `ready` deltaP `4.0539` edge `0.0808` maxDD `-4.7865`
- `market_context_high->index_1h` score `-0.523` n `200` status `ready` deltaP `0.5689` edge `0.0158` maxDD `-1.7205`
- `market_context_high->crypto_major_24h` score `-0.5288` n `144` status `ready` deltaP `22.7677` edge `0.639` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.5849` n `200` status `ready` deltaP `6.2545` edge `0.0169` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5878` n `192` status `ready` deltaP `12.0299` edge `0.14` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6581` n `200` status `ready` deltaP `-2.7964` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7769` n `144` status `ready` deltaP `4.9596` edge `0.0071` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.7044` n `192` status `ready` deltaP `-5.8562` edge `-0.0101` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1064` n `200` status `ready` deltaP `0.7036` edge `-0.0293` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
