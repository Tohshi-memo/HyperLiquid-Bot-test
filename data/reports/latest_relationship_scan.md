# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T19:22:28.423710+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11624`

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

- `market_context_high->crypto_major_24h` score `2.7105` n `91` status `ready` deltaP `10.0294` edge `0.2798` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6713` n `91` status `ready` deltaP `19.2899` edge `0.269` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.2352` n `96` status `ready` deltaP `10.2109` edge `0.065` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.8261` n `96` status `ready` deltaP `14.5833` edge `0.0292` maxDD `-1.273`
- `market_context_high->equity_4h` score `0.8255` n `96` status `ready` deltaP `5.3607` edge `0.1219` maxDD `-2.4411`
- `market_context_high->index_1h` score `0.6695` n `96` status `ready` deltaP `12.9179` edge `0.0084` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.5658` n `96` status `ready` deltaP `8.2571` edge `0.0942` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4423` n `96` status `ready` deltaP `9.2066` edge `-0.0018` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.0592` n `96` status `ready` deltaP `8.689` edge `0.074` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0177` n `96` status `ready` deltaP `4.1729` edge `0.0094` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.0456` n `91` status `ready` deltaP `13.7821` edge `-0.0743` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.1782` n `96` status `ready` deltaP `4.1412` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.4358` n `96` status `ready` deltaP `3.0234` edge `0.009` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4397` n `96` status `ready` deltaP `-3.2685` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4626` n `96` status `ready` deltaP `1.628` edge `0.01` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.4648` n `96` status `ready` deltaP `1.8546` edge `0.0144` maxDD `-0.5728`
- `market_context_high->crypto_major_1h` score `-0.5746` n `96` status `ready` deltaP `0.2869` edge `0.0089` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8627` n `96` status `ready` deltaP `-7.2917` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1657` n `91` status `ready` deltaP `-5.7596` edge `0.0378` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.3505` n `91` status `ready` deltaP `-27.7339` edge `-0.0277` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
