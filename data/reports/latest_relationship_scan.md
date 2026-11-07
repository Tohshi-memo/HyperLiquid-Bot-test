# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T11:22:28.220589+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4001`

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

- `market_context_high->equity_1h` score `3.512` n `33` status `ready` deltaP `10.0073` edge `0.2719` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.2375` n `62` status `ready` deltaP `11.3788` edge `0.1567` maxDD `-4.2454`
- `market_context_high->fx_1h` score `0.6631` n `33` status `ready` deltaP `9.8939` edge `0.0164` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.6251` n `62` status `ready` deltaP `11.8607` edge `0.0208` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.6236` n `33` status `ready` deltaP `5.294` edge `0.0437` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.3345` n `62` status `ready` deltaP `9.9294` edge `0.1435` maxDD `-6.6786`
- `market_context_high->crypto_major_1h` score `0.3325` n `33` status `ready` deltaP `6.9407` edge `0.0549` maxDD `-3.0172`
- `market_context_high->metal_1h` score `0.2608` n `33` status `ready` deltaP `6.977` edge `0.0197` maxDD `-0.6226`
- `market_context_high->crypto_alt_1h` score `0.207` n `33` status `ready` deltaP `7.9886` edge `0.0548` maxDD `-3.1881`
- `market_context_high->commodity_1h` score `0.0915` n `33` status `ready` deltaP `8.66` edge `0.0086` maxDD `-1.7019`
- `news_risk_high->fx_24h` score `0.053` n `62` status `ready` deltaP `-2.7442` edge `0.0669` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0466` n `62` status `ready` deltaP `7.2001` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0939` n `62` status `ready` deltaP `-0.5988` edge `0.0469` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1394` n `62` status `ready` deltaP `2.7091` edge `0.0026` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.1866` n `62` status `ready` deltaP `2.4243` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5314` n `62` status `ready` deltaP `-3.8246` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9475` n `62` status `ready` deltaP `1.4211` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1338` n `62` status `ready` deltaP `-1.3956` edge `-0.0205` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2312` n `62` status `ready` deltaP `-2.7046` edge `0.0206` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.635` n `62` status `ready` deltaP `-11.6235` edge `-0.0028` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
