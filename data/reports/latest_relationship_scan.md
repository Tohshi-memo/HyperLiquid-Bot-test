# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T11:37:35.063917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `17.0212` n `91` status `ready` deltaP `34.2624` edge `1.213` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.0212` n `91` status `ready` deltaP `34.2624` edge `1.213` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `12.4325` n `201` status `ready` deltaP `25.8266` edge `0.9466` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.0543` n `91` status `ready` deltaP `40.269` edge `0.4399` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.0543` n `91` status `ready` deltaP `40.269` edge `0.4399` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.3478` n `91` status `ready` deltaP `30.0674` edge `0.4144` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.3478` n `91` status `ready` deltaP `30.0674` edge `0.4144` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.8273` n `91` status `ready` deltaP `23.1113` edge `0.9998` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.8273` n `91` status `ready` deltaP `23.1113` edge `0.9998` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.3765` n `91` status `ready` deltaP `35.0714` edge `0.0518` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.3765` n `91` status `ready` deltaP `35.0714` edge `0.0518` maxDD `-0.0051`
- `market_context_high->equity_24h` score `3.3261` n `201` status `ready` deltaP `19.2708` edge `0.1487` maxDD `0.0`
- `market_context_high->index_24h` score `2.5048` n `201` status `ready` deltaP `29.4129` edge `0.052` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.1612` n `91` status `ready` deltaP `27.0956` edge `0.0088` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.1612` n `91` status `ready` deltaP `27.0956` edge `0.0088` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.8196` n `201` status `ready` deltaP `18.2784` edge `0.0437` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.8034` n `91` status `ready` deltaP `17.9449` edge `0.04` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.8034` n `91` status `ready` deltaP `17.9449` edge `0.04` maxDD `-0.0811`
- `risk_on_high->equity_24h` score `1.7205` n `91` status `ready` deltaP `19.2708` edge `0.0149` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7205` n `91` status `ready` deltaP `19.2708` edge `0.0149` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
