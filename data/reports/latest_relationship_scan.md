# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T09:52:26.092896+00:00`
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

- `risk_on_high->crypto_alt_24h` score `15.9412` n `91` status `ready` deltaP `33.0472` edge `1.1311` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.9412` n `91` status `ready` deltaP `33.0472` edge `1.1311` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `11.3525` n `201` status `ready` deltaP `24.6114` edge `0.8647` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.7496` n `91` status `ready` deltaP `39.3544` edge `0.4206` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.7496` n `91` status `ready` deltaP `39.3544` edge `0.4206` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.893` n `91` status `ready` deltaP `29.1527` edge `0.3826` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.893` n `91` status `ready` deltaP `29.1527` edge `0.3826` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.1112` n `91` status `ready` deltaP `21.896` edge `0.9161` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.1112` n `91` status `ready` deltaP `21.896` edge `0.9161` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.2109` n `91` status `ready` deltaP `33.8561` edge `0.0461` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.2109` n `91` status `ready` deltaP `33.8561` edge `0.0461` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.762` n `201` status `ready` deltaP `18.0556` edge `0.1098` maxDD `0.0`
- `market_context_high->index_24h` score `2.3392` n `201` status `ready` deltaP `28.1976` edge `0.0463` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `1.9403` n `91` status `ready` deltaP `26.0286` edge `-0.0025` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.9403` n `91` status `ready` deltaP `26.0286` edge `-0.0025` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.917` n `201` status `ready` deltaP `18.6256` edge `0.0495` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.9008` n `91` status `ready` deltaP `18.2921` edge `0.0458` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.9008` n `91` status `ready` deltaP `18.2921` edge `0.0458` maxDD `-0.0811`
- `risk_on_high->equity_24h` score `1.1564` n `91` status `ready` deltaP `18.0556` edge `-0.024` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.1564` n `91` status `ready` deltaP `18.0556` edge `-0.024` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
