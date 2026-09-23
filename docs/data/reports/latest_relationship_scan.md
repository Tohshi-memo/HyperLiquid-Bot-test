# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T19:37:28.319902+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9883`

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

- `market_context_high->unknown_1h` score `82.8343` n `47` status `ready` deltaP `9.8166` edge `6.8445` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `33.0007` n `46` status `ready` deltaP `19.0897` edge `2.6384` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.8009` n `46` status `ready` deltaP `16.4855` edge `1.4669` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.8838` n `46` status `ready` deltaP `14.0625` edge `1.2299` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.3072` n `96` status `ready` deltaP `-3.6458` edge `1.4024` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.3586` n `46` status `ready` deltaP `25.5133` edge `0.3685` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.4344` n `103` status `ready` deltaP `16.9755` edge `0.3141` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.1454` n `103` status `ready` deltaP `12.0975` edge `0.3646` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `2.9929` n `96` status `ready` deltaP `-5.7292` edge `0.7757` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.888` n `96` status `ready` deltaP `27.0833` edge `0.178` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.3903` n `103` status `ready` deltaP `12.5589` edge `0.1645` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.3193` n `47` status `ready` deltaP `27.7763` edge `0.0235` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0397` n `103` status `ready` deltaP `15.8523` edge `0.1078` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4186` n `103` status `ready` deltaP `21.2423` edge `0.0402` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2406` n `96` status `ready` deltaP `29.3403` edge `0.1224` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.9906` n `46` status `ready` deltaP `19.4898` edge `-0.024` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.9212` n `47` status `ready` deltaP `8.4555` edge `0.0622` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6588` n `47` status `ready` deltaP `11.3167` edge `0.0073` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.593` n `103` status `ready` deltaP `14.9032` edge `0.0094` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.4748` n `96` status `ready` deltaP `16.3195` edge `0.0365` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
