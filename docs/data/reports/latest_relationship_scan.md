# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T11:07:27.043241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `43.6139` n `51` status `ready` deltaP `2.0833` edge `3.6206` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0138` n `51` status `ready` deltaP `25.7831` edge `0.9172` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `9.7558` n `51` status `ready` deltaP `36.0703` edge `0.6656` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.6041` n `51` status `ready` deltaP `45.1287` edge `0.098` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1487` n `52` status `ready` deltaP `15.9488` edge `0.1916` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.1155` n `51` status `ready` deltaP `36.8633` edge `0.0273` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.3894` n `51` status `ready` deltaP `22.6596` edge `0.1251` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0197` n `133` status `ready` deltaP `20.2251` edge `0.0743` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2` n `52` status `ready` deltaP `16.5131` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7595` n `52` status `ready` deltaP `16.8125` edge `0.0217` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4062` n `51` status `ready` deltaP `9.4333` edge `0.0107` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.25` n `52` status `ready` deltaP `9.0166` edge `-0.008` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.0738` n `133` status `ready` deltaP `11.8713` edge `-0.0281` maxDD `-1.5916`
- `news_risk_high->index_1h` score `0.0518` n `52` status `ready` deltaP `6.0226` edge `0.0018` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2823` n `51` status `ready` deltaP `6.1484` edge `-0.0114` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3906` n `52` status `ready` deltaP `-0.1727` edge `-0.0088` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4825` n `133` status `ready` deltaP `1.7503` edge `-0.0003` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.6701` n `133` status `ready` deltaP `6.399` edge `-0.0348` maxDD `-2.4293`
- `news_risk_high->metal_24h` score `-0.6852` n `51` status `ready` deltaP `21.6503` edge `-0.1972` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.1568` n `133` status `ready` deltaP `-5.4725` edge `-0.0061` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
