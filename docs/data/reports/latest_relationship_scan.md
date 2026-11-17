# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T15:52:49.181089+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4056`

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

- `market_context_high->unknown_24h` score `1519.2848` n `97` status `ready` deltaP `3.4602` edge `126.584` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.7704` n `49` status `ready` deltaP `67.8589` edge `4.5991` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.133` n `49` status `ready` deltaP `29.4259` edge `2.1147` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.9005` n `97` status `ready` deltaP `44.469` edge `1.9409` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.6602` n `49` status `ready` deltaP `44.6739` edge `1.0254` maxDD `-6.4566`
- `market_context_high->crypto_alt_24h` score `14.1241` n `97` status `ready` deltaP `30.382` edge `1.8206` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.3573` n `49` status `ready` deltaP `59.2084` edge `0.4154` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.1885` n `49` status `ready` deltaP `53.8062` edge `0.407` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0034` n `49` status `ready` deltaP `15.4862` edge `1.3734` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.1603` n `49` status `ready` deltaP `45.0722` edge `0.1598` maxDD `-0.7538`
- `news_risk_high->crypto_alt_4h` score `4.6081` n `49` status `ready` deltaP `26.4` edge `0.3356` maxDD `-8.2073`
- `news_risk_high->equity_1h` score `4.1387` n `49` status `ready` deltaP `22.3818` edge `0.2587` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.0238` n `49` status `ready` deltaP `19.9726` edge `0.3126` maxDD `-7.1683`
- `news_risk_high->commodity_4h` score `3.5304` n `49` status `ready` deltaP `33.1571` edge `0.0985` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2535` n `49` status `ready` deltaP `29.7442` edge `0.1026` maxDD `-0.7146`
- `news_risk_high->metal_1h` score `2.2367` n `49` status `ready` deltaP `25.2658` edge `0.0434` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.424` n `49` status `ready` deltaP `18.5995` edge `0.0248` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9121` n `49` status `ready` deltaP `19.9527` edge `0.2012` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.6057` n `49` status `ready` deltaP `16.2593` edge `0.0672` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.5494` n `49` status `ready` deltaP `17.2522` edge `0.0606` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
