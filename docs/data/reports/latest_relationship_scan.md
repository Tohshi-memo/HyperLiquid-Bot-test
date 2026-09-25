# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T09:22:30.430738+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11206`

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

- `market_context_high->unknown_1h` score `84.8409` n `47` status `ready` deltaP `8.4693` edge `7.0207` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2069` n `47` status `ready` deltaP `30.9434` edge `4.0169` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.2408` n `47` status `ready` deltaP `24.782` edge `2.5595` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.7127` n `47` status `ready` deltaP `34.5892` edge `1.9477` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.4309` n `111` status `ready` deltaP `3.7156` edge `0.9417` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.9554` n `47` status `ready` deltaP `36.1517` edge `0.4349` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6539` n `47` status `ready` deltaP `39.3987` edge `0.149` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6605` n `47` status `ready` deltaP `30.2489` edge `0.1382` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.7467` n `47` status `ready` deltaP `31.7397` edge `0.0327` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.2358` n `47` status `ready` deltaP `15.4677` edge `0.125` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.0332` n `47` status `ready` deltaP `9.5355` edge `0.0893` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.8935` n `47` status `ready` deltaP `11.167` edge `0.0403` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8912` n `47` status `ready` deltaP `13.8616` edge `0.0097` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.7362` n `111` status `ready` deltaP `7.9814` edge `0.0992` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4841` n `47` status `ready` deltaP `10.2592` edge `0.0076` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0219` n `47` status `ready` deltaP `3.4272` edge `0.0116` maxDD `-0.1976`
- `news_risk_high->index_1h` score `0.0136` n `111` status `ready` deltaP `3.7601` edge `0.0065` maxDD `-0.3863`
- `news_risk_high->metal_1h` score `0.0112` n `111` status `ready` deltaP `8.5451` edge `0.0069` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0547` n `47` status `ready` deltaP `3.2552` edge `0.0555` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.0744` n `111` status `ready` deltaP `1.9664` edge `0.0281` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
