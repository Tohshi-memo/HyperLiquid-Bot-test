# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T02:37:26.980881+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `1.041` n `68` status `ready` deltaP `8.42` edge `0.1554` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7533` n `68` status `ready` deltaP `13.3877` edge `0.0213` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3021` n `68` status `ready` deltaP `8.9767` edge `0.1457` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0331` n `68` status `ready` deltaP `6.9567` edge `0.0032` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `-0.1416` n `68` status `ready` deltaP `-3.1862` edge `0.0537` maxDD `-0.2073`
- `news_risk_high->fx_4h` score `-0.1534` n `68` status `ready` deltaP `3.2281` edge `0.0034` maxDD `-0.2336`
- `news_risk_high->equity_1h` score `-0.207` n `68` status `ready` deltaP `-2.3688` edge `0.0442` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2928` n `68` status `ready` deltaP `-0.0792` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4861` n `68` status `ready` deltaP `-2.9676` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2339` n `68` status `ready` deltaP `-4.071` edge `-0.0405` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.6639` n `68` status `ready` deltaP `-6.6894` edge `-0.0083` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-2.1325` n `68` status `ready` deltaP `-14.2832` edge `-0.0039` maxDD `-1.2868`
- `news_risk_high->crypto_major_1h` score `-2.3645` n `68` status `ready` deltaP `-9.6689` edge `-0.0387` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.5355` n `68` status `ready` deltaP `-5.9792` edge `-0.0539` maxDD `-5.4024`
- `news_risk_high->crypto_alt_4h` score `-2.7837` n `68` status `ready` deltaP `-7.2991` edge `-0.0462` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.5017` n `68` status `ready` deltaP `-2.3897` edge `-0.2434` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.7422` n `68` status `ready` deltaP `23.366` edge `0.5231` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.6431` n `68` status `ready` deltaP `-32.2991` edge `-0.0118` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.3743` n `68` status `ready` deltaP `-29.8815` edge `-0.0974` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.4288` n `68` status `ready` deltaP `-29.136` edge `-0.0745` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
