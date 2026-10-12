# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T01:52:29.592177+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9488`

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

- `market_context_high->unknown_24h` score `929.5955` n `47` status `ready` deltaP `-18.846` edge `77.6283` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `37.6132` n `112` status `ready` deltaP `-8.5366` edge `3.2619` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.4145` n `47` status `ready` deltaP `31.0247` edge `0.6206` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.0335` n `47` status `ready` deltaP `50.4765` edge `0.1706` maxDD `-0.012`
- `risk_on_high->crypto_alt_4h` score `5.0693` n `33` status `ready` deltaP `21.9466` edge `0.3209` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0693` n `33` status `ready` deltaP `21.9466` edge `0.3209` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.9738` n `33` status `ready` deltaP `27.7578` edge `0.3147` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9738` n `33` status `ready` deltaP `27.7578` edge `0.3147` maxDD `-4.1548`
- `market_context_high->crypto_major_24h` score `4.6785` n `47` status `ready` deltaP `-8.6251` edge `0.7622` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `2.9998` n `33` status `ready` deltaP `27.5684` edge `0.0894` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `2.9998` n `33` status `ready` deltaP `27.5684` edge `0.0894` maxDD `-0.1896`
- `market_context_high->fx_24h` score `1.4908` n `47` status `ready` deltaP `19.8692` edge `0.0239` maxDD `-0.2368`
- `risk_on_high->metal_1h` score `1.3217` n `45` status `ready` deltaP `16.344` edge `0.0251` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.3217` n `45` status `ready` deltaP `16.344` edge `0.0251` maxDD `-0.2466`
- `risk_on_high->crypto_major_1h` score `1.1724` n `45` status `ready` deltaP `11.6234` edge `0.0855` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.1724` n `45` status `ready` deltaP `11.6234` edge `0.0855` maxDD `-3.2233`
- `market_context_high->unknown_1h` score `0.9396` n `124` status `ready` deltaP `-3.6266` edge `0.1361` maxDD `-1.0231`
- `risk_on_high->equity_4h` score `0.7822` n `33` status `ready` deltaP `7.9962` edge `0.0851` maxDD `-1.0501`
- `risk_on_and_context->equity_4h` score `0.7822` n `33` status `ready` deltaP `7.9962` edge `0.0851` maxDD `-1.0501`
- `risk_on_high->crypto_alt_1h` score `0.7083` n `45` status `ready` deltaP `8.1803` edge `0.0918` maxDD `-2.4421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
