# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T12:37:31.797628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `17.6372` n `91` status `ready` deltaP `34.9569` edge `1.2597` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.6372` n `91` status `ready` deltaP `34.9569` edge `1.2597` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.0484` n `201` status `ready` deltaP `26.5211` edge `0.9933` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.2831` n `91` status `ready` deltaP `40.8788` edge `0.4549` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.2831` n `91` status `ready` deltaP `40.8788` edge `0.4549` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.6858` n `91` status `ready` deltaP `30.6771` edge `0.4385` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.6858` n `91` status `ready` deltaP `30.6771` edge `0.4385` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.2269` n `91` status `ready` deltaP `23.8057` edge `1.0464` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.2269` n `91` status `ready` deltaP `23.8057` edge `1.0464` maxDD `-24.5429`
- `market_context_high->equity_24h` score `3.672` n `201` status `ready` deltaP `19.9653` edge `0.1729` maxDD `0.0`
- `risk_on_high->index_24h` score `3.4765` n `91` status `ready` deltaP `35.7658` edge `0.0555` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.4765` n `91` status `ready` deltaP `35.7658` edge `0.0555` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6047` n `201` status `ready` deltaP `30.1073` edge `0.0557` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.3648` n `91` status `ready` deltaP `27.7054` edge `0.0217` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.3648` n `91` status `ready` deltaP `27.7054` edge `0.0217` maxDD `-0.0802`
- `risk_on_high->equity_24h` score `2.0664` n `91` status `ready` deltaP `19.9653` edge `0.0391` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.0664` n `91` status `ready` deltaP `19.9653` edge `0.0391` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.6956` n `201` status `ready` deltaP `17.584` edge `0.038` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.6795` n `91` status `ready` deltaP `17.2505` edge `0.0343` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.6795` n `91` status `ready` deltaP `17.2505` edge `0.0343` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
