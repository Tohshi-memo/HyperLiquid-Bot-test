# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T15:37:32.867964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12636`

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

- `market_context_high->unknown_24h` score `6089.9542` n `93` status `ready` deltaP `13.3009` edge `507.4127` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `3443.0449` n `48` status `ready` deltaP `15.4514` edge `286.8174` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3443.0449` n `48` status `ready` deltaP `15.4514` edge `286.8174` maxDD `0.0`
- `news_risk_high->unknown_1h` score `382.9732` n `82` status `ready` deltaP `-5.5499` edge `31.9936` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `23.6815` n `61` status `ready` deltaP `53.0111` edge `1.7101` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `17.7085` n `48` status `ready` deltaP `39.5833` edge `1.2348` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.7085` n `48` status `ready` deltaP `39.5833` edge `1.2348` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.2183` n `61` status `ready` deltaP `28.6885` edge `1.2924` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.4512` n `93` status `ready` deltaP `32.7957` edge `1.1517` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `11.8229` n `61` status `ready` deltaP `32.8523` edge `0.7848` maxDD `-0.8192`
- `risk_on_high->equity_24h` score `9.2524` n `48` status `ready` deltaP `39.4097` edge `0.5083` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2524` n `48` status `ready` deltaP `39.4097` edge `0.5083` maxDD `0.0`
- `market_context_high->equity_24h` score `8.9668` n `93` status `ready` deltaP `39.4097` edge `0.4845` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6259` n `48` status `ready` deltaP `42.0732` edge `0.4755` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6259` n `48` status `ready` deltaP `42.0732` edge `0.4755` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.0008` n `61` status `ready` deltaP `51.4088` edge `0.3347` maxDD `-0.1884`
- `news_risk_high->index_24h` score `7.609` n `61` status `ready` deltaP `49.1718` edge `0.3156` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.87` n `48` status `ready` deltaP `49.4792` edge `0.0802` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.87` n `48` status `ready` deltaP `49.4792` edge `0.0802` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1222` n `48` status `ready` deltaP `36.6362` edge `0.1086` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
