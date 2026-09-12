# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T21:36:44.112607+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12697`

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

- `market_context_high->unknown_24h` score `12520.6631` n `69` status `ready` deltaP `12.5528` edge `1043.3101` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.8604` n `82` status `ready` deltaP `-5.6996` edge `31.9852` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.4554` n `76` status `ready` deltaP `39.2361` edge `1.423` maxDD `-9.0632`
- `news_risk_high->crypto_alt_24h` score `17.5055` n `76` status `ready` deltaP `31.7525` edge `1.2959` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `12.5168` n `69` status `ready` deltaP `26.9852` edge `0.9459` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.8017` n `69` status `ready` deltaP `43.5764` edge `0.5263` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.3681` n `76` status `ready` deltaP `18.5764` edge `0.6234` maxDD `-4.9922`
- `news_risk_high->index_24h` score `6.5143` n `76` status `ready` deltaP `44.9287` edge `0.261` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.611` n `76` status `ready` deltaP `33.3882` edge `0.2896` maxDD `-0.5682`
- `market_context_high->index_24h` score `3.2651` n `69` status `ready` deltaP `35.0317` edge `0.0779` maxDD `-0.1483`
- `market_context_high->commodity_24h` score `3.0305` n `69` status `ready` deltaP `33.3182` edge `0.0443` maxDD `-0.1105`
- `risk_on_high->crypto_alt_4h` score `1.6781` n `47` status `ready` deltaP `16.2623` edge `0.2206` maxDD `-4.7761`
- `risk_on_and_context->crypto_alt_4h` score `1.6781` n `47` status `ready` deltaP `16.2623` edge `0.2206` maxDD `-4.7761`
- `market_context_high->equity_4h` score `0.4582` n `94` status `ready` deltaP `13.2135` edge `0.0411` maxDD `-2.6138`
- `news_risk_high->index_4h` score `0.066` n `82` status `ready` deltaP `6.5549` edge `0.0276` maxDD `-0.6935`
- `risk_on_high->index_1h` score `0.052` n `56` status `ready` deltaP `6.2447` edge `0.0004` maxDD `-0.162`
- `risk_on_and_context->index_1h` score `0.052` n `56` status `ready` deltaP `6.2447` edge `0.0004` maxDD `-0.162`
- `risk_on_high->metal_1h` score `0.0077` n `56` status `ready` deltaP `4.9294` edge `0.0008` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.0077` n `56` status `ready` deltaP `4.9294` edge `0.0008` maxDD `-0.3081`
- `risk_on_high->equity_4h` score `0.0023` n `47` status `ready` deltaP `8.9582` edge `0.0314` maxDD `-2.5997`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
