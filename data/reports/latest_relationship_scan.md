# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T22:52:26.318132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9834`

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

- `market_context_high->unknown_1h` score `72.1327` n `47` status `ready` deltaP `10.116` edge `5.9507` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `34.6153` n `46` status `ready` deltaP `21.3466` edge `2.7579` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.0495` n `46` status `ready` deltaP `18.7425` edge `1.5559` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `18.162` n `46` status `ready` deltaP `16.3194` edge `1.4047` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.9592` n `97` status `ready` deltaP `-2.1407` edge `1.4467` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.7527` n `46` status `ready` deltaP `27.7703` edge `0.3863` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.7598` n `103` status `ready` deltaP `13.9267` edge `0.4036` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5658` n `103` status `ready` deltaP `17.4328` edge `0.322` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `4.2713` n `97` status `ready` deltaP `-4.2992` edge `0.8727` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.5853` n `97` status `ready` deltaP `25.0841` edge `0.1661` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.4994` n `103` status `ready` deltaP `13.1577` edge `0.1696` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4162` n `47` status `ready` deltaP `28.5385` edge `0.0265` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9653` n `103` status `ready` deltaP `15.4032` edge `0.1046` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.5455` n `46` status `ready` deltaP `21.7467` edge `0.0072` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.5332` n `103` status `ready` deltaP `22.6143` edge `0.0406` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.2775` n `47` status `ready` deltaP `10.2847` edge `0.0797` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1086` n `97` status `ready` deltaP `27.6221` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7259` n `47` status `ready` deltaP `12.0652` edge `0.0079` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.6666` n `97` status `ready` deltaP `17.8246` edge `0.0584` maxDD `-3.0086`
- `news_risk_high->metal_1h` score `0.5835` n `103` status `ready` deltaP `14.7535` edge `0.0096` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
