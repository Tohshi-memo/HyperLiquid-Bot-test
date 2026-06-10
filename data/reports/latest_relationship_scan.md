# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T16:52:31.331676+00:00`
- Price records: `672`
- Market context records: `3500`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13142`

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

- `risk_on_high->crypto_major_24h` score `54.2904` n `32` status `ready` deltaP `57.8802` edge `4.1426` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `54.2904` n `32` status `ready` deltaP `57.8802` edge `4.1426` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `51.0633` n `32` status `ready` deltaP `57.7069` edge `3.8857` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `51.0633` n `32` status `ready` deltaP `57.7069` edge `3.8857` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.4014` n `32` status `ready` deltaP `55.1127` edge `3.3327` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.4014` n `32` status `ready` deltaP `55.1127` edge `3.3327` maxDD `0.0`
- `risk_on_high->index_24h` score `24.3604` n `32` status `ready` deltaP `50.7799` edge `1.6915` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.3604` n `32` status `ready` deltaP `50.7799` edge `1.6915` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `19.0948` n `155` status `ready` deltaP `23.5858` edge `2.2071` maxDD `-54.8486`
- `market_context_high->equity_24h` score `18.8139` n `155` status `ready` deltaP `31.8869` edge `1.9965` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `17.1564` n `155` status `ready` deltaP `18.2513` edge `2.1081` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `16.1723` n `32` status `ready` deltaP `31.4883` edge `1.1639` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.1723` n `32` status `ready` deltaP `31.4883` edge `1.1639` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `14.8052` n `32` status `ready` deltaP `27.9585` edge `1.1596` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.8052` n `32` status `ready` deltaP `27.9585` edge `1.1596` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.987` n `155` status `ready` deltaP `35.296` edge `1.0686` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.1313` n `32` status `ready` deltaP `8.985` edge `0.7188` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.1313` n `32` status `ready` deltaP `8.985` edge `0.7188` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.0854` n `155` status `ready` deltaP `25.9641` edge `1.0611` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.9079` n `32` status `ready` deltaP `16.6143` edge `0.5037` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
