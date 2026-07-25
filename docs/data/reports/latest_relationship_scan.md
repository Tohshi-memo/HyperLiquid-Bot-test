# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T03:22:32.858813+00:00`
- Price records: `672`
- Market context records: `7839`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `10.0314` n `132` status `ready` deltaP `28.5507` edge `0.7798` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3567` n `133` status `ready` deltaP `5.9449` edge `0.3256` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.1699` n `133` status `ready` deltaP `10.7648` edge `0.2348` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.1065` n `133` status `ready` deltaP `13.4573` edge `0.0466` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.1003` n `133` status `ready` deltaP `13.8891` edge `0.1709` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `0.8942` n `132` status `ready` deltaP `19.2095` edge `0.1048` maxDD `-7.0012`
- `market_context_high->fx_24h` score `0.8296` n `132` status `ready` deltaP `25.2187` edge `0.047` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7574` n `133` status `ready` deltaP `8.1961` edge `0.0944` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.7322` n `133` status `ready` deltaP `7.8947` edge `0.1201` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.4625` n `133` status `ready` deltaP `8.6098` edge `0.0405` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3626` n `133` status `ready` deltaP `8.4943` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2803` n `133` status `ready` deltaP `5.1765` edge `0.0321` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.099` n `133` status `ready` deltaP `6.0975` edge `0.0135` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0658` n `133` status `ready` deltaP `12.8521` edge `0.0517` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3726` n `133` status `ready` deltaP `1.1245` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8375` n `133` status `ready` deltaP `1.5668` edge `0.0201` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.237` n `132` status `ready` deltaP `-5.3136` edge `0.0871` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.3993` n `133` status `ready` deltaP `1.7479` edge `0.0772` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4318` n `133` status `ready` deltaP `-3.2443` edge `0.0009` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-2.0154` n `133` status `ready` deltaP `14.9164` edge `0.1717` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
