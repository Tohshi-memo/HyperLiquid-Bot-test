# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T20:37:31.691389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11136`

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

- `news_risk_high->unknown_24h` score `300.1089` n `71` status `ready` deltaP `-1.0613` edge `25.0206` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.6442` n `47` status `ready` deltaP `7.8704` edge `5.7583` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.5813` n `47` status `ready` deltaP `30.9434` edge `4.0481` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.02` n `47` status `ready` deltaP `24.782` edge `2.5411` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3479` n `47` status `ready` deltaP `34.5892` edge `1.9173` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6792` n `47` status `ready` deltaP `34.5892` edge `0.4223` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9814` n `47` status `ready` deltaP `33.8431` edge `0.13` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7581` n `47` status `ready` deltaP `17.6018` edge `0.1543` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.653` n `47` status `ready` deltaP `30.6727` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4269` n `47` status `ready` deltaP `11.5172` edge `0.1089` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.132` n `47` status `ready` deltaP `12.9634` edge `0.0482` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.9064` n `111` status `ready` deltaP `9.179` edge `0.1054` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8661` n `47` status `ready` deltaP `13.5622` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5093` n `47` status `ready` deltaP `10.5586` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.366` n `47` status `ready` deltaP `4.5375` edge `0.0907` maxDD `-5.2359`
- `news_risk_high->metal_24h` score `0.3091` n `71` status `ready` deltaP `19.9384` edge `0.0728` maxDD `-6.9545`
- `market_context_high->crypto_major_1h` score `0.2871` n `47` status `ready` deltaP `4.9019` edge `0.073` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `0.0807` n `111` status `ready` deltaP `3.7628` edge `0.036` maxDD `-2.0595`
- `news_risk_high->crypto_major_1h` score `0.0663` n `111` status `ready` deltaP `4.2119` edge `0.053` maxDD `-3.3776`
- `market_context_high->fx_4h` score `0.0469` n `47` status `ready` deltaP `9.4739` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
