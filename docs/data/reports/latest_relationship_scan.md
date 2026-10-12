# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T11:37:27.162751+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `25.7263` n `42` status `ready` deltaP `28.1746` edge `2.0591` maxDD `-5.5788`
- `market_context_high->crypto_major_24h` score `25.397` n `42` status `ready` deltaP `39.8066` edge `1.9271` maxDD `-3.4184`
- `market_context_high->unknown_4h` score `4.2104` n `107` status `ready` deltaP `-4.2299` edge `0.4437` maxDD `-1.8373`
- `risk_on_high->crypto_alt_4h` score `3.8436` n `48` status `ready` deltaP `18.1911` edge `0.2438` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.8436` n `48` status `ready` deltaP `18.1911` edge `0.2438` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4589` n `48` status `ready` deltaP `32.6728` edge `0.3109` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4589` n `48` status `ready` deltaP `32.6728` edge `0.3109` maxDD `-4.1548`
- `market_context_high->metal_24h` score `2.3861` n `42` status `ready` deltaP `23.4871` edge `0.0834` maxDD `-0.9576`
- `market_context_high->crypto_major_4h` score `2.3467` n `107` status `ready` deltaP `15.1883` edge `0.2721` maxDD `-8.5569`
- `market_context_high->crypto_alt_4h` score `1.7841` n `107` status `ready` deltaP `8.8258` edge `0.2795` maxDD `-11.5067`
- `market_context_high->crypto_alt_1h` score `1.3235` n `107` status `ready` deltaP `10.8568` edge `0.133` maxDD `-4.9401`
- `market_context_high->equity_24h` score `1.2957` n `42` status `ready` deltaP `-4.4891` edge `0.3765` maxDD `-10.1034`
- `market_context_high->index_24h` score `1.1822` n `42` status `ready` deltaP `19.1965` edge `0.0919` maxDD `-0.7988`
- `risk_on_high->crypto_alt_1h` score `0.8208` n `48` status `ready` deltaP `5.6387` edge `0.0905` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8208` n `48` status `ready` deltaP `5.6387` edge `0.0905` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.5618` n `107` status `ready` deltaP `4.505` edge `0.0931` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.322` n `48` status `ready` deltaP `4.4661` edge `0.0768` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.322` n `48` status `ready` deltaP `4.4661` edge `0.0768` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.0587` n `107` status `ready` deltaP `3.4571` edge `0.0025` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1196` n `107` status `ready` deltaP `5.662` edge `0.003` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
