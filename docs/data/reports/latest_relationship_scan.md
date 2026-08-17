# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T08:07:32.494364+00:00`
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
- `market_context_high->crypto_major_24h` score `2.7559` n `85` status `ready` deltaP `8.0126` edge `0.3139` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4279` n `85` status `ready` deltaP `20.8333` edge `-0.0199` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1946` n `32` status `ready` deltaP `16.4634` edge `0.0039` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1946` n `32` status `ready` deltaP `16.4634` edge `0.0039` maxDD `-0.1285`
- `market_context_high->equity_24h` score `1.1619` n `85` status `ready` deltaP `14.9898` edge `0.0178` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.1091` n `35` status `ready` deltaP `12.2583` edge `0.0413` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.1091` n `35` status `ready` deltaP `12.2583` edge `0.0413` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `1.0055` n `35` status `ready` deltaP `14.4055` edge `0.0421` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `1.0055` n `35` status `ready` deltaP `14.4055` edge `0.0421` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8812` n `35` status `ready` deltaP `14.6921` edge `0.013` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8812` n `35` status `ready` deltaP `14.6921` edge `0.013` maxDD `-0.3343`
- `market_context_high->commodity_24h` score `0.7526` n `85` status `ready` deltaP `21.2826` edge `0.0974` maxDD `-3.7567`
- `risk_on_high->crypto_major_4h` score `0.7054` n `32` status `ready` deltaP `8.6128` edge `0.1042` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.7054` n `32` status `ready` deltaP `8.6128` edge `0.1042` maxDD `-2.0278`
- `risk_on_high->commodity_4h` score `0.6492` n `32` status `ready` deltaP `4.1159` edge `0.0802` maxDD `-1.283`
- `risk_on_and_context->commodity_4h` score `0.6492` n `32` status `ready` deltaP `4.1159` edge `0.0802` maxDD `-1.283`
- `market_context_high->commodity_4h` score `0.1635` n `116` status `ready` deltaP `8.2107` edge `0.0419` maxDD `-2.3871`
- `risk_on_high->fx_1h` score `0.0858` n `35` status `ready` deltaP `4.7348` edge `0.0022` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
