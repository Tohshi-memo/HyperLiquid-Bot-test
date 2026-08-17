# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T10:52:27.139375+00:00`
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

- `risk_on_high->unknown_1h` score `7.2759` n `35` status `ready` deltaP `2.639` edge `0.6282` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2759` n `35` status `ready` deltaP `2.639` edge `0.6282` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.6487` n `92` status `ready` deltaP `8.9674` edge `0.2986` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.2583` n `92` status `ready` deltaP `18.9236` edge `-0.0213` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1767` n `35` status `ready` deltaP `16.2848` edge `0.0036` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1767` n `35` status `ready` deltaP `16.2848` edge `0.0036` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0887` n `35` status `ready` deltaP `12.1086` edge `0.0406` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0887` n `35` status `ready` deltaP `12.1086` edge `0.0406` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.9024` n `35` status `ready` deltaP `13.5073` edge `0.0395` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.9024` n `35` status `ready` deltaP `13.5073` edge `0.0395` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8177` n `35` status `ready` deltaP `13.9436` edge `0.0127` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8177` n `35` status `ready` deltaP `13.9436` edge `0.0127` maxDD `-0.3343`
- `market_context_high->equity_24h` score `0.7005` n `92` status `ready` deltaP `13.6172` edge `-0.0115` maxDD `-0.6726`
- `risk_on_high->commodity_4h` score `0.3249` n `35` status `ready` deltaP `2.4564` edge `0.0736` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3249` n `35` status `ready` deltaP `2.4564` edge `0.0736` maxDD `-1.3651`
- `market_context_high->commodity_24h` score `0.3095` n `92` status `ready` deltaP `17.8216` edge `0.1042` maxDD `-4.666`
- `risk_on_high->crypto_major_4h` score `0.2723` n `35` status `ready` deltaP `3.5235` edge `0.0826` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.2723` n `35` status `ready` deltaP `3.5235` edge `0.0826` maxDD `-2.0278`
- `market_context_high->commodity_4h` score `0.2569` n `127` status `ready` deltaP `10.3754` edge `0.0488` maxDD `-2.4692`
- `risk_on_high->fx_1h` score `0.0788` n `35` status `ready` deltaP `4.5851` edge `0.0023` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
