# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T03:37:27.814347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8030`

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

- `market_context_high->unknown_24h` score `7347.2275` n `46` status `ready` deltaP `1.3889` edge `612.2597` maxDD `0.0`
- `market_context_high->unknown_4h` score `434.6122` n `47` status `ready` deltaP `7.1711` edge `36.1742` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `52.8394` n `51` status `ready` deltaP `5.6153` edge `4.3769` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.6783` n `46` status `ready` deltaP `42.4442` edge `1.3805` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.7335` n `94` status `ready` deltaP `33.566` edge `1.0563` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.7103` n `46` status `ready` deltaP `45.1162` edge `0.2895` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.335` n `47` status `ready` deltaP `26.2714` edge `0.3822` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.3246` n `46` status `ready` deltaP `49.1319` edge `0.1995` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.2613` n `47` status `ready` deltaP `29.3202` edge `0.2766` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.6557` n `47` status `ready` deltaP `34.4966` edge `0.0914` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.222` n `47` status `ready` deltaP `1.9654` edge `0.3256` maxDD `-2.283`
- `market_context_high->equity_1h` score `2.3211` n `51` status `ready` deltaP `8.2247` edge `0.1911` maxDD `-1.5336`
- `news_risk_high->crypto_alt_4h` score `2.2736` n `126` status `ready` deltaP `9.1657` edge `0.267` maxDD `-7.4246`
- `market_context_high->crypto_alt_1h` score `1.9983` n `51` status `ready` deltaP `6.713` edge `0.183` maxDD `-2.2314`
- `market_context_high->crypto_major_1h` score `1.8401` n `51` status `ready` deltaP `8.075` edge `0.1504` maxDD `-1.4048`
- `market_context_high->crypto_alt_24h` score `1.4576` n `46` status `ready` deltaP `-6.952` edge `0.385` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.4328` n `47` status `ready` deltaP `17.0375` edge `0.0483` maxDD `-0.7323`
- `market_context_high->crypto_major_24h` score `1.3236` n `46` status `ready` deltaP `3.7439` edge `0.2124` maxDD `-3.0799`
- `market_context_high->fx_1h` score `1.3105` n `51` status `ready` deltaP `17.7293` edge `0.0086` maxDD `-0.0736`
- `market_context_high->metal_1h` score `0.6099` n `51` status `ready` deltaP `8.9439` edge `0.0169` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
