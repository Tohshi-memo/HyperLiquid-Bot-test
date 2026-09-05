# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T21:52:27.346166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10679`

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

- `risk_on_high->unknown_4h` score `20.7343` n `134` status `ready` deltaP `-1.8429` edge `1.9407` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.7343` n `134` status `ready` deltaP `-1.8429` edge `1.9407` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.315` n `228` status `ready` deltaP `2.0913` edge `0.9258` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.5531` n `37` status `ready` deltaP `25.1783` edge `0.4052` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8743` n `37` status `ready` deltaP `20.1389` edge `0.1886` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2177` n `37` status `ready` deltaP `16.1132` edge `0.202` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3259` n `37` status `ready` deltaP `23.5416` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6051` n `37` status `ready` deltaP `13.2344` edge `0.0846` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.6038` n `37` status `ready` deltaP `8.0752` edge `0.0999` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3077` n `37` status `ready` deltaP `15.6134` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0983` n `37` status `ready` deltaP `5.717` edge `0.0717` maxDD `-0.4628`
- `market_context_high->equity_24h` score `1.0258` n `161` status `ready` deltaP `12.6283` edge `0.4356` maxDD `-20.7444`
- `news_risk_high->fx_24h` score `0.8888` n `37` status `ready` deltaP `19.6086` edge `0.0449` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8398` n `37` status `ready` deltaP `8.2781` edge `0.0413` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.3613` n `37` status `ready` deltaP `16.0567` edge `0.2169` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.2537` n `37` status `ready` deltaP `4.1118` edge `0.0266` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.0499` n `145` status `ready` deltaP `6.1666` edge `-0.0028` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0499` n `145` status `ready` deltaP `6.1666` edge `-0.0028` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0511` n `37` status `ready` deltaP `5.276` edge `0.0029` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
