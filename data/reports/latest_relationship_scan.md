# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T04:57:40.610530+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4524`

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

- `market_context_high->unknown_1h` score `32360.3282` n `45` status `ready` deltaP `2.0159` edge `2696.69` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22202.1866` n `45` status `ready` deltaP `2.2629` edge `1850.181` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1150.7988` n `31` status `ready` deltaP `2.231` edge `95.9026` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `966.8335` n `31` status `ready` deltaP `3.4815` edge `80.5519` maxDD `-0.119`
- `news_risk_high->equity_24h` score `35.8833` n `31` status `ready` deltaP `41.6667` edge `2.7125` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9562` n `31` status `ready` deltaP `46.0069` edge `2.6063` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.6277` n `31` status `ready` deltaP `44.7917` edge `2.2537` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.6848` n `31` status `ready` deltaP `41.5827` edge `0.724` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.6856` n `31` status `ready` deltaP `23.864` edge `0.8184` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6275` n `31` status `ready` deltaP `30.8222` edge `0.5617` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6567` n `31` status `ready` deltaP `56.4684` edge `0.1911` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.6281` n `31` status `ready` deltaP `14.1866` edge `0.8969` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.4537` n `31` status `ready` deltaP `39.2361` edge `0.1929` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2349` n `31` status `ready` deltaP `17.7419` edge `0.17` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1296` n `45` status `ready` deltaP `37.4051` edge `0.0399` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7108` n `31` status `ready` deltaP `30.2125` edge `0.0505` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5436` n `31` status `ready` deltaP `11.2082` edge `0.2975` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4482` n `31` status `ready` deltaP `29.2979` edge `0.0172` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1561` n `31` status `ready` deltaP `10.6094` edge `0.2414` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.652` n `31` status `ready` deltaP `31.3791` edge `0.0305` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
