# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T04:37:28.423463+00:00`
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

- `market_context_high->unknown_1h` score `32360.2826` n `45` status `ready` deltaP `2.0159` edge `2696.6862` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22205.0678` n `45` status `ready` deltaP `2.2629` edge `1850.4211` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1150.7532` n `31` status `ready` deltaP `2.231` edge `95.8988` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `969.7147` n `31` status `ready` deltaP `3.4815` edge `80.792` maxDD `-0.119`
- `news_risk_high->equity_24h` score `36.004` n `31` status `ready` deltaP `41.8403` edge `2.7214` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9784` n `31` status `ready` deltaP `46.1806` edge `2.607` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.6692` n `31` status `ready` deltaP `44.9653` edge `2.256` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.7028` n `31` status `ready` deltaP `41.5827` edge `0.7255` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.7086` n `31` status `ready` deltaP `24.0165` edge `0.8193` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6287` n `31` status `ready` deltaP `30.8222` edge `0.5618` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6531` n `31` status `ready` deltaP `56.4684` edge `0.1908` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.6312` n `31` status `ready` deltaP `14.1866` edge `0.8973` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.482` n `31` status `ready` deltaP `39.4097` edge `0.1941` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2541` n `31` status `ready` deltaP `17.8916` edge `0.1706` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1296` n `45` status `ready` deltaP `37.4051` edge `0.0399` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7242` n `31` status `ready` deltaP `30.3649` edge `0.0506` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5568` n `31` status `ready` deltaP `11.3579` edge `0.2982` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4614` n `31` status `ready` deltaP `29.4476` edge `0.0173` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1725` n `31` status `ready` deltaP `10.7591` edge `0.2425` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6435` n `31` status `ready` deltaP `31.2294` edge `0.0304` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
