# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T08:37:24.520533+00:00`
- Price records: `672`
- Market context records: `8603`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4748.4768` n `64` status `ready` deltaP `34.7222` edge `395.517` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `19.2096` n `31` status `ready` deltaP `49.2496` edge `1.3122` maxDD `-2.1786`
- `market_context_high->crypto_major_24h` score `6.0915` n `31` status `ready` deltaP `20.7941` edge `0.8459` maxDD `-13.285`
- `news_risk_high->equity_4h` score `5.8027` n `64` status `ready` deltaP `20.1982` edge `0.4086` maxDD `-3.4427`
- `market_context_high->fx_24h` score `3.8462` n `31` status `ready` deltaP `39.3986` edge `0.0917` maxDD `-0.3737`
- `news_risk_high->index_4h` score `2.2518` n `64` status `ready` deltaP `19.2454` edge `0.0784` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7385` n `64` status `ready` deltaP `16.2519` edge `0.0842` maxDD `-2.4803`
- `market_context_high->metal_24h` score `1.6669` n `31` status `ready` deltaP `13.8496` edge `0.1054` maxDD `-1.7058`
- `market_context_high->crypto_alt_4h` score `1.5608` n `62` status `ready` deltaP `11.5312` edge `0.1489` maxDD `-5.323`
- `market_context_high->index_24h` score `1.2441` n `31` status `ready` deltaP `25.1344` edge `0.0644` maxDD `-2.7968`
- `news_risk_high->crypto_major_4h` score `1.0841` n `64` status `ready` deltaP `7.5076` edge `0.1665` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.4236` n `64` status `ready` deltaP `11.128` edge `0.1193` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4079` n `64` status `ready` deltaP `7.8125` edge `0.0529` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3579` n `64` status `ready` deltaP `7.064` edge `0.05` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1049` n `64` status `ready` deltaP `5.5857` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0838` n `64` status `ready` deltaP `12.0808` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.038` n `64` status `ready` deltaP `3.0869` edge `0.0319` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0169` n `64` status `ready` deltaP `3.7706` edge `0.0087` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0844` n `62` status `ready` deltaP `8.9054` edge `0.0132` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1599` n `64` status `ready` deltaP `2.9566` edge `0.0073` maxDD `-0.5599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
