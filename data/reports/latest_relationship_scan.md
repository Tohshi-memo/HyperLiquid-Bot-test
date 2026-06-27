# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T03:37:29.870044+00:00`
- Price records: `672`
- Market context records: `4894`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8584`

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

- `market_context_high->unknown_1h` score `15.3667` n `110` status `ready` deltaP `9.5727` edge `1.2585` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5532` n `110` status `ready` deltaP `23.3148` edge `0.6938` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5002` n `110` status `ready` deltaP `21.3609` edge `0.5345` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4082` n `110` status `ready` deltaP `18.9495` edge `0.5301` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2648` n `91` status `ready` deltaP `24.2541` edge `0.3113` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1077` n `110` status `ready` deltaP `7.9102` edge `0.1058` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8945` n `110` status `ready` deltaP `12.439` edge `0.1699` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5731` n `110` status `ready` deltaP `11.8403` edge `0.0408` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4555` n `110` status `ready` deltaP `6.4698` edge `0.1191` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4097` n `110` status `ready` deltaP `8.1709` edge `0.1003` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1973` n `110` status `ready` deltaP `3.9358` edge `0.0588` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.2137` n `110` status `ready` deltaP `3.4322` edge `0.0157` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2344` n `110` status `ready` deltaP `-0.3539` edge `0.0303` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5328` n `110` status `ready` deltaP `-0.5879` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7114` n `110` status `ready` deltaP `0.3049` edge `0.0038` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.8634` n `110` status `ready` deltaP `6.2721` edge `0.0049` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3597` n `110` status `ready` deltaP `-7.1666` edge `-0.0042` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.6232` n `91` status `ready` deltaP `-3.9053` edge `-0.0082` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5447` n `91` status `ready` deltaP `-5.2351` edge `-0.1392` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.685` n `91` status `ready` deltaP `15.7146` edge `0.0157` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
