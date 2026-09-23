# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T18:22:28.278243+00:00`
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

- `market_context_high->unknown_1h` score `82.5715` n `47` status `ready` deltaP `9.8166` edge `6.8226` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `32.3493` n `46` status `ready` deltaP `18.2216` edge `2.5899` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.2947` n `46` status `ready` deltaP `15.6175` edge `1.4305` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.0068` n `46` status `ready` deltaP `13.1944` edge `1.1626` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `7.6557` n `96` status `ready` deltaP `-4.5139` edge `1.3539` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.1967` n `46` status `ready` deltaP `24.6453` edge `0.3608` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.309` n `103` status `ready` deltaP `16.5182` edge `0.3067` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.8746` n `103` status `ready` deltaP `11.4877` edge `0.3461` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `3.0283` n `96` status `ready` deltaP `27.9514` edge `0.1839` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.2872` n `103` status `ready` deltaP `12.1098` edge `0.1589` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.2403` n `47` status `ready` deltaP `27.0141` edge `0.022` maxDD `-0.2323`
- `news_risk_high->crypto_alt_24h` score `2.1158` n `96` status `ready` deltaP `-6.5973` edge `0.7084` maxDD `-32.7147`
- `news_risk_high->crypto_major_1h` score `1.9749` n `103` status `ready` deltaP `15.5529` edge `0.1044` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3517` n `103` status `ready` deltaP `20.4801` edge `0.0397` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1916` n `96` status `ready` deltaP `28.4722` edge `0.1219` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.7699` n `46` status `ready` deltaP `18.6217` edge `-0.0366` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.7644` n `47` status `ready` deltaP `7.8457` edge `0.0532` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6564` n `47` status `ready` deltaP `11.3167` edge `0.0071` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5835` n `103` status `ready` deltaP `14.7535` edge `0.0096` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.3326` n `47` status `ready` deltaP `6.9754` edge `0.0215` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
