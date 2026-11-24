# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T05:37:28.373203+00:00`
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

- `market_context_high->unknown_1h` score `32360.2898` n `45` status `ready` deltaP `1.8662` edge `2696.6878` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22198.4063` n `45` status `ready` deltaP `1.958` edge `1849.868` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1150.7605` n `31` status `ready` deltaP `2.0813` edge `95.9004` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `963.0531` n `31` status `ready` deltaP `3.1766` edge `80.2389` maxDD `-0.119`
- `news_risk_high->equity_24h` score `35.5658` n `31` status `ready` deltaP `41.4931` edge `2.6872` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9231` n `31` status `ready` deltaP `45.8333` edge `2.6047` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.4985` n `31` status `ready` deltaP `44.2708` edge `2.2464` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.6181` n `31` status `ready` deltaP `41.4091` edge `0.7196` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.5926` n `31` status `ready` deltaP `23.4067` edge `0.8137` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6095` n `31` status `ready` deltaP `30.8222` edge `0.5602` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6675` n `31` status `ready` deltaP `56.4684` edge `0.192` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.6109` n `31` status `ready` deltaP `14.1866` edge `0.8947` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3978` n `31` status `ready` deltaP `39.0625` edge `0.1894` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1606` n `31` status `ready` deltaP `17.2928` edge `0.1668` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1296` n `45` status `ready` deltaP `37.4051` edge `0.0399` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7072` n `31` status `ready` deltaP `30.2125` edge `0.0502` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.489` n `31` status `ready` deltaP `10.7591` edge `0.2935` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4099` n `31` status `ready` deltaP `28.8488` edge `0.017` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.0945` n `31` status `ready` deltaP `10.1603` edge `0.2365` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6318` n `31` status `ready` deltaP `31.0797` edge `0.0299` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
