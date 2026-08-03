# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T01:22:32.962426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `4786.4734` n `57` status `ready` deltaP `23.3644` edge `398.7591` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.5731` n `40` status `ready` deltaP `51.4583` edge `0.9111` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.2314` n `40` status `ready` deltaP `51.3194` edge `0.6066` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.2617` n `57` status `ready` deltaP `12.016` edge `0.3514` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7176` n `57` status `ready` deltaP `16.3644` edge `0.0721` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9572` n `41` status `ready` deltaP `12.6525` edge `0.123` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.8148` n `57` status `ready` deltaP `10.1219` edge `0.0827` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.7228` n `41` status `ready` deltaP `7.7744` edge `0.1314` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6336` n `41` status `ready` deltaP `19.9696` edge `0.0277` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.3572` n `47` status `ready` deltaP `7.4149` edge `0.0338` maxDD `-1.3282`
- `news_risk_high->metal_4h` score `0.1773` n `57` status `ready` deltaP `6.0654` edge `0.0174` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.1128` n `57` status `ready` deltaP `5.4995` edge `0.0101` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0014` n `47` status `ready` deltaP `7.1155` edge `-0.0087` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.0466` n `57` status `ready` deltaP `6.7392` edge `0.0173` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.1711` n `57` status `ready` deltaP `0.9192` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.1732` n `57` status `ready` deltaP `7.7316` edge `0.022` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.2808` n `57` status `ready` deltaP `3.6795` edge `0.0115` maxDD `-3.762`
- `news_risk_high->metal_1h` score `-0.3071` n `57` status `ready` deltaP `-0.021` edge `0.0011` maxDD `-0.5599`
- `market_context_high->fx_24h` score `-0.7355` n `40` status `ready` deltaP `0.6597` edge `0.0323` maxDD `-2.506`
- `news_risk_high->commodity_1h` score `-0.7939` n `57` status `ready` deltaP `2.973` edge `-0.0182` maxDD `-2.0891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
