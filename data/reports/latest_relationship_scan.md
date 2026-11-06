# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T14:37:28.463228+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3932`

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

- `news_risk_high->equity_24h` score `0.8257` n `112` status `ready` deltaP `26.8197` edge `1.0857` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.2548` n `112` status `ready` deltaP `11.4329` edge `0.0166` maxDD `-1.4793`
- `news_risk_high->equity_4h` score `0.2074` n `112` status `ready` deltaP `11.8902` edge `0.1686` maxDD `-14.3686`
- `news_risk_high->index_1h` score `-0.2276` n `112` status `ready` deltaP `6.266` edge `0.0025` maxDD `-0.8765`
- `news_risk_high->index_24h` score `-0.4036` n `112` status `ready` deltaP `-0.519` edge `0.1352` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.4212` n `112` status `ready` deltaP `0.5667` edge `0.0011` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.445` n `112` status `ready` deltaP `2.9887` edge `0.0458` maxDD `-5.8225`
- `news_risk_high->crypto_alt_4h` score `-0.7275` n `112` status `ready` deltaP `2.3519` edge `0.1547` maxDD `-14.0916`
- `news_risk_high->crypto_major_1h` score `-0.7359` n `112` status `ready` deltaP `-1.7697` edge `0.018` maxDD `-4.7103`
- `news_risk_high->metal_1h` score `-0.7646` n `112` status `ready` deltaP `-1.0426` edge `-0.0064` maxDD `-1.0293`
- `news_risk_high->crypto_major_4h` score `-0.9887` n `112` status `ready` deltaP `-1.568` edge `0.0648` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.0256` n `112` status `ready` deltaP `-0.5009` edge `-0.0012` maxDD `-0.4745`
- `news_risk_high->equity_1h` score `-1.1465` n `112` status `ready` deltaP `-0.1497` edge `0.0267` maxDD `-8.815`
- `news_risk_high->fx_24h` score `-1.1697` n `112` status `ready` deltaP `-12.9325` edge `-0.0003` maxDD `-0.4086`
- `news_risk_high->metal_4h` score `-1.9524` n `112` status `ready` deltaP `-4.1376` edge `-0.0396` maxDD `-1.9743`
- `news_risk_high->commodity_1h` score `-2.9266` n `112` status `ready` deltaP `-14.7348` edge `-0.009` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.1624` n `112` status `ready` deltaP `-1.174` edge `-0.208` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.2264` n `112` status `ready` deltaP `-25.9799` edge `-0.0269` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.0139` n `112` status `ready` deltaP `-15.8088` edge `0.1847` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.3876` n `112` status `ready` deltaP `-24.1998` edge `-0.0062` maxDD `-38.5147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
