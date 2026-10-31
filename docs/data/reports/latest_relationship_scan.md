# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T23:52:32.560723+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6775`

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

- `market_context_high->unknown_24h` score `3907.4041` n `83` status `ready` deltaP `-10.607` edge `325.7307` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `135.5479` n `83` status `ready` deltaP `0.6979` edge `11.3043` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `80.0596` n `108` status `ready` deltaP `-5.1951` edge `6.7349` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `16.2571` n `89` status `ready` deltaP `38.0598` edge `1.1714` maxDD `-3.6296`
- `market_context_high->equity_24h` score `10.6437` n `83` status `ready` deltaP `21.2684` edge `1.0209` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.6032` n `108` status `ready` deltaP `21.3415` edge `0.4633` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.0046` n `83` status `ready` deltaP `44.0491` edge `0.1417` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `1.9733` n `83` status `ready` deltaP `20.976` edge `0.0705` maxDD `-0.3387`
- `market_context_high->metal_4h` score `1.2755` n `83` status `ready` deltaP `15.8665` edge `0.043` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.9344` n `108` status `ready` deltaP `9.4755` edge `0.1101` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7016` n `83` status `ready` deltaP `10.2265` edge `0.0193` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.6864` n `83` status `ready` deltaP `14.1162` edge `0.0022` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.5226` n `83` status `ready` deltaP `12.8147` edge `0.0` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.321` n `83` status `ready` deltaP `-1.5023` edge `0.1905` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.2744` n `83` status `ready` deltaP `2.406` edge `0.1067` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0044` n `83` status `ready` deltaP `4.9654` edge `0.0691` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.2726` n `83` status `ready` deltaP `-0.018` edge `0.0166` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4066` n `83` status `ready` deltaP `0.303` edge `0.0017` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.7282` n `108` status `ready` deltaP `3.4043` edge `-0.0034` maxDD `-1.3981`
- `market_context_high->metal_24h` score `-0.7817` n `83` status `ready` deltaP `3.627` edge `0.1403` maxDD `-10.5088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
