# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T06:52:31.606937+00:00`
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

- `market_context_high->unknown_1h` score `32347.415` n `45` status `ready` deltaP `1.7165` edge `2695.6159` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22197.6577` n `45` status `ready` deltaP `2.1105` edge `1849.8046` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1137.8857` n `31` status `ready` deltaP `1.9316` edge `94.8285` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `962.3045` n `31` status `ready` deltaP `3.3291` edge `80.1755` maxDD `-0.119`
- `news_risk_high->equity_24h` score `35.1878` n `31` status `ready` deltaP `41.4931` edge `2.6557` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9958` n `31` status `ready` deltaP `46.0069` edge `2.6096` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4529` n `31` status `ready` deltaP `44.2708` edge `2.2426` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.5557` n `31` status `ready` deltaP `41.4091` edge `0.7144` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.4104` n `31` status `ready` deltaP `22.6445` edge `0.8036` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5577` n `31` status `ready` deltaP `30.6698` edge `0.5569` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6831` n `31` status `ready` deltaP `56.4684` edge `0.1933` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5262` n `31` status `ready` deltaP `13.5769` edge `0.8879` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3342` n `31` status `ready` deltaP `39.0625` edge `0.1841` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2217` n `31` status `ready` deltaP `17.7419` edge `0.1689` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.0858` n `45` status `ready` deltaP `36.9478` edge `0.0393` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.667` n `31` status `ready` deltaP `29.7551` edge `0.0499` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.507` n `31` status `ready` deltaP `10.9088` edge `0.2948` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4602` n `31` status `ready` deltaP `29.4476` edge `0.0172` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1007` n `31` status `ready` deltaP `10.31` edge `0.2363` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6544` n `31` status `ready` deltaP `31.3791` edge `0.0308` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
