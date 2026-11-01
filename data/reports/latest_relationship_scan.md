# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T00:52:26.881605+00:00`
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

- `market_context_high->unknown_24h` score `4222.0571` n `79` status `ready` deltaP `-10.4298` edge `351.9506` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `160.6037` n `79` status `ready` deltaP `1.4453` edge `13.3873` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `76.5064` n `108` status `ready` deltaP `-5.1951` edge `6.4388` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.8165` n `92` status `ready` deltaP `35.0921` edge `1.1181` maxDD `-6.3871`
- `market_context_high->equity_24h` score `10.8809` n `79` status `ready` deltaP `20.4377` edge `1.0462` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.5634` n `108` status `ready` deltaP `21.189` edge `0.461` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.0556` n `79` status `ready` deltaP `44.0115` edge `0.1462` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.3802` n `79` status `ready` deltaP `23.7824` edge `0.0732` maxDD `-0.3387`
- `market_context_high->metal_4h` score `1.2096` n `79` status `ready` deltaP `15.0278` edge `0.0431` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.8948` n `108` status `ready` deltaP `9.1761` edge `0.1088` maxDD `-3.9659`
- `market_context_high->unknown_1h` score `0.8543` n `79` status `ready` deltaP `4.4626` edge `0.0525` maxDD `-0.2178`
- `market_context_high->fx_4h` score `0.6815` n `79` status `ready` deltaP `14.0398` edge `0.0023` maxDD `-0.1285`
- `market_context_high->metal_1h` score `0.638` n `79` status `ready` deltaP `9.3572` edge `0.0198` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5105` n `79` status `ready` deltaP `12.6109` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.2581` n `79` status `ready` deltaP `0.1156` edge `0.1083` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.2185` n `79` status `ready` deltaP `-3.6682` edge `0.1918` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `-0.0685` n `79` status `ready` deltaP `3.7634` edge `0.0689` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.4519` n `79` status `ready` deltaP `-0.47` edge `0.0169` maxDD `-0.4475`
- `market_context_high->commodity_24h` score `-0.4754` n `79` status `ready` deltaP `22.2903` edge `0.0683` maxDD `-14.228`
- `market_context_high->index_1h` score `-0.5063` n `79` status `ready` deltaP `-1.5993` edge `0.0016` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
