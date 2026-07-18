# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T03:22:29.485473+00:00`
- Price records: `672`
- Market context records: `7097`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.4299` n `158` status `ready` deltaP `16.6815` edge `0.0139` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1432` n `158` status `ready` deltaP `4.5119` edge `0.0031` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2112` n `158` status `ready` deltaP `-0.1706` edge `0.0394` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.4396` n `158` status `ready` deltaP `0.5514` edge `0.0264` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4675` n `158` status `ready` deltaP `1.1426` edge `-0.0056` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6005` n `158` status `ready` deltaP `3.3825` edge `0.0357` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8354` n `158` status `ready` deltaP `-3.9263` edge `-0.0193` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3616` n `158` status `ready` deltaP `-4.1892` edge `-0.0431` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4683` n `158` status `ready` deltaP `-6.0714` edge `-0.0051` maxDD `-2.1427`
- `market_context_high->unknown_4h` score `-1.6505` n `158` status `ready` deltaP `-7.5312` edge `-0.0012` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0875` n `158` status `ready` deltaP `2.4085` edge `-0.0414` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3839` n `158` status `ready` deltaP `0.8818` edge `-0.0416` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-3.0108` n `158` status `ready` deltaP `4.1024` edge `0.0151` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.1045` n `158` status `ready` deltaP `-6.439` edge `-0.0849` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.1716` n `158` status `ready` deltaP `-1.0767` edge `-0.0209` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.2417` n `158` status `ready` deltaP `-7.7795` edge `-0.0189` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.3129` n `158` status `ready` deltaP `-7.6336` edge `-0.0102` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.4601` n `158` status `ready` deltaP `0.7062` edge `-0.2023` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.8202` n `158` status `ready` deltaP `-23.3012` edge `-0.065` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.0591` n `158` status `ready` deltaP `-24.8704` edge `-0.1353` maxDD `-43.3059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
