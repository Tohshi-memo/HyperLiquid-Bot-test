# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T00:52:26.626834+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.3657` n `154` status `ready` deltaP `15.6755` edge `0.0766` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8015` n `166` status `ready` deltaP `10.5584` edge `0.0307` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4306` n `133` status `ready` deltaP `18.19` edge `0.0206` maxDD `-1.9329`
- `market_context_high->fx_1h` score `-0.2702` n `166` status `ready` deltaP `2.5666` edge `-0.0022` maxDD `-0.9639`
- `market_context_high->metal_24h` score `-0.3158` n `133` status `ready` deltaP `-0.5078` edge `0.0555` maxDD `-2.2743`
- `market_context_high->equity_24h` score `-0.4975` n `133` status `ready` deltaP `1.3993` edge `0.2552` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.526` n `133` status `ready` deltaP `2.0416` edge `0.0957` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5945` n `166` status `ready` deltaP `-3.4359` edge `-0.0056` maxDD `-0.8168`
- `market_context_high->fx_4h` score `-0.6018` n `154` status `ready` deltaP `3.8961` edge `-0.0008` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7549` n `166` status `ready` deltaP `-4.4838` edge `-0.0096` maxDD `-1.5832`
- `market_context_high->equity_1h` score `-0.7784` n `166` status `ready` deltaP `-1.735` edge `-0.0012` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.7828` n `154` status `ready` deltaP `-3.6921` edge `-0.0109` maxDD `-1.1876`
- `market_context_high->metal_4h` score `-1.3678` n `154` status `ready` deltaP `-4.6345` edge `-0.0265` maxDD `-4.1033`
- `market_context_high->crypto_alt_1h` score `-1.584` n `166` status `ready` deltaP `-8.9928` edge `-0.041` maxDD `-5.5029`
- `market_context_high->equity_4h` score `-1.9585` n `154` status `ready` deltaP `-4.5949` edge `-0.0784` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.7092` n `166` status `ready` deltaP `-10.6828` edge `-0.0645` maxDD `-10.5372`
- `market_context_high->crypto_major_24h` score `-4.5291` n `133` status `ready` deltaP `-0.3302` edge `-0.1258` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.5839` n `133` status `ready` deltaP `-12.1933` edge `-0.1564` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-5.1325` n `154` status `ready` deltaP `-10.8688` edge `-0.1444` maxDD `-10.2014`
- `market_context_high->unknown_1h` score `-7.5122` n `166` status `ready` deltaP `-4.3666` edge `-0.5512` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
