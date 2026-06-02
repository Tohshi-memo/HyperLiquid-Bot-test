# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T03:07:20.875053+00:00`
- Price records: `672`
- Market context records: `2623`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.6554` n `146` status `ready` deltaP `18.2958` edge `0.5488` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0369` n `146` status `ready` deltaP `24.8914` edge `0.5217` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.2225` n `146` status `ready` deltaP `14.0014` edge `0.3562` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.3004` n `146` status `ready` deltaP `11.2809` edge `0.1519` maxDD `-6.1656`
- `market_context_high->index_24h` score `1.0784` n `146` status `ready` deltaP `10.1907` edge `0.12` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `1.0577` n `146` status `ready` deltaP `7.5321` edge `0.1429` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6789` n `146` status `ready` deltaP `8.7134` edge `0.1179` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.5344` n `146` status `ready` deltaP `2.0643` edge `0.6686` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2698` n `146` status `ready` deltaP `8.9751` edge `0.0468` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0988` n `146` status `ready` deltaP `4.2408` edge `0.0129` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.276` n `146` status `ready` deltaP `1.8005` edge `0.0313` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.2984` n `146` status `ready` deltaP `6.2505` edge `0.0213` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6812` n `146` status `ready` deltaP `1.1115` edge `0.0106` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.718` n `146` status `ready` deltaP `-1.4334` edge `0.0032` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.854` n `146` status `ready` deltaP `-0.6767` edge `0.0172` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-0.8916` n `146` status `ready` deltaP `5.1683` edge `0.0455` maxDD `-10.2078`
- `market_context_high->fx_24h` score `-0.9939` n `146` status `ready` deltaP `3.0203` edge `-0.0036` maxDD `-1.6157`
- `market_context_high->metal_4h` score `-1.0055` n `146` status `ready` deltaP `2.9777` edge `0.0351` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-1.0285` n `146` status `ready` deltaP `-1.445` edge `0.0097` maxDD `-0.8621`
- `market_context_high->equity_4h` score `-1.3542` n `146` status `ready` deltaP `1.6497` edge `0.0166` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
