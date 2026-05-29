# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T11:07:21.183132+00:00`
- Price records: `672`
- Market context records: `2238`
- Flow alert records: `8337`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.5788` n `36` status `ready` deltaP `55.7291` edge `1.8189` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.3455` n `36` status `ready` deltaP `45.8333` edge `1.0172` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.0054` n `36` status `ready` deltaP `36.8055` edge `0.9532` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.8234` n `131` status `ready` deltaP `35.9477` edge `0.9226` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6118` n `131` status `ready` deltaP `41.6019` edge `0.7433` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.1178` n `36` status `ready` deltaP `36.6319` edge `0.5382` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `8.1619` n `36` status `ready` deltaP `21.3542` edge `0.9621` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `6.1846` n `131` status `ready` deltaP `24.5043` edge `0.3974` maxDD `-1.6306`
- `market_context_high->unknown_24h` score `5.9522` n `124` status `ready` deltaP `26.8649` edge `0.5583` maxDD `-16.3105`
- `market_context_high->equity_4h` score `4.4587` n `131` status `ready` deltaP `24.3705` edge `0.2493` maxDD `-1.2171`
- `market_context_high->crypto_major_24h` score `3.9731` n `124` status `ready` deltaP `16.3363` edge `0.9245` maxDD `-35.9234`
- `news_risk_high->commodity_4h` score `3.9427` n `43` status `ready` deltaP `33.2246` edge `0.3511` maxDD `-3.0367`
- `market_context_high->index_4h` score `3.9416` n `131` status `ready` deltaP `29.7081` edge `0.168` maxDD `-0.34`
- `news_risk_high->fx_24h` score `3.2562` n `36` status `ready` deltaP `33.3333` edge `0.0676` maxDD `-0.1442`
- `market_context_high->crypto_major_1h` score `2.8298` n `143` status `ready` deltaP `15.1847` edge `0.1823` maxDD `-1.817`
- `news_risk_high->commodity_24h` score `2.7255` n `36` status `ready` deltaP `1.5625` edge `0.2984` maxDD `-3.202`
- `market_context_high->index_24h` score `2.7071` n `124` status `ready` deltaP `11.2847` edge `0.2166` maxDD `-2.2991`
- `market_context_high->crypto_alt_1h` score `2.7067` n `143` status `ready` deltaP `15.1847` edge `0.2107` maxDD `-4.9097`
- `news_risk_high->index_24h` score `2.349` n `36` status `ready` deltaP `11.2847` edge `0.1624` maxDD `-1.3507`
- `news_risk_high->fx_4h` score `2.1512` n `43` status `ready` deltaP `27.2794` edge `0.0158` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
