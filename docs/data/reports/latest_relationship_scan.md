# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T11:07:23.759204+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11752`

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

- `news_risk_high->unknown_24h` score `49.5007` n `56` status `ready` deltaP `14.1121` edge `4.0855` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.2008` n `56` status `ready` deltaP `36.2351` edge `1.9958` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.4539` n `110` status `ready` deltaP `17.5537` edge `0.6607` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2855` n `80` status `ready` deltaP `10.9756` edge `0.5096` maxDD `-1.7183`
- `market_context_high->metal_24h` score `3.9775` n `110` status `ready` deltaP `30.7765` edge `0.2282` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.9098` n `110` status `ready` deltaP `18.7029` edge `0.1585` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.6847` n `80` status `ready` deltaP `5.6737` edge `0.2216` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.5791` n `56` status `ready` deltaP `23.0903` edge `0.3659` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3937` n `80` status `ready` deltaP `34.8171` edge `0.0223` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `2.0798` n `56` status `ready` deltaP `19.4444` edge `0.3769` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.6648` n `56` status `ready` deltaP `36.4583` edge `0.0418` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.3566` n `56` status `ready` deltaP `19.37` edge `0.0259` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.0767` n `119` status `ready` deltaP `8.7619` edge `0.0805` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7375` n `80` status `ready` deltaP `14.1916` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4338` n `80` status `ready` deltaP `12.3503` edge `0.0053` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.2917` n `110` status `ready` deltaP `6.9179` edge `0.0082` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.4066` n `80` status `ready` deltaP `0.0075` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->crypto_major_4h` score `-0.4873` n `110` status `ready` deltaP `14.5455` edge `0.2075` maxDD `-20.9394`
- `news_risk_high->index_4h` score `-0.5285` n `80` status `ready` deltaP `1.9207` edge `-0.0164` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.617` n `80` status `ready` deltaP `6.7378` edge `0.0101` maxDD `-2.0635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
