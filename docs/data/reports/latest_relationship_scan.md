# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T07:22:34.590533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4584`

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

- `market_context_high->unknown_1h` score `32335.2014` n `45` status `ready` deltaP `1.7165` edge `2694.5981` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22197.6913` n `45` status `ready` deltaP `2.1105` edge `1849.8074` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1125.6721` n `31` status `ready` deltaP `1.9316` edge `93.8107` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `962.3381` n `31` status `ready` deltaP `3.3291` edge `80.1783` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.0408` n `31` status `ready` deltaP `46.1806` edge `2.6122` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.0342` n `31` status `ready` deltaP `41.4931` edge `2.6429` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4469` n `31` status `ready` deltaP `44.2708` edge `2.2421` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.5293` n `31` status `ready` deltaP `41.4091` edge `0.7122` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.3128` n `31` status `ready` deltaP `22.3397` edge `0.7975` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5081` n `31` status `ready` deltaP `30.3649` edge `0.5548` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6879` n `31` status `ready` deltaP `56.4684` edge `0.1937` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.4674` n `31` status `ready` deltaP `13.272` edge `0.8824` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3078` n `31` status `ready` deltaP `39.0625` edge `0.1819` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2145` n `31` status `ready` deltaP `17.7419` edge `0.1683` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.059` n `45` status `ready` deltaP `36.6429` edge `0.0391` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.6536` n `31` status `ready` deltaP `29.6027` edge `0.0498` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4976` n `31` status `ready` deltaP `10.7591` edge `0.2946` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4602` n `31` status `ready` deltaP `29.4476` edge `0.0172` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1015` n `31` status `ready` deltaP `10.31` edge `0.2364` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6349` n `31` status `ready` deltaP `31.0797` edge `0.0303` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
