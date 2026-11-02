# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T03:22:26.726084+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7535`

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

- `market_context_high->unknown_24h` score `7394.1235` n `47` status `ready` deltaP `1.3889` edge `616.1677` maxDD `0.0`
- `market_context_high->unknown_4h` score `433.9486` n `47` status `ready` deltaP `7.1711` edge `36.1189` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `46.6312` n `52` status `ready` deltaP `5.8038` edge `3.8583` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.8716` n `47` status `ready` deltaP `42.4904` edge `1.3963` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.7311` n `94` status `ready` deltaP `33.566` edge `1.0561` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.6658` n `47` status `ready` deltaP `45.2201` edge `0.2851` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.3026` n `47` status `ready` deltaP `26.2714` edge `0.3795` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.2958` n `47` status `ready` deltaP `49.1319` edge `0.1971` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.1377` n `47` status `ready` deltaP `29.3202` edge `0.2663` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.9157` n `47` status `ready` deltaP `36.4718` edge `0.0999` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.9448` n `47` status `ready` deltaP `1.9654` edge `0.3025` maxDD `-2.283`
- `market_context_high->equity_1h` score `2.3833` n `52` status `ready` deltaP `9.0166` edge `0.191` maxDD `-1.5336`
- `news_risk_high->crypto_alt_4h` score `2.276` n `126` status `ready` deltaP `9.1657` edge `0.2672` maxDD `-7.4246`
- `market_context_high->crypto_major_1h` score `1.8878` n `52` status `ready` deltaP `8.8669` edge `0.1491` maxDD `-1.4048`
- `market_context_high->crypto_alt_1h` score `1.8724` n `52` status `ready` deltaP `5.7692` edge `0.1788` maxDD `-2.2314`
- `market_context_high->crypto_major_24h` score `1.4528` n `47` status `ready` deltaP `4.669` edge `0.2228` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.4203` n `47` status `ready` deltaP `-7.9233` edge `0.3867` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.4064` n `47` status `ready` deltaP `17.0375` edge `0.0461` maxDD `-0.7323`
- `market_context_high->fx_1h` score `1.3588` n `52` status `ready` deltaP `18.3326` edge `0.0086` maxDD `-0.0736`
- `market_context_high->metal_1h` score `0.5218` n `52` status `ready` deltaP `8.0378` edge `0.0156` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
