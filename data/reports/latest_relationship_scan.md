# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T07:52:26.075364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11803`

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

- `risk_on_high->unknown_1h` score `7.2999` n `35` status `ready` deltaP `2.4893` edge `0.6312` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2999` n `35` status `ready` deltaP `2.4893` edge `0.6312` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.722` n `84` status `ready` deltaP `7.7381` edge `0.3129` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4406` n `84` status `ready` deltaP `21.0069` edge `-0.02` maxDD `0.0`
- `market_context_high->equity_24h` score `1.1787` n `84` status `ready` deltaP `15.0793` edge `0.0186` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.1079` n `35` status `ready` deltaP `12.2583` edge `0.0412` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.1079` n `35` status `ready` deltaP `12.2583` edge `0.0412` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `1.0067` n `35` status `ready` deltaP `14.4055` edge `0.0422` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `1.0067` n `35` status `ready` deltaP `14.4055` edge `0.0422` maxDD `-1.6811`
- `risk_on_high->fx_4h` score `0.8893` n `31` status `ready` deltaP `18.5287` edge `0.0046` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8893` n `31` status `ready` deltaP `18.5287` edge `0.0046` maxDD `-0.1285`
- `risk_on_high->index_1h` score `0.8812` n `35` status `ready` deltaP `14.6921` edge `0.013` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8812` n `35` status `ready` deltaP `14.6921` edge `0.013` maxDD `-0.3343`
- `risk_on_high->commodity_4h` score `0.874` n `31` status `ready` deltaP `5.7779` edge `0.0834` maxDD `-1.2602`
- `risk_on_and_context->commodity_4h` score `0.874` n `31` status `ready` deltaP `5.7779` edge `0.0834` maxDD `-1.2602`
- `market_context_high->commodity_24h` score `0.8467` n `84` status `ready` deltaP `21.9494` edge `0.0984` maxDD `-3.5605`
- `risk_on_high->crypto_major_4h` score `0.8347` n `31` status `ready` deltaP `10.5281` edge `0.108` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.8347` n `31` status `ready` deltaP `10.5281` edge `0.108` maxDD `-2.0278`
- `market_context_high->commodity_4h` score `0.2192` n `115` status `ready` deltaP `8.583` edge `0.0421` maxDD `-2.3643`
- `risk_on_high->fx_1h` score `0.078` n `35` status `ready` deltaP `4.5851` edge `0.0022` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
