# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T13:37:28.553046+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12058`

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

- `market_context_high->unknown_24h` score `4578.5054` n `101` status `ready` deltaP `13.4712` edge `381.4575` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `1616.1289` n `54` status `ready` deltaP `15.4514` edge `134.5744` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1616.1289` n `54` status `ready` deltaP `15.4514` edge `134.5744` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.2922` n `82` status `ready` deltaP `-4.6517` edge `32.0142` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.5337` n `59` status `ready` deltaP `54.6786` edge `1.77` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `18.344` n `54` status `ready` deltaP `39.3518` edge `1.2893` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.344` n `54` status `ready` deltaP `39.3518` edge `1.2893` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.6026` n `59` status `ready` deltaP `29.967` edge `1.3159` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.7995` n `101` status `ready` deltaP `32.7695` edge `1.1809` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.4059` n `59` status `ready` deltaP `34.631` edge `0.8128` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.9373` n `54` status `ready` deltaP `38.0208` edge `0.4913` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9373` n `54` status `ready` deltaP `38.0208` edge `0.4913` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7534` n `54` status `ready` deltaP `42.7676` edge `0.4815` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7534` n `54` status `ready` deltaP `42.7676` edge `0.4815` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.6757` n `101` status `ready` deltaP `38.0208` edge `0.4695` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.456` n `59` status `ready` deltaP `54.3403` edge `0.3424` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9383` n `59` status `ready` deltaP `51.8185` edge `0.3254` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8791` n `54` status `ready` deltaP `49.6527` edge `0.0798` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8791` n `54` status `ready` deltaP `49.6527` edge `0.0798` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.2045` n `54` status `ready` deltaP `37.4097` edge `0.1103` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
