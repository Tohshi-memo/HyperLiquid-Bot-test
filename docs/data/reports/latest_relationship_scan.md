# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T22:52:27.442831+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6659`

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

- `market_context_high->unknown_24h` score `3621.5236` n `87` status `ready` deltaP `-11.7277` edge `301.9148` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `112.4757` n `87` status `ready` deltaP `1.0302` edge `9.3794` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `80.0776` n `108` status `ready` deltaP `-5.1951` edge `6.7364` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `17.9982` n `85` status `ready` deltaP `42.3427` edge `1.2358` maxDD `-0.7921`
- `market_context_high->equity_24h` score `10.659` n `87` status `ready` deltaP `22.4797` edge `1.0141` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.579` n `108` status `ready` deltaP `21.189` edge `0.4623` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9866` n `87` status `ready` deltaP `44.0194` edge `0.1404` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `1.5283` n `87` status `ready` deltaP `18.4837` edge `0.0676` maxDD `-0.4108`
- `market_context_high->metal_4h` score `1.4149` n `87` status `ready` deltaP `17.6391` edge `0.0428` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.8624` n `108` status `ready` deltaP `9.0264` edge `0.1071` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7396` n `87` status `ready` deltaP `10.7165` edge `0.0192` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.643` n `87` status `ready` deltaP `13.6179` edge `0.0019` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.4866` n `87` status `ready` deltaP `12.1223` edge `0.0` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.403` n `87` status `ready` deltaP `0.2698` edge `0.1892` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.3538` n `87` status `ready` deltaP `4.1727` edge `0.1051` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.1558` n `87` status `ready` deltaP `6.6212` edge `0.0786` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3842` n `87` status `ready` deltaP `-2.0287` edge `0.0157` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.5467` n `87` status `ready` deltaP `6.2859` edge `0.1527` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.6277` n `87` status `ready` deltaP `0.2753` edge `0.0017` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.7282` n `108` status `ready` deltaP `3.4043` edge `-0.0034` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
