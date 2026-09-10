# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T05:22:27.679973+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.6796` n `97` status `ready` deltaP `30.2621` edge `0.9612` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.6796` n `97` status `ready` deltaP `30.2621` edge `0.9612` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.7517` n `219` status `ready` deltaP `22.6313` edge `0.7445` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2613` n `97` status `ready` deltaP `37.3759` edge `0.3931` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2613` n `97` status `ready` deltaP `37.3759` edge `0.3931` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.1179` n `97` status `ready` deltaP `26.0639` edge `0.3386` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1179` n `97` status `ready` deltaP `26.0639` edge `0.3386` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.8618` n `97` status `ready` deltaP `21.0141` edge `0.89` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.8618` n `97` status `ready` deltaP `21.0141` edge `0.89` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.9388` n `97` status `ready` deltaP `30.935` edge `0.0429` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9388` n `97` status `ready` deltaP `30.935` edge `0.0429` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.668` n `219` status `ready` deltaP `14.9306` edge `0.1228` maxDD `0.0`
- `market_context_high->index_24h` score `2.3616` n `219` status `ready` deltaP `25.8086` edge `0.0641` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.3179` n `97` status `ready` deltaP `13.334` edge `0.0396` maxDD `-0.16`
- `risk_on_and_context->commodity_24h` score `1.3179` n `97` status `ready` deltaP `13.334` edge `0.0396` maxDD `-0.16`
- `risk_on_high->crypto_alt_1h` score `1.2336` n `97` status `ready` deltaP `5.5852` edge `0.1008` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.2336` n `97` status `ready` deltaP `5.5852` edge `0.1008` maxDD `-1.1521`
- `risk_on_high->equity_4h` score `1.1815` n `97` status `ready` deltaP `22.0439` edge `-0.0144` maxDD `-1.0611`
- `risk_on_and_context->equity_4h` score `1.1815` n `97` status `ready` deltaP `22.0439` edge `-0.0144` maxDD `-1.0611`
- `risk_on_high->equity_1h` score `1.0578` n `97` status `ready` deltaP `16.7248` edge `0.0045` maxDD `-0.228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
