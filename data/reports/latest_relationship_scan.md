# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T02:30:09.271275+00:00`
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

- `market_context_high->unknown_24h` score `756.1693` n `50` status `ready` deltaP `-17.5694` edge `63.1676` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `36.4006` n `115` status `ready` deltaP `-7.8844` edge `3.1565` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.2679` n `50` status `ready` deltaP `30.3472` edge `0.6129` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.9813` n `50` status `ready` deltaP `50.6042` edge `0.1654` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.257` n `36` status `ready` deltaP `29.5732` edge `0.3262` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.257` n `36` status `ready` deltaP `29.5732` edge `0.3262` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.0635` n `36` status `ready` deltaP `23.5095` edge `0.31` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0635` n `36` status `ready` deltaP `23.5095` edge `0.31` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `3.7658` n `50` status `ready` deltaP `-4.6319` edge `0.8285` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `3.2276` n `36` status `ready` deltaP `29.3361` edge `0.0966` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.2276` n `36` status `ready` deltaP `29.3361` edge `0.0966` maxDD `-0.1896`
- `risk_on_high->metal_1h` score `1.4989` n `48` status `ready` deltaP `18.2884` edge `0.0269` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.4989` n `48` status `ready` deltaP `18.2884` edge `0.0269` maxDD `-0.2466`
- `risk_on_high->crypto_major_1h` score `1.2126` n `48` status `ready` deltaP `11.9012` edge `0.087` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.2126` n `48` status `ready` deltaP `11.9012` edge `0.087` maxDD `-3.2233`
- `market_context_high->fx_24h` score `0.8927` n `50` status `ready` deltaP `15.1458` edge `0.0197` maxDD `-0.3693`
- `risk_on_high->crypto_alt_1h` score `0.7105` n `48` status `ready` deltaP `8.6078` edge `0.0934` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.7105` n `48` status `ready` deltaP `8.6078` edge `0.0934` maxDD `-2.4421`
- `market_context_high->unknown_1h` score `0.3885` n `127` status `ready` deltaP `-3.0741` edge `0.0865` maxDD `-1.024`
- `risk_on_high->equity_4h` score `0.3875` n `36` status `ready` deltaP `2.9979` edge `0.0678` maxDD `-1.0489`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
