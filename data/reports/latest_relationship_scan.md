# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T06:37:29.323971+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4572`

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

- `market_context_high->unknown_1h` score `32349.6146` n `45` status `ready` deltaP `1.7165` edge `2695.7992` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22196.8669` n `45` status `ready` deltaP `2.1105` edge `1849.7387` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1140.0853` n `31` status `ready` deltaP `1.9316` edge `95.0118` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `961.5137` n `31` status `ready` deltaP `3.3291` edge `80.1096` maxDD `-0.119`
- `news_risk_high->equity_24h` score `35.2682` n `31` status `ready` deltaP `41.4931` edge `2.6624` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9886` n `31` status `ready` deltaP `46.0069` edge `2.609` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4613` n `31` status `ready` deltaP `44.2708` edge `2.2433` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.5689` n `31` status `ready` deltaP `41.4091` edge `0.7155` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.4574` n `31` status `ready` deltaP `22.797` edge `0.8065` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5879` n `31` status `ready` deltaP `30.8222` edge `0.5584` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6807` n `31` status `ready` deltaP `56.4684` edge `0.1931` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5544` n `31` status `ready` deltaP `13.7293` edge `0.8905` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3486` n `31` status `ready` deltaP `39.0625` edge `0.1853` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2061` n `31` status `ready` deltaP `17.5922` edge `0.1686` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1004` n `45` status `ready` deltaP `37.1002` edge `0.0395` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.6816` n `31` status `ready` deltaP `29.9076` edge `0.0501` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4937` n `31` status `ready` deltaP `10.7591` edge `0.2941` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4482` n `31` status `ready` deltaP `29.2979` edge `0.0172` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.0875` n `31` status `ready` deltaP `10.1603` edge `0.2356` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6458` n `31` status `ready` deltaP `31.2294` edge `0.0307` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
