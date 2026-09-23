# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T22:23:12.182965+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9826`

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

- `market_context_high->unknown_1h` score `72.1615` n `47` status `ready` deltaP `10.116` edge `5.9531` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `34.3499` n `46` status `ready` deltaP `20.9994` edge `2.7381` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.8717` n `46` status `ready` deltaP `18.3953` edge `1.5434` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `17.7814` n `46` status `ready` deltaP `15.9722` edge `1.3753` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.6938` n `97` status `ready` deltaP `-2.4879` edge `1.4269` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.6961` n `46` status `ready` deltaP `27.423` edge `0.3839` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.661` n `103` status `ready` deltaP `13.6219` edge `0.3974` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5358` n `103` status `ready` deltaP `17.4328` edge `0.3195` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `3.8907` n `97` status `ready` deltaP `-4.6464` edge `0.8433` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.6419` n `97` status `ready` deltaP `25.4313` edge `0.1685` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.4406` n `103` status `ready` deltaP `13.008` edge `0.1657` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4138` n `47` status `ready` deltaP `28.5385` edge `0.0263` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9437` n `103` status `ready` deltaP `15.4032` edge `0.1028` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.5076` n `103` status `ready` deltaP `22.3094` edge `0.0405` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.4601` n `46` status `ready` deltaP `21.3995` edge `0.0024` maxDD `-0.2042`
- `market_context_high->equity_4h` score `1.2315` n `47` status `ready` deltaP `9.9798` edge `0.0779` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.0996` n `97` status `ready` deltaP `27.4485` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7235` n `47` status `ready` deltaP `12.0652` edge `0.0077` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.6111` n `97` status `ready` deltaP `17.4774` edge `0.0536` maxDD `-3.0086`
- `news_risk_high->metal_1h` score `0.5691` n `103` status `ready` deltaP `14.6038` edge `0.0094` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
