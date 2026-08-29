# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T10:37:26.800150+00:00`
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

- `news_risk_high->unknown_24h` score `49.3565` n `56` status `ready` deltaP `13.7649` edge `4.0758` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.1384` n `56` status `ready` deltaP `36.2351` edge `1.9906` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.3693` n `112` status `ready` deltaP `17.3363` edge `0.6551` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2819` n `80` status `ready` deltaP `10.9756` edge `0.5093` maxDD `-1.7183`
- `market_context_high->metal_24h` score `3.9073` n `112` status `ready` deltaP `30.754` edge `0.2225` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.8289` n `112` status `ready` deltaP `19.0113` edge `0.1497` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.6847` n `80` status `ready` deltaP `5.6737` edge `0.2216` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.5158` n `56` status `ready` deltaP `22.7431` edge `0.3601` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3925` n `80` status `ready` deltaP `34.8171` edge `0.0222` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `2.0022` n `56` status `ready` deltaP `19.2708` edge `0.3681` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.6272` n `56` status `ready` deltaP `36.1111` edge `0.0393` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.3216` n `56` status `ready` deltaP `19.0228` edge `0.0253` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.0791` n `119` status `ready` deltaP `8.7619` edge `0.0807` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7244` n `80` status `ready` deltaP `14.0419` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4338` n `80` status `ready` deltaP `12.3503` edge `0.0053` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.2565` n `112` status `ready` deltaP `7.5348` edge `0.0086` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.391` n `80` status `ready` deltaP `0.3069` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->crypto_major_4h` score `-0.4284` n `112` status `ready` deltaP `15.0262` edge `0.2092` maxDD `-20.9394`
- `news_risk_high->index_4h` score `-0.5285` n `80` status `ready` deltaP `1.9207` edge `-0.0164` maxDD `-1.7996`
- `market_context_high->crypto_alt_4h` score `-0.5712` n `112` status `ready` deltaP `17.4434` edge `0.2951` maxDD `-31.4361`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
