# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T15:37:25.410378+00:00`
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

- `risk_on_high->unknown_1h` score `7.2819` n `35` status `ready` deltaP `2.1899` edge `0.6317` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2819` n `35` status `ready` deltaP `2.1899` edge `0.6317` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `3.1587` n `85` status `ready` deltaP `10.0368` edge `0.3171` maxDD `-4.9964`
- `market_context_high->equity_24h` score `1.2867` n `85` status `ready` deltaP `15.1818` edge `0.0156` maxDD `-0.1006`
- `market_context_high->index_24h` score `1.2271` n `85` status `ready` deltaP `18.9236` edge `-0.0239` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2047` n `35` status `ready` deltaP `16.5897` edge `0.0039` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2047` n `35` status `ready` deltaP `16.5897` edge `0.0039` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `0.9484` n `35` status `ready` deltaP `11.3601` edge `0.0339` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.9484` n `35` status `ready` deltaP `11.3601` edge `0.0339` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.7789` n `35` status `ready` deltaP `12.9085` edge `0.0332` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.7789` n `35` status `ready` deltaP `12.9085` edge `0.0332` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.7495` n `35` status `ready` deltaP `13.1951` edge `0.012` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.7495` n `35` status `ready` deltaP `13.1951` edge `0.012` maxDD `-0.3343`
- `risk_on_high->commodity_4h` score `0.4659` n `35` status `ready` deltaP `2.9137` edge `0.0823` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4659` n `35` status `ready` deltaP `2.9137` edge `0.0823` maxDD `-1.3651`
- `market_context_high->commodity_4h` score `0.345` n `132` status `ready` deltaP `12.2644` edge `0.0475` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `0.2991` n `85` status `ready` deltaP `17.5612` edge `0.1046` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.0873` n `35` status `ready` deltaP `4.7348` edge `0.0024` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0873` n `35` status `ready` deltaP `4.7348` edge `0.0024` maxDD `-0.1547`
- `risk_on_high->commodity_1h` score `-0.024` n `35` status `ready` deltaP `1.4286` edge `0.0154` maxDD `-0.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
