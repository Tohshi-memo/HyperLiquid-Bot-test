# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T11:37:32.355039+00:00`
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

- `market_context_high->equity_1h` score `3.5219` n `34` status `ready` deltaP `11.0162` edge `0.266` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.228` n `62` status `ready` deltaP `11.2264` edge `0.1565` maxDD `-4.2454`
- `market_context_high->index_1h` score `0.7078` n `34` status `ready` deltaP `6.4812` edge `0.0428` maxDD `-0.1621`
- `market_context_high->crypto_major_1h` score `0.652` n `34` status `ready` deltaP `8.2776` edge `0.0577` maxDD `-3.0172`
- `news_risk_high->index_4h` score `0.6129` n `62` status `ready` deltaP `11.7083` edge `0.0208` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.5038` n `34` status `ready` deltaP `8.0222` edge `0.0156` maxDD `-0.1681`
- `news_risk_high->index_24h` score `0.3443` n `62` status `ready` deltaP `10.103` edge `0.1436` maxDD `-6.6786`
- `market_context_high->crypto_alt_1h` score `0.289` n `34` status `ready` deltaP `9.3255` edge `0.0564` maxDD `-3.1881`
- `market_context_high->metal_1h` score `0.1649` n `34` status `ready` deltaP `5.2836` edge `0.0187` maxDD `-0.6226`
- `market_context_high->commodity_1h` score `0.1587` n `34` status `ready` deltaP `9.8186` edge `0.0095` maxDD `-1.7019`
- `news_risk_high->fx_24h` score `0.053` n `62` status `ready` deltaP `-2.7442` edge `0.0669` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0388` n `62` status `ready` deltaP `7.0504` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.1025` n `62` status `ready` deltaP `-0.7485` edge `0.0468` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1394` n `62` status `ready` deltaP `2.7091` edge `0.0026` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.1945` n `62` status `ready` deltaP `2.2718` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5314` n `62` status `ready` deltaP `-3.8246` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9396` n `62` status `ready` deltaP `1.5736` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1338` n `62` status `ready` deltaP `-1.3956` edge `-0.0205` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2312` n `62` status `ready` deltaP `-2.7046` edge `0.0206` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.635` n `62` status `ready` deltaP `-11.6235` edge `-0.0028` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
