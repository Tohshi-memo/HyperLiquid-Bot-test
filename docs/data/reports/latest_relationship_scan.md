# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T16:37:26.208655+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7457`

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

- `market_context_high->unknown_24h` score `2613.2204` n `105` status `ready` deltaP `-8.378` edge `217.8672` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `77.1738` n `108` status `ready` deltaP `-6.2431` edge `6.5014` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `66.9853` n `105` status `ready` deltaP `1.2601` edge `5.587` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.208` n `60` status `ready` deltaP `45.2778` edge `1.2206` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.2955` n `105` status `ready` deltaP `27.4058` edge `1.0343` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.9232` n `105` status `ready` deltaP `44.127` edge `0.1344` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.6783` n `100` status `ready` deltaP `17.0549` edge `0.4148` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.8202` n `105` status `ready` deltaP `22.4201` edge `0.0447` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.4088` n `105` status `ready` deltaP `8.2854` edge `0.2015` maxDD `-4.48`
- `market_context_high->metal_1h` score `0.9515` n `105` status `ready` deltaP `13.4559` edge `0.0186` maxDD `-0.3209`
- `market_context_high->crypto_major_1h` score `0.7466` n `105` status `ready` deltaP `10.8569` edge `0.0926` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.6763` n `105` status `ready` deltaP `6.8435` edge `0.0983` maxDD `-2.3383`
- `news_risk_high->crypto_alt_1h` score `0.5951` n `108` status `ready` deltaP `7.5294` edge `0.0948` maxDD `-3.9659`
- `market_context_high->crypto_major_4h` score `0.3406` n `105` status `ready` deltaP `18.0749` edge `0.1819` maxDD `-14.5879`
- `market_context_high->metal_24h` score `0.2211` n `105` status `ready` deltaP `15.3968` edge `0.1904` maxDD `-10.5088`
- `market_context_high->fx_1h` score `0.1906` n `105` status `ready` deltaP `7.7545` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.1258` n `105` status `ready` deltaP `7.4085` edge `0.0002` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `-0.0062` n `105` status `ready` deltaP `10.0784` edge `0.0539` maxDD `-1.0837`
- `market_context_high->index_1h` score `-0.2755` n `105` status `ready` deltaP `4.5438` edge `0.0026` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4746` n `105` status `ready` deltaP `-0.3935` edge `0.0145` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
