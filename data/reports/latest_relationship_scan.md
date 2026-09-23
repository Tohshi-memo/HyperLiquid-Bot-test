# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T18:52:43.153560+00:00`
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

- `market_context_high->unknown_1h` score `82.8607` n `47` status `ready` deltaP `9.8166` edge `6.8467` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `32.6159` n `46` status `ready` deltaP `18.5689` edge `2.6098` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.4748` n `46` status `ready` deltaP `15.9647` edge `1.4432` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.3609` n `46` status `ready` deltaP `13.5417` edge `1.1898` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `7.9223` n `96` status `ready` deltaP `-4.1666` edge `1.3738` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.2569` n `46` status `ready` deltaP `24.9925` edge `0.3635` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.3572` n `103` status `ready` deltaP `16.6706` edge `0.3097` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.9842` n `103` status `ready` deltaP `11.7926` edge `0.3532` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `2.9777` n `96` status `ready` deltaP `27.6042` edge `0.182` maxDD `-2.431`
- `news_risk_high->crypto_alt_24h` score `2.47` n `96` status `ready` deltaP `-6.25` edge `0.7356` maxDD `-32.7147`
- `news_risk_high->crypto_alt_1h` score `2.3435` n `103` status `ready` deltaP `12.4092` edge `0.1616` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.2671` n `47` status `ready` deltaP `27.319` edge `0.0222` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0217` n `103` status `ready` deltaP `15.8523` edge `0.1063` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3797` n `103` status `ready` deltaP `20.785` edge `0.04` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2112` n `96` status `ready` deltaP `28.8194` edge `0.1221` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.8529` n `46` status `ready` deltaP `18.9689` edge `-0.032` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.7922` n `47` status `ready` deltaP `7.9981` edge `0.0545` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6396` n `47` status `ready` deltaP `11.167` edge `0.0067` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5643` n `103` status `ready` deltaP `14.6038` edge `0.009` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.3853` n `96` status `ready` deltaP `15.7986` edge `0.0285` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
