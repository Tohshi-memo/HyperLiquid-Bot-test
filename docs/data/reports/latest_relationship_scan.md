# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T19:52:22.026877+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10365`

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

- `risk_on_high->unknown_24h` score `259.9617` n `103` status `ready` deltaP `25.2124` edge `21.5053` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `259.9617` n `103` status `ready` deltaP `25.2124` edge `21.5053` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `20.0869` n `103` status `ready` deltaP `32.376` edge `1.5047` maxDD `-1.397`
- `risk_on_and_context->crypto_major_24h` score `20.0869` n `103` status `ready` deltaP `32.376` edge `1.5047` maxDD `-1.397`
- `risk_on_high->crypto_alt_24h` score `12.3473` n `103` status `ready` deltaP `25.772` edge `0.9076` maxDD `-2.3709`
- `risk_on_and_context->crypto_alt_24h` score `12.3473` n `103` status `ready` deltaP `25.772` edge `0.9076` maxDD `-2.3709`
- `market_context_high->crypto_alt_24h` score `7.5567` n `196` status `ready` deltaP `20.8829` edge `0.5663` maxDD `-3.7304`
- `market_context_high->equity_24h` score `6.5392` n `196` status `ready` deltaP `22.4171` edge `0.4054` maxDD `-0.1266`
- `risk_on_high->equity_24h` score `5.7347` n `103` status `ready` deltaP `21.4958` edge `0.3445` maxDD `-0.1266`
- `risk_on_and_context->equity_24h` score `5.7347` n `103` status `ready` deltaP `21.4958` edge `0.3445` maxDD `-0.1266`
- `risk_on_high->crypto_alt_4h` score `2.512` n `117` status `ready` deltaP `25.9042` edge `0.2474` maxDD `-14.5278`
- `risk_on_and_context->crypto_alt_4h` score `2.512` n `117` status `ready` deltaP `25.9042` edge `0.2474` maxDD `-14.5278`
- `risk_on_high->index_24h` score `2.0255` n `103` status `ready` deltaP `19.4899` edge `0.0785` maxDD `-0.8382`
- `risk_on_and_context->index_24h` score `2.0255` n `103` status `ready` deltaP `19.4899` edge `0.0785` maxDD `-0.8382`
- `market_context_high->index_24h` score `1.8093` n `196` status `ready` deltaP `19.6038` edge `0.0911` maxDD `-1.3477`
- `risk_on_high->metal_24h` score `1.0411` n `103` status `ready` deltaP `14.7013` edge `0.0953` maxDD `-3.5241`
- `risk_on_and_context->metal_24h` score `1.0411` n `103` status `ready` deltaP `14.7013` edge `0.0953` maxDD `-3.5241`
- `risk_on_high->crypto_major_4h` score `0.9259` n `117` status `ready` deltaP `19.8184` edge `0.1838` maxDD `-16.101`
- `risk_on_and_context->crypto_major_4h` score `0.9259` n `117` status `ready` deltaP `19.8184` edge `0.1838` maxDD `-16.101`
- `risk_on_high->crypto_alt_1h` score `0.3943` n `129` status `ready` deltaP `3.8516` edge `0.0706` maxDD `-3.4071`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
