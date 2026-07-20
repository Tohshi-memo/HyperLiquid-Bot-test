# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T00:59:19.123015+00:00`
- Price records: `672`
- Market context records: `7307`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14799`

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

- `risk_on_high->crypto_major_1h` score `1.2612` n `30` status `ready` deltaP `18.6527` edge `0.0618` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2612` n `30` status `ready` deltaP `18.6527` edge `0.0618` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.8687` n `30` status `ready` deltaP `7.988` edge `0.0881` maxDD `-0.7314`
- `risk_on_and_context->equity_1h` score `0.8687` n `30` status `ready` deltaP `7.988` edge `0.0881` maxDD `-0.7314`
- `risk_on_high->commodity_1h` score `0.3223` n `30` status `ready` deltaP `4.4144` edge `0.0211` maxDD `-0.227`
- `risk_on_and_context->commodity_1h` score `0.3223` n `30` status `ready` deltaP `4.4144` edge `0.0211` maxDD `-0.227`
- `risk_on_high->crypto_alt_1h` score `0.143` n `30` status `ready` deltaP `0.2994` edge `0.0534` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.143` n `30` status `ready` deltaP `0.2994` edge `0.0534` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1755` n `126` status `ready` deltaP `3.861` edge `0.0007` maxDD `-0.5817`
- `market_context_high->index_1h` score `-0.6695` n `126` status `ready` deltaP `-3.2818` edge `-0.0031` maxDD `-1.868`
- `market_context_high->commodity_1h` score `-0.7194` n `126` status `ready` deltaP `-3.046` edge `-0.0147` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.7557` n `126` status `ready` deltaP `3.4146` edge `0.0214` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.7646` n `111` status `ready` deltaP `3.1602` edge `0.0037` maxDD `-2.1564`
- `risk_on_high->index_1h` score `-0.784` n `30` status `ready` deltaP `-12.012` edge `0.0124` maxDD `-0.2932`
- `risk_on_and_context->index_1h` score `-0.784` n `30` status `ready` deltaP `-12.012` edge `0.0124` maxDD `-0.2932`
- `market_context_high->commodity_4h` score `-0.7861` n `117` status `ready` deltaP `1.3291` edge `-0.0128` maxDD `-2.4139`
- `market_context_high->crypto_alt_1h` score `-0.9766` n `126` status `ready` deltaP `-0.4943` edge `0.0258` maxDD `-5.9775`
- `risk_on_high->fx_1h` score `-0.9907` n `30` status `ready` deltaP `-7.5676` edge `-0.005` maxDD `-0.1688`
- `risk_on_and_context->fx_1h` score `-0.9907` n `30` status `ready` deltaP `-7.5676` edge `-0.005` maxDD `-0.1688`
- `market_context_high->fx_4h` score `-1.0524` n `117` status `ready` deltaP `2.4229` edge `0.0089` maxDD `-1.4649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
