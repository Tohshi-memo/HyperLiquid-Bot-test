# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T03:07:27.736760+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `25.7956` n `142` status `ready` deltaP `-15.2037` edge `2.4964` maxDD `-9.6329`
- `market_context_high->fx_24h` score `1.0462` n `142` status `ready` deltaP `19.8819` edge `0.0354` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9197` n `168` status `ready` deltaP `12.4201` edge `0.0653` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6789` n `180` status `ready` deltaP `9.3114` edge `0.0288` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1856` n `180` status `ready` deltaP `3.3101` edge `-0.0007` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1983` n `168` status `ready` deltaP `4.4788` edge `0.0047` maxDD `-0.4647`
- `market_context_high->index_1h` score `-0.8404` n `180` status `ready` deltaP `-6.67` edge `-0.0045` maxDD `-1.0359`
- `market_context_high->metal_1h` score `-1.2996` n `180` status `ready` deltaP `-5.2195` edge `-0.0099` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4778` n `180` status `ready` deltaP `-6.4604` edge `-0.0187` maxDD `-6.8818`
- `market_context_high->commodity_24h` score `-1.7432` n `142` status `ready` deltaP `8.757` edge `0.0984` maxDD `-22.0881`
- `market_context_high->index_4h` score `-1.8188` n `168` status `ready` deltaP `-6.8162` edge `-0.0167` maxDD `-1.4875`
- `market_context_high->metal_24h` score `-1.8258` n `142` status `ready` deltaP `2.0528` edge `-0.0334` maxDD `-2.9283`
- `market_context_high->index_24h` score `-2.2679` n `142` status `ready` deltaP `-10.1277` edge `-0.0137` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.7186` n `180` status `ready` deltaP `-9.9201` edge `-0.0419` maxDD `-6.4812`
- `market_context_high->metal_4h` score `-3.1709` n `168` status `ready` deltaP `-7.6582` edge `-0.0368` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.5633` n `180` status `ready` deltaP `-8.6128` edge `-0.0491` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.4487` n `168` status `ready` deltaP `-16.3545` edge `-0.1504` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.5976` n `168` status `ready` deltaP `-11.7887` edge `-0.1364` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-6.7165` n `142` status `ready` deltaP `-13.3131` edge `-0.1952` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.4687` n `142` status `ready` deltaP `-12.4856` edge `-0.226` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
