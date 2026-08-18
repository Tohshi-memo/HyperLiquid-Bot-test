# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T12:16:05.236482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2793` n `85` status `ready` deltaP `8.27` edge `0.2556` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.557` n `85` status `ready` deltaP `17.0456` edge `0.2693` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0185` n `96` status `ready` deltaP `9.163` edge `0.0542` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.7675` n `96` status `ready` deltaP `14.7357` edge `0.0233` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6599` n `96` status `ready` deltaP `12.9179` edge `0.0076` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.6388` n `96` status `ready` deltaP `9.0193` edge `0.0952` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5292` n `96` status `ready` deltaP `9.2066` edge `0.0054` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.4358` n `96` status `ready` deltaP `10.3659` edge `0.0942` maxDD `-5.4926`
- `market_context_high->equity_4h` score `0.0395` n `96` status `ready` deltaP `2.6168` edge `0.0763` maxDD `-2.5696`
- `market_context_high->metal_1h` score `-0.0441` n `96` status `ready` deltaP `4.0232` edge `0.0082` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1186` n `85` status `ready` deltaP `13.3021` edge `-0.0808` maxDD `-0.0875`
- `market_context_high->fx_4h` score `-0.2076` n `96` status `ready` deltaP `3.5315` edge `0.0001` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.371` n `96` status `ready` deltaP `4.0905` edge `0.0102` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.3769` n `96` status `ready` deltaP `2.0771` edge `0.018` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4467` n `96` status `ready` deltaP `-3.4182` edge `0.0014` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4795` n `96` status `ready` deltaP `1.3348` edge `0.0141` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5921` n `96` status `ready` deltaP `0.7876` edge `0.0109` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8549` n `96` status `ready` deltaP `-7.142` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.0025` n `85` status `ready` deltaP `-6.7876` edge `0.0195` maxDD `-7.1455`
- `market_context_high->index_24h` score `-4.4851` n `85` status `ready` deltaP `-14.66` edge `-0.1785` maxDD `-12.5691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
