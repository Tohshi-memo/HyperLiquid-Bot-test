# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T09:37:37.367670+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `4.4642` n `108` status `ready` deltaP `24.3056` edge `0.8038` maxDD `-26.8138`
- `news_risk_high->crypto_alt_4h` score `1.482` n `130` status `ready` deltaP `9.5779` edge `0.2664` maxDD `-7.5533`
- `news_risk_high->crypto_alt_1h` score `-0.2849` n `142` status `ready` deltaP `2.7115` edge `0.0527` maxDD `-4.584`
- `news_risk_high->fx_1h` score `-0.5225` n `142` status `ready` deltaP `0.8097` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.6932` n `142` status `ready` deltaP `-0.3437` edge `-0.0066` maxDD `-1.3981`
- `news_risk_high->metal_24h` score `-0.8924` n `108` status `ready` deltaP `12.6736` edge `0.1267` maxDD `-14.0483`
- `news_risk_high->metal_1h` score `-1.2136` n `142` status `ready` deltaP `-3.81` edge `-0.008` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4046` n `130` status `ready` deltaP `-5.9874` edge `-0.015` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.2311` n `130` status `ready` deltaP `-4.1159` edge `-0.0285` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.4766` n `142` status `ready` deltaP `-9.4712` edge `-0.0067` maxDD `-3.2568`
- `news_risk_high->fx_24h` score `-2.4887` n `108` status `ready` deltaP `-18.75` edge `-0.0232` maxDD `-2.336`
- `news_risk_high->metal_4h` score `-2.7945` n `130` status `ready` deltaP `-1.5877` edge `-0.0272` maxDD `-9.3056`
- `news_risk_high->equity_1h` score `-2.9815` n `142` status `ready` deltaP `-8.0459` edge `-0.061` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1872` n `142` status `ready` deltaP `-7.7465` edge `-0.0414` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-3.4066` n `108` status `ready` deltaP `-15.6829` edge `-0.048` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.7297` n `130` status `ready` deltaP `-12.3358` edge `-0.0136` maxDD `-7.8641`
- `news_risk_high->crypto_major_4h` score `-4.6138` n `130` status `ready` deltaP `-13.3748` edge `-0.1004` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-6.5265` n `108` status `ready` deltaP `2.9514` edge `0.1531` maxDD `-67.0937`
- `news_risk_high->crypto_major_24h` score `-6.9927` n `108` status `ready` deltaP `-19.3287` edge `-0.1641` maxDD `-36.9504`
- `news_risk_high->equity_4h` score `-8.5491` n `130` status `ready` deltaP `-3.2012` edge `-0.2386` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
