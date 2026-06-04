# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T01:52:19.929788+00:00`
- Price records: `672`
- Market context records: `2821`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.3579` n `142` status `ready` deltaP `2.9489` edge `0.2233` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.8592` n `142` status `ready` deltaP `6.1856` edge `0.1357` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7756` n `142` status `ready` deltaP `11.7322` edge `0.2958` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.2933` n `142` status `ready` deltaP `13.1484` edge `0.0341` maxDD `-2.3986`
- `market_context_high->crypto_alt_24h` score `0.1566` n `142` status `ready` deltaP `-0.5966` edge `0.4087` maxDD `-22.6673`
- `market_context_high->unknown_1h` score `0.1485` n `142` status `ready` deltaP `5.0793` edge `0.0516` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0789` n `142` status `ready` deltaP `4.198` edge `0.0113` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5359` n `142` status `ready` deltaP `-0.5376` edge `0.0033` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6094` n `142` status `ready` deltaP `0.0169` edge `-0.0029` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.657` n `142` status `ready` deltaP `5.2459` edge `0.0568` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7051` n `142` status `ready` deltaP `0.1328` edge `-0.0067` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8687` n `142` status `ready` deltaP `3.926` edge `0.0494` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9027` n `142` status `ready` deltaP `-2.7494` edge `0.0264` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.118` n `142` status `ready` deltaP `2.1148` edge `0.0307` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1787` n `142` status `ready` deltaP `-4.0579` edge `0.0067` maxDD `-0.5631`
- `market_context_high->index_24h` score `-1.3182` n `142` status `ready` deltaP `1.384` edge `-0.021` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `-1.3561` n `142` status `ready` deltaP `1.8378` edge `0.0059` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.7061` n `142` status `ready` deltaP `-4.663` edge `-0.0239` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-2.0367` n `142` status `ready` deltaP `13.1183` edge `0.1769` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.3838` n `142` status `ready` deltaP `-1.0756` edge `-0.0434` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
