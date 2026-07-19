# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T21:37:25.274341+00:00`
- Price records: `672`
- Market context records: `7293`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.1509` n `130` status `ready` deltaP `4.1834` edge `0.0017` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6853` n `130` status `ready` deltaP `-1.6332` edge `-0.0154` maxDD `-1.9261`
- `market_context_high->crypto_alt_1h` score `-0.7609` n `130` status `ready` deltaP `-1.0894` edge `0.0136` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-0.7976` n `128` status `ready` deltaP `6.4387` edge `0.0148` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-0.8548` n `130` status `ready` deltaP `2.6486` edge `0.0138` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.9718` n `124` status `ready` deltaP `-0.4348` edge `0.0011` maxDD `-2.1564`
- `market_context_high->unknown_1h` score `-1.1648` n `130` status `ready` deltaP `1.0064` edge `-0.0937` maxDD `-1.3212`
- `market_context_high->commodity_4h` score `-1.2102` n `128` status `ready` deltaP `1.4239` edge `-0.0135` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-1.364` n `128` status `ready` deltaP `5.6402` edge `0.0846` maxDD `-6.2026`
- `market_context_high->index_1h` score `-1.4721` n `130` status `ready` deltaP `-6.7521` edge `-0.0105` maxDD `-2.3729`
- `market_context_high->metal_1h` score `-2.3214` n `130` status `ready` deltaP `-10.5735` edge `-0.0075` maxDD `-1.9032`
- `market_context_high->metal_4h` score `-2.5378` n `128` status `ready` deltaP `-10.3659` edge `-0.0107` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-2.9713` n `124` status `ready` deltaP `-5.5862` edge `-0.1306` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-3.6994` n `128` status `ready` deltaP `-0.1714` edge `-0.0199` maxDD `-16.3127`
- `market_context_high->equity_1h` score `-4.7336` n `130` status `ready` deltaP `-10.4481` edge `-0.0728` maxDD `-15.4942`
- `market_context_high->crypto_major_4h` score `-4.9652` n `128` status `ready` deltaP `0.1143` edge `-0.0251` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.2998` n `128` status `ready` deltaP `-15.0277` edge `-0.064` maxDD `-11.8637`
- `market_context_high->unknown_24h` score `-5.7286` n `125` status `ready` deltaP `-10.5889` edge `-0.0539` maxDD `-16.2313`
- `market_context_high->metal_24h` score `-11.545` n `125` status `ready` deltaP `-29.2444` edge `-0.1362` maxDD `-23.8067`
- `market_context_high->index_24h` score `-13.8857` n `124` status `ready` deltaP `-29.7545` edge `-0.1749` maxDD `-37.0438`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
