# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T14:52:25.932770+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11819`

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

- `risk_on_high->unknown_1h` score `7.162` n `35` status `ready` deltaP `1.8905` edge `0.6237` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.162` n `35` status `ready` deltaP `1.8905` edge `0.6237` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.6454` n `88` status `ready` deltaP `8.1913` edge `0.2908` maxDD `-4.9964`
- `market_context_high->index_24h` score `1.2379` n `88` status `ready` deltaP `18.9236` edge `-0.023` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2303` n `35` status `ready` deltaP `16.8946` edge `0.004` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2303` n `35` status `ready` deltaP `16.8946` edge `0.004` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0252` n `35` status `ready` deltaP `11.8092` edge `0.0373` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0252` n `35` status `ready` deltaP `11.8092` edge `0.0373` maxDD `-1.1144`
- `market_context_high->equity_24h` score `0.9435` n `88` status `ready` deltaP `14.2992` edge `-0.0063` maxDD `-0.1657`
- `risk_on_high->equity_1h` score `0.8269` n `35` status `ready` deltaP `13.0582` edge `0.0362` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.8269` n `35` status `ready` deltaP `13.0582` edge `0.0362` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.7782` n `35` status `ready` deltaP `13.4945` edge `0.0124` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.7782` n `35` status `ready` deltaP `13.4945` edge `0.0124` maxDD `-0.3343`
- `risk_on_high->commodity_4h` score `0.4441` n `35` status `ready` deltaP `2.7613` edge `0.0815` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4441` n `35` status `ready` deltaP `2.7613` edge `0.0815` maxDD `-1.3651`
- `market_context_high->commodity_4h` score `0.4072` n `135` status `ready` deltaP `12.92` edge `0.0511` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `0.3692` n `88` status `ready` deltaP `18.3239` edge `0.1085` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.0873` n `35` status `ready` deltaP `4.7348` edge `0.0024` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0873` n `35` status `ready` deltaP `4.7348` edge `0.0024` maxDD `-0.1547`
- `risk_on_high->crypto_major_4h` score `0.0123` n `35` status `ready` deltaP `1.3894` edge `0.0635` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
