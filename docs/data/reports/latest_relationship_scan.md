# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T10:52:34.548435+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7605`

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

- `market_context_high->unknown_24h` score `2024.5255` n `120` status `ready` deltaP `-6.3542` edge `168.7958` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `102.3018` n `98` status `ready` deltaP `-5.3433` edge `8.5894` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `46.9046` n `120` status `ready` deltaP `1.6362` edge `3.9111` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.2027` n `37` status `ready` deltaP `48.6862` edge `1.1971` maxDD `-0.049`
- `market_context_high->equity_24h` score `9.9013` n `120` status `ready` deltaP `24.618` edge `0.9367` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1637` n `98` status `ready` deltaP `18.638` edge `0.4447` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.4985` n `120` status `ready` deltaP `41.5625` edge `0.1161` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.966` n `120` status `ready` deltaP `13.997` edge `0.0162` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.9092` n `98` status `ready` deltaP `8.096` edge `0.1047` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.5447` n `120` status `ready` deltaP `17.1545` edge `0.0332` maxDD `-1.5519`
- `market_context_high->equity_1h` score `0.4148` n `120` status `ready` deltaP `5.4491` edge `0.0858` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3498` n `120` status `ready` deltaP `8.8673` edge `0.0728` maxDD `-5.2213`
- `market_context_high->commodity_4h` score `0.0601` n `120` status `ready` deltaP `11.6972` edge `0.0516` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.0539` n `120` status `ready` deltaP `2.1951` edge `0.1459` maxDD `-5.6228`
- `market_context_high->fx_1h` score `-0.1036` n `120` status `ready` deltaP `3.503` edge `-0.001` maxDD `-0.1842`
- `market_context_high->metal_24h` score `-0.1465` n `120` status `ready` deltaP `9.0625` edge `0.1855` maxDD `-10.5088`
- `market_context_high->commodity_1h` score `-0.3237` n `120` status `ready` deltaP `1.3273` edge `0.0156` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.3899` n `120` status `ready` deltaP `1.6565` edge `-0.0023` maxDD `-0.3654`
- `market_context_high->index_1h` score `-0.4933` n `120` status `ready` deltaP `1.986` edge `0.0015` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8457` n `120` status `ready` deltaP `2.1607` edge `0.0547` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
