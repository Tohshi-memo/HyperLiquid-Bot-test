# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T01:07:26.954933+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6231`

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

- `market_context_high->unknown_24h` score `4305.7209` n `78` status `ready` deltaP `-10.657` edge `358.9241` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `167.3244` n `78` status `ready` deltaP `1.3641` edge `13.9479` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `76.492` n `108` status `ready` deltaP `-5.1951` edge `6.4376` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.7985` n `92` status `ready` deltaP `35.0921` edge `1.1166` maxDD `-6.3871`
- `market_context_high->equity_24h` score `11.2271` n `78` status `ready` deltaP `21.3141` edge `1.0591` maxDD `-13.5818`
- `news_risk_high->crypto_alt_4h` score `5.5404` n `108` status `ready` deltaP `21.0366` edge `0.4601` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.1702` n `78` status `ready` deltaP `45.0988` edge `0.1485` maxDD `-0.1315`
- `market_context_high->unknown_1h` score `4.1368` n `78` status `ready` deltaP `4.349` edge `0.3268` maxDD `-0.2178`
- `market_context_high->commodity_4h` score `2.4539` n `78` status `ready` deltaP `24.5388` edge `0.0743` maxDD `-0.3387`
- `news_risk_high->crypto_alt_1h` score `0.872` n `108` status `ready` deltaP `9.0264` edge `0.1079` maxDD `-3.9659`
- `market_context_high->fx_1h` score `0.8408` n `78` status `ready` deltaP `13.2888` edge `-0.0001` maxDD `-0.1407`
- `market_context_high->metal_4h` score `0.7585` n `78` status `ready` deltaP `14.5247` edge `0.0429` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.6989` n `78` status `ready` deltaP `10.0875` edge `0.02` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.6478` n `78` status `ready` deltaP `13.6179` edge `0.0023` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.203` n `78` status `ready` deltaP `0.5988` edge `0.1096` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.1869` n `78` status `ready` deltaP `-4.366` edge `0.1924` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `-0.0981` n `78` status `ready` deltaP `3.1629` edge `0.0691` maxDD `-5.2213`
- `market_context_high->commodity_24h` score `-0.3286` n `78` status `ready` deltaP `22.8633` edge `0.0731` maxDD `-13.7454`
- `market_context_high->commodity_1h` score `-0.3979` n `78` status `ready` deltaP `0.1305` edge `0.0174` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4734` n `78` status `ready` deltaP `-0.9827` edge `0.0017` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
