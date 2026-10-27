# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T10:07:28.326280+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9402`

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

- `market_context_high->unknown_4h` score `87.5133` n `135` status `ready` deltaP `5.4619` edge `7.2716` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.4511` n `135` status `ready` deltaP `1.5181` edge `1.3264` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.8855` n `128` status `ready` deltaP `26.6573` edge `0.0482` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4979` n `135` status `ready` deltaP `11.0557` edge `0.0036` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4749` n `135` status `ready` deltaP `13.3537` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0842` n `135` status `ready` deltaP `11.0945` edge `0.0115` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3417` n `135` status `ready` deltaP `1.8286` edge `0.0094` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4677` n `135` status `ready` deltaP `5.7363` edge `0.0301` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5399` n `135` status `ready` deltaP `0.0865` edge `-0.0015` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.6406` n `135` status `ready` deltaP `10.1479` edge `0.0043` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.6884` n `128` status `ready` deltaP `7.5417` edge `0.0187` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.7365` n `135` status `ready` deltaP `3.9453` edge `0.0342` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-0.9381` n `128` status `ready` deltaP `14.4606` edge `0.0892` maxDD `-7.1026`
- `market_context_high->equity_1h` score `-1.3303` n `135` status `ready` deltaP `2.6391` edge `0.0031` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9374` n `135` status `ready` deltaP `-1.0413` edge `-0.0051` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.468` n `135` status `ready` deltaP `-3.1166` edge `-0.0227` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-2.6943` n `128` status `ready` deltaP `6.4354` edge `0.029` maxDD `-15.7143`
- `market_context_high->crypto_major_4h` score `-3.5721` n `135` status `ready` deltaP `4.4219` edge `-0.0555` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.6045` n `128` status `ready` deltaP `-1.1265` edge `-0.0971` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7053` n `135` status `ready` deltaP `3.9194` edge `-0.106` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
