# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T06:07:38.455980+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32357.3126` n `45` status `ready` deltaP `1.7165` edge `2696.4407` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22197.2315` n `45` status `ready` deltaP `1.958` edge `1849.7701` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1147.7833` n `31` status `ready` deltaP `1.9316` edge `95.6533` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `961.8783` n `31` status `ready` deltaP `3.1766` edge `80.141` maxDD `-0.119`
- `news_risk_high->equity_24h` score `35.4134` n `31` status `ready` deltaP `41.4931` edge `2.6745` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.955` n `31` status `ready` deltaP `46.0069` edge `2.6062` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4697` n `31` status `ready` deltaP `44.2708` edge `2.244` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.5941` n `31` status `ready` deltaP `41.4091` edge `0.7176` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.5214` n `31` status `ready` deltaP `23.1018` edge `0.8098` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5903` n `31` status `ready` deltaP `30.8222` edge `0.5586` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6747` n `31` status `ready` deltaP `56.4684` edge `0.1926` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5858` n `31` status `ready` deltaP `14.0342` edge `0.8925` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3726` n `31` status `ready` deltaP `39.0625` edge `0.1873` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1594` n `31` status `ready` deltaP `17.2928` edge `0.1667` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1284` n `45` status `ready` deltaP `37.4051` edge `0.0398` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.6804` n `31` status `ready` deltaP `29.9076` edge `0.05` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4602` n `31` status `ready` deltaP `10.4597` edge `0.2918` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4218` n `31` status `ready` deltaP `28.9985` edge `0.017` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.0665` n `31` status `ready` deltaP `10.0106` edge `0.2339` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6334` n `31` status `ready` deltaP `31.0797` edge `0.0301` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
