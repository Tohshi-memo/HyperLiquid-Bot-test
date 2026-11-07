# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T05:37:29.649296+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4184`

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

- `news_risk_high->equity_4h` score `1.2663` n `63` status `ready` deltaP `11.7524` edge `0.1579` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.9095` n `63` status `ready` deltaP `15.2947` edge `0.0216` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3959` n `63` status `ready` deltaP `10.6151` edge `0.1468` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.1684` n `63` status `ready` deltaP `-1.0168` edge `0.065` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.1308` n `63` status `ready` deltaP `8.7896` edge `0.0035` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0628` n `63` status `ready` deltaP `-0.1045` edge `0.0476` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1525` n `63` status `ready` deltaP `2.5022` edge `0.0023` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2764` n `63` status `ready` deltaP `0.8034` edge `0.0038` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5428` n `63` status `ready` deltaP `-4.0277` edge `-0.007` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.1169` n `63` status `ready` deltaP `-1.7615` edge `-0.0409` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2887` n `63` status `ready` deltaP `-3.1604` edge `-0.0286` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.3407` n `63` status `ready` deltaP `-3.8788` edge `0.0144` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6108` n `63` status `ready` deltaP `-11.3654` edge `-0.0023` maxDD `-1.1598`
- `news_risk_high->crypto_major_1h` score `-1.8477` n `63` status `ready` deltaP `-6.9338` edge `-0.026` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.3253` n `63` status `ready` deltaP `-4.1836` edge `-0.0082` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.7611` n `63` status `ready` deltaP `-5.3075` edge `-0.2572` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.4358` n `63` status `ready` deltaP `-30.2531` edge `-0.0108` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.5944` n `63` status `ready` deltaP `21.0318` edge `0.4294` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6039` n `63` status `ready` deltaP `-29.0675` edge `-0.1235` maxDD `-27.9769`
- `news_risk_high->crypto_major_24h` score `-14.1878` n `63` status `ready` deltaP `-30.1339` edge `-0.1311` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
