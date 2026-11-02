# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T06:37:34.833117+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5157`

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

- `market_context_high->unknown_24h` score `6496.1947` n `36` status `ready` deltaP `1.3889` edge `541.3403` maxDD `0.0`
- `market_context_high->unknown_4h` score `546.8477` n `41` status `ready` deltaP `8.8415` edge `45.5117` maxDD `0.0`
- `market_context_high->unknown_1h` score `130.0087` n `41` status `ready` deltaP `8.1021` edge `10.7911` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.2424` n `36` status `ready` deltaP `41.8403` edge `1.3482` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2957` n `96` status `ready` deltaP `32.6389` edge `1.026` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `7.2231` n `36` status `ready` deltaP `43.5764` edge `0.3425` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.735` n `36` status `ready` deltaP `49.1319` edge `0.2337` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.3736` n `41` status `ready` deltaP `26.8292` edge `0.3817` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.5994` n `41` status `ready` deltaP `11.433` edge `0.4606` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `5.0299` n `41` status `ready` deltaP `25.1525` edge `0.2851` maxDD `-1.6901`
- `market_context_high->equity_1h` score `2.6972` n `41` status `ready` deltaP `7.9378` edge `0.2119` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.3967` n `126` status `ready` deltaP `9.7754` edge `0.2732` maxDD `-7.4246`
- `market_context_high->crypto_alt_1h` score `1.9211` n `41` status `ready` deltaP `6.397` edge `0.1616` maxDD `-1.5324`
- `market_context_high->crypto_alt_24h` score `1.8444` n `36` status `ready` deltaP `-7.2917` edge `0.3541` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.8431` n `41` status `ready` deltaP `21.3415` edge `0.0538` maxDD `-0.7323`
- `market_context_high->crypto_major_1h` score `1.7016` n `41` status `ready` deltaP `8.2372` edge `0.1261` maxDD `-1.1375`
- `market_context_high->index_4h` score `1.4401` n `41` status `ready` deltaP `16.1585` edge `0.0447` maxDD `-0.9265`
- `market_context_high->commodity_4h` score `1.2937` n `41` status `ready` deltaP `24.3902` edge `0.0445` maxDD `-1.633`
- `market_context_high->fx_1h` score `1.1741` n `41` status `ready` deltaP `15.704` edge `0.0103` maxDD `-0.0388`
- `market_context_high->metal_1h` score `0.5917` n `41` status `ready` deltaP `11.9797` edge `0.0217` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
