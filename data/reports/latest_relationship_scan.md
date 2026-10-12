# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T02:37:24.021118+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `756.1669` n `50` status `ready` deltaP `-17.5694` edge `63.1674` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `36.3946` n `115` status `ready` deltaP `-7.8844` edge `3.156` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.2559` n `50` status `ready` deltaP `30.3472` edge `0.6119` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.9777` n `50` status `ready` deltaP `50.6042` edge `0.1651` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.2798` n `36` status `ready` deltaP `29.5732` edge `0.3281` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2798` n `36` status `ready` deltaP `29.5732` edge `0.3281` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.1367` n `36` status `ready` deltaP `23.5095` edge `0.3161` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.1367` n `36` status `ready` deltaP `23.5095` edge `0.3161` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `3.7752` n `50` status `ready` deltaP `-4.6319` edge `0.8297` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `3.2204` n `36` status `ready` deltaP `29.3361` edge `0.096` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.2204` n `36` status `ready` deltaP `29.3361` edge `0.096` maxDD `-0.1896`
- `risk_on_high->metal_1h` score `1.4941` n `48` status `ready` deltaP `18.2884` edge `0.0265` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.4941` n `48` status `ready` deltaP `18.2884` edge `0.0265` maxDD `-0.2466`
- `risk_on_high->crypto_major_1h` score `1.2294` n `48` status `ready` deltaP `11.9012` edge `0.0884` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.2294` n `48` status `ready` deltaP `11.9012` edge `0.0884` maxDD `-3.2233`
- `market_context_high->fx_24h` score `0.8907` n `50` status `ready` deltaP `15.1458` edge `0.0196` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `0.7448` n `48` status `ready` deltaP `8.6078` edge `0.0978` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.7448` n `48` status `ready` deltaP `8.6078` edge `0.0978` maxDD `-2.4421`
- `market_context_high->metal_4h` score `0.3798` n `115` status `ready` deltaP `11.3892` edge `0.028` maxDD `-1.1153`
- `market_context_high->unknown_1h` score `0.3789` n `127` status `ready` deltaP `-3.0741` edge `0.0857` maxDD `-1.024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
