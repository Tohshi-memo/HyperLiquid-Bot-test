# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T09:07:32.960426+00:00`
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

- `news_risk_high->unknown_24h` score `43.6927` n `51` status `ready` deltaP `2.6042` edge `3.6237` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9484` n `51` status `ready` deltaP `25.3258` edge `0.9148` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.2521` n `51` status `ready` deltaP `37.4592` edge `0.6977` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.7692` n `51` status `ready` deltaP `46.5176` edge `0.1025` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.0887` n `51` status `ready` deltaP `36.5585` edge `0.0271` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0744` n `52` status `ready` deltaP `15.35` edge `0.1894` maxDD `-0.8426`
- `news_risk_high->equity_4h` score `2.6487` n `51` status `ready` deltaP `23.7267` edge `0.1396` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9543` n `133` status `ready` deltaP `19.7678` edge `0.0719` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1748` n `52` status `ready` deltaP `16.2137` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7587` n `52` status `ready` deltaP `16.8125` edge `0.0216` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.5046` n `51` status `ready` deltaP `10.3479` edge `0.0128` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.1948` n `52` status `ready` deltaP `8.5675` edge `-0.0096` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.0533` n `52` status `ready` deltaP `6.0226` edge `0.002` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0005` n `133` status `ready` deltaP `11.2725` edge `-0.0303` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.2763` n `51` status `ready` deltaP `6.1484` edge `-0.0109` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.4026` n `52` status `ready` deltaP `-0.3224` edge `-0.0088` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4989` n `133` status `ready` deltaP `1.4509` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6468` n `51` status `ready` deltaP `21.6503` edge `-0.194` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.6641` n `133` status `ready` deltaP `6.399` edge `-0.0343` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1544` n `133` status `ready` deltaP `-5.4725` edge `-0.0059` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
