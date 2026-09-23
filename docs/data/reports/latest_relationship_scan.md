# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T22:37:32.864596+00:00`
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

- `market_context_high->unknown_1h` score `72.1435` n `47` status `ready` deltaP `10.116` edge `5.9516` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `34.4826` n `46` status `ready` deltaP `21.173` edge `2.748` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.9612` n `46` status `ready` deltaP `18.5689` edge `1.5497` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `17.9705` n `46` status `ready` deltaP `16.1458` edge `1.3899` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.8265` n `97` status `ready` deltaP `-2.3143` edge `1.4368` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.7244` n `46` status `ready` deltaP `27.5966` edge `0.3851` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.7092` n `103` status `ready` deltaP `13.7743` edge `0.4004` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5478` n `103` status `ready` deltaP `17.4328` edge `0.3205` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `4.0798` n `97` status `ready` deltaP `-4.4728` edge `0.8579` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.6136` n `97` status `ready` deltaP `25.2577` edge `0.1673` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.4778` n `103` status `ready` deltaP `13.1577` edge `0.1678` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.415` n `47` status `ready` deltaP `28.5385` edge `0.0264` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9533` n `103` status `ready` deltaP `15.4032` edge `0.1036` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.521` n `103` status `ready` deltaP `22.4618` edge `0.0406` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.5028` n `46` status `ready` deltaP `21.5731` edge `0.0048` maxDD `-0.2042`
- `market_context_high->equity_4h` score `1.2545` n `47` status `ready` deltaP `10.1323` edge `0.0788` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1086` n `97` status `ready` deltaP `27.6221` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7235` n `47` status `ready` deltaP `12.0652` edge `0.0077` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.6388` n `97` status `ready` deltaP `17.651` edge `0.056` maxDD `-3.0086`
- `news_risk_high->metal_1h` score `0.5691` n `103` status `ready` deltaP `14.6038` edge `0.0094` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
