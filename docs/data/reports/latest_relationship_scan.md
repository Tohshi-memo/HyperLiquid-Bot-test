# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T13:22:24.641133+00:00`
- Price records: `672`
- Market context records: `7358`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `6.8978` n `32` status `ready` deltaP `38.186` edge `0.3395` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.8978` n `32` status `ready` deltaP `38.186` edge `0.3395` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.6627` n `32` status `ready` deltaP `31.4787` edge `0.2864` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.6627` n `32` status `ready` deltaP `31.4787` edge `0.2864` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.3045` n `32` status `ready` deltaP `17.9878` edge `0.3651` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3045` n `32` status `ready` deltaP `17.9878` edge `0.3651` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2113` n `32` status `ready` deltaP `19.9289` edge `0.0469` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2113` n `32` status `ready` deltaP `19.9289` edge `0.0469` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2283` n `32` status `ready` deltaP `3.9977` edge `0.0203` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2283` n `32` status `ready` deltaP `3.9977` edge `0.0203` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1624` n `32` status `ready` deltaP `3.9039` edge `0.0325` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1624` n `32` status `ready` deltaP `3.9039` edge `0.0325` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1118` n `32` status `ready` deltaP `0.5988` edge `0.0474` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1118` n `32` status `ready` deltaP `0.5988` edge `0.0474` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.1346` n `32` status `ready` deltaP `-0.6098` edge `0.0752` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1346` n `32` status `ready` deltaP `-0.6098` edge `0.0752` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1715` n `129` status `ready` deltaP `4.089` edge `-0.0003` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.595` n `129` status `ready` deltaP `5.9238` edge `0.1201` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7276` n `129` status `ready` deltaP `-3.4151` edge `-0.0133` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.8085` n `129` status `ready` deltaP `-5.3111` edge `-0.0074` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
