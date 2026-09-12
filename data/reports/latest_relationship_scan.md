# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T18:52:29.556751+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12779`

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

- `market_context_high->unknown_24h` score `9159.1446` n `80` status `ready` deltaP `12.9514` edge `763.1809` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `6667.8181` n `40` status `ready` deltaP `15.4514` edge `555.5485` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `6667.8181` n `40` status `ready` deltaP `15.4514` edge `555.5485` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.4232` n `82` status `ready` deltaP `-5.4002` edge `32.0301` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.6946` n `69` status `ready` deltaP `46.1504` edge `1.5365` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.188` n `69` status `ready` deltaP `29.8837` edge `1.2819` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.0029` n `40` status `ready` deltaP `37.6736` edge `1.1054` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.0029` n `40` status `ready` deltaP `37.6736` edge `1.1054` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.0702` n `80` status `ready` deltaP `30.1736` edge `1.0541` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.8745` n `40` status `ready` deltaP `41.6667` edge `0.5451` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.8745` n `40` status `ready` deltaP `41.6667` edge `0.5451` maxDD `0.0`
- `market_context_high->equity_24h` score `9.5037` n `80` status `ready` deltaP `41.6667` edge `0.5142` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.2172` n `69` status `ready` deltaP `24.2754` edge `0.687` maxDD `-3.1258`
- `risk_on_high->crypto_alt_4h` score `7.7508` n `47` status `ready` deltaP `37.9897` edge `0.4298` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.7508` n `47` status `ready` deltaP `37.9897` edge `0.4298` maxDD `-1.9733`
- `news_risk_high->index_24h` score `6.6973` n `69` status `ready` deltaP `43.9009` edge `0.2831` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.4287` n `69` status `ready` deltaP `40.9496` edge `0.3068` maxDD `-0.526`
- `risk_on_high->index_24h` score `4.92` n `40` status `ready` deltaP `49.4444` edge `0.0846` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.92` n `40` status `ready` deltaP `49.4444` edge `0.0846` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `3.5398` n `47` status `ready` deltaP `30.6857` edge `0.1039` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
