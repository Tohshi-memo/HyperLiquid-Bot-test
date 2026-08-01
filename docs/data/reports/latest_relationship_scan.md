# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T12:52:28.422139+00:00`
- Price records: `672`
- Market context records: `8623`
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

- `news_risk_high->unknown_24h` score `5191.9686` n `60` status `ready` deltaP `34.2345` edge `432.4779` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.8444` n `46` status `ready` deltaP `53.3494` edge `1.1711` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.2065` n `60` status `ready` deltaP `21.2557` edge `0.4352` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4946` n `60` status `ready` deltaP `21.5601` edge `0.0832` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6844` n `60` status `ready` deltaP `14.9302` edge `0.0885` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.6207` n `60` status `ready` deltaP `12.5038` edge `0.1474` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.1324` n `60` status `ready` deltaP `7.207` edge `0.1747` maxDD `-3.5385`
- `market_context_high->fx_24h` score `0.5745` n `46` status `ready` deltaP `16.1254` edge `0.0483` maxDD `-1.905`
- `news_risk_high->crypto_alt_1h` score `0.4288` n `60` status `ready` deltaP `8.1836` edge `0.0531` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.3991` n `60` status `ready` deltaP `10.8371` edge `0.1181` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3349` n `60` status `ready` deltaP `6.3673` edge `0.0517` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.3169` n `60` status `ready` deltaP `14.6651` edge `0.0244` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1166` n `60` status `ready` deltaP `4.1476` edge `0.0349` maxDD `-0.8085`
- `news_risk_high->fx_1h` score `0.111` n `60` status `ready` deltaP `5.5988` edge `0.005` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0559` n `60` status `ready` deltaP `5.489` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->index_1h` score `-0.0069` n `60` status `ready` deltaP `3.2236` edge `0.0093` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0141` n `60` status `ready` deltaP `9.6651` edge `0.014` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.1829` n `60` status `ready` deltaP `3.9321` edge `0.0006` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3434` n `60` status `ready` deltaP `3.6128` edge `-0.0059` maxDD `-1.9764`
- `market_context_high->crypto_alt_1h` score `-0.6009` n `60` status `ready` deltaP `-3.483` edge `0.0089` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
