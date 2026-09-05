# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T21:37:26.429074+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10649`

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

- `risk_on_high->unknown_4h` score `20.9939` n `135` status `ready` deltaP `-1.5831` edge `1.9606` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.9939` n `135` status `ready` deltaP `-1.5831` edge `1.9606` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `7.7342` n `228` status `ready` deltaP `2.0913` edge `0.8774` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.6071` n `37` status `ready` deltaP `25.1783` edge `0.4097` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8671` n `37` status `ready` deltaP `20.1389` edge `0.188` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2299` n `37` status `ready` deltaP `16.2657` edge `0.202` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3259` n `37` status `ready` deltaP `23.5416` edge `0.059` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.6172` n `37` status `ready` deltaP `8.2276` edge `0.1` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6051` n `37` status `ready` deltaP `13.2344` edge `0.0846` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.3197` n `37` status `ready` deltaP `15.7631` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1383` n `37` status `ready` deltaP `14.2742` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1007` n `37` status `ready` deltaP `5.717` edge `0.0719` maxDD `-0.4628`
- `market_context_high->equity_24h` score `0.9871` n `162` status `ready` deltaP `12.7894` edge `0.4313` maxDD `-20.7444`
- `news_risk_high->fx_24h` score `0.8737` n `37` status `ready` deltaP `19.435` edge `0.0448` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8602` n `37` status `ready` deltaP `8.4278` edge `0.042` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.4093` n `37` status `ready` deltaP `16.2303` edge `0.2219` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.2827` n `37` status `ready` deltaP `4.2642` edge `0.028` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.0202` n `145` status `ready` deltaP `6.7066` edge `-0.0026` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0202` n `145` status `ready` deltaP `6.7066` edge `-0.0026` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0433` n `37` status `ready` deltaP `5.4257` edge `0.0029` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
