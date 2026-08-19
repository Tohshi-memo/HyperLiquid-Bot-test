# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T20:52:24.494521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10827`

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

- `market_context_high->equity_4h` score `2.2927` n `96` status `ready` deltaP `11.6107` edge `0.2025` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8068` n `96` status `ready` deltaP `14.8516` edge `0.0817` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9869` n `96` status `ready` deltaP `16.5107` edge `0.0109` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5088` n `96` status `ready` deltaP `13.2113` edge `0.0119` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2954` n `96` status `ready` deltaP `9.7815` edge `0.0249` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.2465` n `96` status `ready` deltaP `6.4236` edge `0.1721` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.1011` n `96` status `ready` deltaP `17.7083` edge `-0.059` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.0375` n `96` status `ready` deltaP `7.4949` edge `0.0051` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.0949` n `96` status `ready` deltaP `6.512` edge `-0.0286` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1364` n `96` status `ready` deltaP `3.4244` edge `0.0045` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3284` n `96` status `ready` deltaP `-1.3224` edge `0.0026` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6669` n `96` status `ready` deltaP `-0.94` edge `0.0058` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7658` n `96` status `ready` deltaP `-0.3181` edge `-0.0159` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8142` n `96` status `ready` deltaP `1.4845` edge `-0.0298` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8876` n `96` status `ready` deltaP `-7.7408` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->crypto_major_24h` score `-1.1941` n `96` status `ready` deltaP `2.9514` edge `0.0016` maxDD `-4.9964`
- `market_context_high->crypto_major_4h` score `-1.3199` n `96` status `ready` deltaP `5.9705` edge `-0.0477` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.5814` n `96` status `ready` deltaP `3.811` edge `-0.0302` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-3.0571` n `96` status `ready` deltaP `-9.2014` edge `0.0002` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.4354` n `96` status `ready` deltaP `-18.0555` edge `-0.0076` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
