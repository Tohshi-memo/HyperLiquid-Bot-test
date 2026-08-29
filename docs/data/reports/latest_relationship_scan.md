# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T09:52:23.432060+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11772`

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

- `news_risk_high->unknown_24h` score `49.1349` n `56` status `ready` deltaP `13.244` edge `4.0608` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.1324` n `56` status `ready` deltaP `36.2351` edge `1.9901` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.2826` n `115` status `ready` deltaP `17.0018` edge `0.6501` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2747` n `80` status `ready` deltaP `10.9756` edge `0.5087` maxDD `-1.7183`
- `market_context_high->metal_24h` score `3.8045` n `115` status `ready` deltaP `30.699` edge `0.2143` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.7179` n `115` status `ready` deltaP `19.4539` edge `0.1375` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.6799` n `80` status `ready` deltaP `5.6737` edge `0.2212` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.4287` n `56` status `ready` deltaP `22.2222` edge `0.3524` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3547` n `80` status `ready` deltaP `34.3598` edge `0.0221` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `1.9569` n `56` status `ready` deltaP `19.2708` edge `0.3623` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.5697` n `56` status `ready` deltaP `35.5903` edge `0.0354` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.2703` n `56` status `ready` deltaP `18.502` edge `0.0245` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.1031` n `119` status `ready` deltaP `8.7619` edge `0.0827` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6872` n `80` status `ready` deltaP `13.5928` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4579` n `80` status `ready` deltaP `12.7994` edge `0.0054` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.213` n `115` status `ready` deltaP `8.2675` edge `0.0093` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5451` n `80` status `ready` deltaP `1.6159` edge `-0.0165` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.5807` n `80` status `ready` deltaP `7.3476` edge `0.0107` maxDD `-2.0635`
- `news_risk_high->equity_1h` score `-0.6061` n `80` status `ready` deltaP `8.3084` edge `-0.0397` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
