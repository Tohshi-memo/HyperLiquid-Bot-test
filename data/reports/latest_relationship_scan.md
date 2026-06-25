# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T10:37:30.427809+00:00`
- Price records: `672`
- Market context records: `4715`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7424`

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

- `market_context_high->unknown_1h` score `76.9568` n `144` status `ready` deltaP `14.1634` edge `6.3604` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.0485` n `144` status `ready` deltaP `13.7026` edge `0.4504` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.9773` n `135` status `ready` deltaP `15.4862` edge `0.2372` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.303` n `144` status `ready` deltaP `2.4077` edge `0.0247` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6791` n `144` status `ready` deltaP `4.4716` edge `-0.0046` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.9235` n `144` status `ready` deltaP `9.1294` edge `0.0315` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.9311` n `144` status `ready` deltaP `-1.355` edge `-0.0021` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-1.0841` n `144` status `ready` deltaP `2.7947` edge `0.0193` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1809` n `144` status `ready` deltaP `-1.7423` edge `0.0119` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2948` n `144` status `ready` deltaP `-5.1356` edge `-0.0057` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6193` n `144` status `ready` deltaP `-3.7841` edge `-0.0093` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.1535` n `144` status `ready` deltaP `-0.6404` edge `-0.0713` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.6592` n `144` status `ready` deltaP `-0.8317` edge `-0.0883` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.3919` n `135` status `ready` deltaP `17.1065` edge `0.0704` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4018` n `144` status `ready` deltaP `-5.1772` edge `-0.0755` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.8009` n `135` status `ready` deltaP `-13.044` edge `-0.0171` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.0331` n `144` status `ready` deltaP `-2.185` edge `-0.1496` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.4071` n `135` status `ready` deltaP `-10.6366` edge `-0.0922` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.6142` n `144` status `ready` deltaP `3.3537` edge `-0.2414` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.7601` n `144` status `ready` deltaP `-2.5745` edge `-0.2723` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
