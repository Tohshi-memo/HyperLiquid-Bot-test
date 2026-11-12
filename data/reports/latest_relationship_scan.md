# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T15:52:28.772818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11990`

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

- `market_context_high->unknown_24h` score `296.8783` n `84` status `ready` deltaP `6.4425` edge `24.711` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `93.1166` n `92` status `ready` deltaP `7.9202` edge `7.7517` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.1535` n `53` status `ready` deltaP `21.0486` edge `2.1931` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.1361` n `84` status `ready` deltaP `18.7799` edge `1.5401` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `10.9436` n `53` status `ready` deltaP `36.8969` edge `1.3536` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.8032` n `53` status `ready` deltaP `33.9536` edge `0.7036` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.5264` n `53` status `ready` deltaP `43.4256` edge `0.3377` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.9955` n `84` status `ready` deltaP `38.2106` edge `1.0517` maxDD `-25.4331`
- `market_context_high->metal_24h` score `6.0347` n `84` status `ready` deltaP `38.8491` edge `0.2852` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6796` n `53` status `ready` deltaP `44.4145` edge `0.1315` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8281` n `84` status `ready` deltaP `20.926` edge `0.189` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.4197` n `53` status `ready` deltaP `19.129` edge `0.1878` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.2747` n `53` status `ready` deltaP `17.4161` edge `0.2198` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.1972` n `53` status `ready` deltaP `21.6579` edge `0.2708` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0531` n `53` status `ready` deltaP `26.7114` edge `0.1017` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2805` n `53` status `ready` deltaP `26.6382` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.899` n `53` status `ready` deltaP `19.5266` edge `0.0717` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5645` n `53` status `ready` deltaP `25.4314` edge `0.1949` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2717` n `53` status `ready` deltaP `17.176` edge `0.0216` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6997` n `53` status `ready` deltaP `18.7916` edge `0.0696` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
