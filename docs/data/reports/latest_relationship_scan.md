# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T02:07:29.817952+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9972`

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

- `market_context_high->unknown_4h` score `46.4662` n `47` status `ready` deltaP `7.3171` edge `3.8234` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `34.4194` n `47` status `ready` deltaP `22.2628` edge `2.7887` maxDD `-4.5065`
- `market_context_high->crypto_alt_24h` score `18.848` n `47` status `ready` deltaP `20.9626` edge `1.4864` maxDD `-4.1052`
- `market_context_high->equity_24h` score `16.7508` n `47` status `ready` deltaP `15.492` edge `1.3265` maxDD `-1.7104`
- `news_risk_high->crypto_major_24h` score `9.7562` n `101` status `ready` deltaP `-1.0572` edge `1.5059` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.4911` n `47` status `ready` deltaP `19.4851` edge `0.3426` maxDD `-0.1926`
- `news_risk_high->crypto_alt_24h` score `5.2958` n `101` status `ready` deltaP `-0.6721` edge `0.9339` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `2.8712` n `101` status `ready` deltaP `14.041` edge `0.2666` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.6274` n `101` status `ready` deltaP `32.2246` edge `0.2526` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3325` n `101` status `ready` deltaP `14.1356` edge `0.1467` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1368` n `101` status `ready` deltaP `16.3276` edge `0.195` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.7671` n `47` status `ready` deltaP `21.8312` edge `0.0206` maxDD `-0.1773`
- `news_risk_high->crypto_major_1h` score `1.6995` n `101` status `ready` deltaP `16.2314` edge `0.0857` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `0.8789` n `47` status `ready` deltaP `8.1636` edge `0.079` maxDD `-2.8148`
- `market_context_high->equity_4h` score `0.8233` n `47` status `ready` deltaP `7.3884` edge `0.0563` maxDD `-0.9558`
- `market_context_high->equity_1h` score `0.7965` n `47` status `ready` deltaP `6.3766` edge `0.0483` maxDD `-0.2885`
- `news_risk_high->fx_4h` score `0.626` n `101` status `ready` deltaP `12.909` edge `0.0297` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.5298` n `101` status `ready` deltaP `13.6998` edge `0.013` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5168` n `47` status `ready` deltaP `8.6221` edge `0.0109` maxDD `-0.0249`
- `market_context_high->crypto_major_1h` score `0.2851` n `47` status `ready` deltaP `0.4109` edge `0.0796` maxDD `-2.3531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
