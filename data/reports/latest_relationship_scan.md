# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T04:37:32.531364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4584`

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

- `news_risk_high->crypto_alt_24h` score `0.3212` n `127` status `ready` deltaP `22.9809` edge `0.8802` maxDD `-68.3781`
- `news_risk_high->crypto_alt_4h` score `0.1593` n `146` status `ready` deltaP `5.1704` edge `0.2496` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4706` n `146` status `ready` deltaP `1.5831` edge `0.0519` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5868` n `146` status `ready` deltaP `-0.4265` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.812` n `127` status `ready` deltaP `13.1411` edge `0.1339` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9035` n `146` status `ready` deltaP `1.1976` edge `-0.0033` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2167` n `146` status `ready` deltaP `-3.0488` edge `-0.0105` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2915` n `146` status `ready` deltaP `-5.098` edge `-0.0094` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-1.6755` n `127` status `ready` deltaP `18.1198` edge `0.6739` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.0478` n `127` status `ready` deltaP `-1.9124` edge `0.0344` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1484` n `146` status `ready` deltaP `-4.3414` edge `-0.0164` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3888` n `146` status `ready` deltaP `-9.0764` edge `-0.0019` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4942` n `127` status `ready` deltaP `-19.7698` edge `-0.0171` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7038` n `146` status `ready` deltaP `-6.9354` edge `-0.0328` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2307` n `146` status `ready` deltaP `-8.1556` edge `-0.0423` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7916` n `146` status `ready` deltaP `-12.1701` edge `0.0006` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9117` n `146` status `ready` deltaP `-7.7577` edge `-0.0371` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.073` n `146` status `ready` deltaP `-14.2312` edge `-0.0926` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.5777` n `127` status `ready` deltaP `-12.7187` edge `0.0769` maxDD `-45.2198`
- `news_risk_high->commodity_24h` score `-11.2735` n `127` status `ready` deltaP `-24.486` edge `-0.0767` maxDD `-33.6283`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
