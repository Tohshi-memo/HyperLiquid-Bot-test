# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T07:22:29.451918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9897`

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

- `market_context_high->unknown_1h` score `66.1782` n `47` status `ready` deltaP `10.5651` edge `5.4515` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `39.9295` n `46` status `ready` deltaP `27.2494` edge `3.1614` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `24.9318` n `46` status `ready` deltaP `22.2222` edge `1.9295` maxDD `0.0`
- `market_context_high->equity_24h` score `23.1053` n `46` status `ready` deltaP `24.6453` edge `1.7712` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.6737` n `46` status `ready` deltaP `33.673` edge `0.4237` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `6.1883` n `103` status `ready` deltaP `-0.4416` edge `1.4229` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.8386` n `103` status `ready` deltaP `14.5365` edge `0.4061` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.7627` n `103` status `ready` deltaP `18.4999` edge `0.3313` maxDD `-2.619`
- `market_context_high->metal_24h` score `2.8721` n `46` status `ready` deltaP `27.6495` edge `0.0784` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.7531` n `47` status `ready` deltaP `32.0446` edge `0.0312` maxDD `-0.2323`
- `news_risk_high->crypto_alt_24h` score `2.6697` n `103` status `ready` deltaP `-3.0205` edge `0.9439` maxDD `-49.7699`
- `news_risk_high->crypto_alt_1h` score `2.2563` n `111` status `ready` deltaP `12.1892` edge `0.1558` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.0202` n `47` status `ready` deltaP `14.8579` edge `0.1111` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `1.9212` n `103` status `ready` deltaP `20.6226` edge `0.1405` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `1.8063` n `111` status `ready` deltaP `14.285` edge `0.0988` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6038` n `103` status `ready` deltaP `23.3765` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2366` n `103` status `ready` deltaP `29.6639` edge `0.1239` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8876` n `47` status `ready` deltaP `13.8616` edge `0.0094` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.7713` n `47` status `ready` deltaP `10.1191` edge `0.0371` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.5337` n `103` status `ready` deltaP `19.5237` edge `0.0831` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
