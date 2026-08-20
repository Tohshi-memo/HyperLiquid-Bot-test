# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T08:37:24.299465+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10800`

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

- `market_context_high->equity_4h` score `1.7946` n `96` status `ready` deltaP `9.629` edge `0.1742` maxDD `-2.4411`
- `market_context_high->equity_1h` score `0.9903` n `101` status `ready` deltaP `10.9474` edge `0.0575` maxDD `-1.8363`
- `market_context_high->index_1h` score `0.5175` n `101` status `ready` deltaP `11.6618` edge `0.0067` maxDD `-0.3054`
- `market_context_high->metal_4h` score `0.3808` n `96` status `ready` deltaP `12.6016` edge `0.0053` maxDD `-1.273`
- `market_context_high->index_4h` score `0.0683` n `96` status `ready` deltaP `7.6473` edge `0.0202` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.018` n `96` status `ready` deltaP `5.5556` edge `0.1486` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0146` n `96` status `ready` deltaP `6.7327` edge `0.0035` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1907` n `101` status `ready` deltaP `3.0162` edge `0.0027` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.215` n `101` status `ready` deltaP `7.0211` edge `-0.042` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.2216` n `101` status `ready` deltaP `0.6107` edge `0.0034` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.6124` n `101` status `ready` deltaP `0.5632` edge `-0.0021` maxDD `-2.413`
- `market_context_high->unknown_24h` score `-0.6453` n `96` status `ready` deltaP `17.7083` edge `-0.1212` maxDD `-1.0505`
- `market_context_high->crypto_major_1h` score `-0.6806` n `101` status `ready` deltaP `2.5671` edge `-0.0199` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.878` n `101` status `ready` deltaP `-7.691` edge `-0.0047` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.8808` n `96` status `ready` deltaP `-3.9888` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-2.1442` n `96` status `ready` deltaP `3.811` edge `-0.0771` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.3829` n `96` status `ready` deltaP `6.1229` edge `-0.1373` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3402` n `96` status `ready` deltaP `-17.3611` edge `-0.0043` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7923` n `96` status `ready` deltaP `-0.6945` edge `-0.0648` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.4962` n `96` status `ready` deltaP `-17.3611` edge `-0.1299` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
