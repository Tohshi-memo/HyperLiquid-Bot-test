# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T13:07:16.714929+00:00`
- Price records: `672`
- Market context records: `1632`
- Flow alert records: `6609`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `10.2074` n `183` status `ready` deltaP `26.9872` edge `0.9133` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.2759` n `183` status `ready` deltaP `19.1086` edge `0.2834` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4181` n `186` status `ready` deltaP `11.7494` edge `0.1493` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `1.3999` n `186` status `ready` deltaP `16.7428` edge `0.3353` maxDD `-16.3952`
- `market_context_high->equity_24h` score `0.6756` n `183` status `ready` deltaP `17.6161` edge `0.4287` maxDD `-33.1875`
- `market_context_high->crypto_major_4h` score `0.6193` n `186` status `ready` deltaP `12.5227` edge `0.2668` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.221` n `197` status `ready` deltaP `1.5805` edge `0.0635` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.3324` n `183` status `ready` deltaP `7.3358` edge `0.0283` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.5285` n `197` status `ready` deltaP `1.126` edge `0.0293` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5323` n `197` status `ready` deltaP `-0.2724` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.6044` n `183` status `ready` deltaP `23.1478` edge `0.6539` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.638` n `197` status `ready` deltaP `0.7057` edge `0.0053` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.8471` n `186` status `ready` deltaP `0.2258` edge `0.0368` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.8827` n `197` status `ready` deltaP `-1.4932` edge `0.0299` maxDD `-5.9819`
- `market_context_high->commodity_1h` score `-0.9087` n `197` status `ready` deltaP `1.5213` edge `0.0021` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.3915` n `197` status `ready` deltaP `2.1784` edge `0.0031` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.4753` n `186` status `ready` deltaP `7.8067` edge `0.0942` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-1.854` n `183` status `ready` deltaP `23.3864` edge `0.8705` maxDD `-88.8062`
- `market_context_high->fx_4h` score `-1.9991` n `186` status `ready` deltaP `-9.0145` edge `-0.0136` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.1274` n `186` status `ready` deltaP `7.7651` edge `-0.1686` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
