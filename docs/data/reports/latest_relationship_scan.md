# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T13:22:32.758251+00:00`
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

- `market_context_high->unknown_24h` score `4406.1629` n `102` status `ready` deltaP `13.4906` edge `367.0955` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `1350.2101` n `55` status `ready` deltaP `15.4514` edge `112.4145` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1350.2101` n `55` status `ready` deltaP `15.4514` edge `112.4145` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.2934` n `82` status `ready` deltaP `-4.6517` edge `32.0143` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.5241` n `59` status `ready` deltaP `54.6786` edge `1.7692` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `18.565` n `55` status `ready` deltaP `39.5202` edge `1.3066` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.565` n `55` status `ready` deltaP `39.5202` edge `1.3066` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.5942` n `59` status `ready` deltaP `29.967` edge `1.3152` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.9331` n `102` status `ready` deltaP `32.9248` edge `1.191` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.3987` n `59` status `ready` deltaP `34.631` edge `0.8122` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.9313` n `55` status `ready` deltaP `38.0208` edge `0.4908` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9313` n `55` status `ready` deltaP `38.0208` edge `0.4908` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7423` n `55` status `ready` deltaP `42.8687` edge `0.4799` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7423` n `55` status `ready` deltaP `42.8687` edge `0.4799` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.6721` n `102` status `ready` deltaP `38.0208` edge `0.4692` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.4361` n `59` status `ready` deltaP `54.1667` edge `0.3419` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9371` n `59` status `ready` deltaP `51.8185` edge `0.3253` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8895` n `55` status `ready` deltaP `49.7538` edge `0.08` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8895` n `55` status `ready` deltaP `49.7538` edge `0.08` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.2165` n `55` status `ready` deltaP `37.5444` edge `0.1104` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
