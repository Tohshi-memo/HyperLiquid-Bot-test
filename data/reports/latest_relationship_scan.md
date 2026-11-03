# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T05:07:28.466444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4564`

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

- `news_risk_high->crypto_alt_4h` score `0.1884` n `146` status `ready` deltaP `5.4753` edge `0.2513` maxDD `-14.0916`
- `news_risk_high->crypto_alt_24h` score `-0.0494` n `128` status `ready` deltaP `22.8298` edge `0.8754` maxDD `-71.3817`
- `news_risk_high->crypto_alt_1h` score `-0.4729` n `146` status `ready` deltaP `1.5831` edge `0.0516` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5953` n `146` status `ready` deltaP `-0.5762` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8151` n `128` status `ready` deltaP `13.0208` edge `0.1343` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9047` n `146` status `ready` deltaP `1.1976` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.208` n `146` status `ready` deltaP `-2.8963` edge `-0.0104` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2915` n `146` status `ready` deltaP `-5.098` edge `-0.0094` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-1.7379` n `128` status `ready` deltaP `17.9687` edge `0.6669` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.0516` n `128` status `ready` deltaP `-1.9097` edge `0.0339` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1484` n `146` status `ready` deltaP `-4.3414` edge `-0.0164` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.39` n `146` status `ready` deltaP `-9.0764` edge `-0.002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4961` n `128` status `ready` deltaP `-19.7917` edge `-0.0172` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7038` n `146` status `ready` deltaP `-6.9354` edge `-0.0328` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2439` n `146` status `ready` deltaP `-8.3053` edge `-0.0424` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7856` n `146` status `ready` deltaP `-12.1701` edge `0.0011` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9045` n `146` status `ready` deltaP `-7.7577` edge `-0.0365` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.061` n `146` status `ready` deltaP `-14.2312` edge `-0.0916` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.8444` n `128` status `ready` deltaP `-12.5868` edge `0.0785` maxDD `-47.1967`
- `news_risk_high->commodity_24h` score `-11.3914` n `128` status `ready` deltaP `-24.2188` edge `-0.0781` maxDD `-34.4447`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
