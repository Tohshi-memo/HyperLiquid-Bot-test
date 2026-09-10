# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T09:22:26.159532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11876`

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

- `risk_on_high->crypto_alt_24h` score `15.6098` n `91` status `ready` deltaP `32.6999` edge `1.1058` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.6098` n `91` status `ready` deltaP `32.6999` edge `1.1058` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `11.2325` n `203` status `ready` deltaP `24.4013` edge `0.8561` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.6784` n `91` status `ready` deltaP `39.0495` edge `0.4167` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.6784` n `91` status `ready` deltaP `39.0495` edge `0.4167` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.7978` n `91` status `ready` deltaP `28.8478` edge `0.3767` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.7978` n `91` status `ready` deltaP `28.8478` edge `0.3767` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.8958` n `91` status `ready` deltaP `21.5488` edge `0.8908` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.8958` n `91` status `ready` deltaP `21.5488` edge `0.8908` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.0931` n `91` status `ready` deltaP `33.5089` edge `0.0386` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.0931` n `91` status `ready` deltaP `33.5089` edge `0.0386` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.7883` n `203` status `ready` deltaP `17.7083` edge `0.1143` maxDD `0.0`
- `market_context_high->index_24h` score `2.4648` n `203` status `ready` deltaP `27.9386` edge `0.0585` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.9303` n `91` status `ready` deltaP `18.4657` edge `0.0471` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.9303` n `91` status `ready` deltaP `18.4657` edge `0.0471` maxDD `-0.0811`
- `risk_on_high->equity_4h` score `1.9029` n `91` status `ready` deltaP `25.8761` edge `-0.0046` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.9029` n `91` status `ready` deltaP `25.8761` edge `-0.0046` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.629` n `203` status `ready` deltaP `17.8973` edge `0.0463` maxDD `-0.7226`
- `risk_on_high->equity_1h` score `1.1222` n `91` status `ready` deltaP `17.8901` edge `0.0021` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1222` n `91` status `ready` deltaP `17.8901` edge `0.0021` maxDD `-0.228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
