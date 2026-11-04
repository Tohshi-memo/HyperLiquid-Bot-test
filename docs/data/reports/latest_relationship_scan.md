# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T20:52:29.307185+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3932`

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

- `news_risk_high->crypto_alt_4h` score `0.2207` n `146` status `ready` deltaP `8.6765` edge `0.2341` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3935` n `146` status `ready` deltaP `3.3795` edge `0.0498` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6568` n `146` status `ready` deltaP `-1.7738` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7957` n `146` status `ready` deltaP `2.3952` edge `-0.0023` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4083` n `146` status `ready` deltaP `-6.595` edge `-0.0144` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4545` n `146` status `ready` deltaP `-7.622` edge `-0.0105` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9153` n `146` status `ready` deltaP `-0.6828` edge `-0.0109` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2317` n `146` status `ready` deltaP `-8.4776` edge `0.0072` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3136` n `146` status `ready` deltaP `-6.4535` edge `0.0306` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4574` n `146` status `ready` deltaP `-18.8368` edge `-0.0186` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5822` n `146` status `ready` deltaP `-6.1869` edge `-0.0222` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1745` n `146` status `ready` deltaP `-6.6586` edge `-0.0476` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.209` n `146` status `ready` deltaP `-9.8835` edge `0.0339` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-4.0104` n `146` status `ready` deltaP `1.7088` edge `0.0126` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.9251` n `146` status `ready` deltaP `-6.0809` edge `-0.0494` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0487` n `146` status `ready` deltaP `-11.1824` edge `-0.1109` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.5197` n `146` status `ready` deltaP `13.438` edge `0.3894` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9957` n `146` status `ready` deltaP `-0.2255` edge `-0.0787` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.6335` n `146` status `ready` deltaP `11.8809` edge `0.4017` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-11.8781` n `146` status `ready` deltaP `-20.6807` edge `-0.0259` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
