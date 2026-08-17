# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T06:22:26.161674+00:00`
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

- `risk_on_high->unknown_1h` score `5.2995` n `35` status `ready` deltaP `2.4893` edge `0.4645` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `5.2995` n `35` status `ready` deltaP `2.4893` edge `0.4645` maxDD `-0.8243`
- `market_context_high->commodity_24h` score `2.3083` n `78` status `ready` deltaP `26.4023` edge `0.1099` maxDD `-2.151`
- `market_context_high->crypto_major_24h` score `2.2385` n `78` status `ready` deltaP `5.8494` edge `0.2852` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4769` n `78` status `ready` deltaP `21.7014` edge `-0.0216` maxDD `0.0`
- `market_context_high->equity_24h` score `1.296` n `78` status `ready` deltaP `15.5716` edge `0.0251` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.0971` n `35` status `ready` deltaP `12.1086` edge `0.0413` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0971` n `35` status `ready` deltaP `12.1086` edge `0.0413` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `1.0055` n `35` status `ready` deltaP `14.4055` edge `0.0421` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `1.0055` n `35` status `ready` deltaP `14.4055` edge `0.0421` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.868` n `35` status `ready` deltaP `14.5424` edge `0.0129` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.868` n `35` status `ready` deltaP `14.5424` edge `0.0129` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.5187` n `109` status `ready` deltaP `11.019` edge `0.0495` maxDD `-1.5164`
- `risk_on_high->fx_1h` score `0.0531` n `35` status `ready` deltaP `4.136` edge `0.002` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0531` n `35` status `ready` deltaP `4.136` edge `0.002` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.143` n `109` status `ready` deltaP `16.9809` edge `0.0156` maxDD `-4.5909`
- `risk_on_high->commodity_1h` score `-0.2384` n `35` status `ready` deltaP `-0.6672` edge `0.0115` maxDD `-0.4871`
- `risk_on_and_context->commodity_1h` score `-0.2384` n `35` status `ready` deltaP `-0.6672` edge `0.0115` maxDD `-0.4871`
- `market_context_high->fx_1h` score `-0.3252` n `121` status `ready` deltaP `-0.5629` edge `-0.0009` maxDD `-0.2968`
- `market_context_high->crypto_major_4h` score `-0.3388` n `109` status `ready` deltaP `5.1983` edge `0.0427` maxDD `-4.6638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
