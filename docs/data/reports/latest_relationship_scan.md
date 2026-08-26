# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T18:08:22.743048+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `47.7089` n `50` status `ready` deltaP `11.5717` edge `3.8986` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.3248` n `50` status `ready` deltaP `26.6252` edge `0.8595` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `10.9696` n `50` status `ready` deltaP `34.6874` edge `0.727` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8949` n `50` status `ready` deltaP `34.2591` edge `0.5226` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1857` n `50` status `ready` deltaP `41.7133` edge `0.0859` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.503` n `50` status `ready` deltaP `41.3171` edge `0.0255` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.185` n `137` status `ready` deltaP `25.3259` edge `0.1374` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.5508` n `50` status `ready` deltaP `14.8802` edge `0.1489` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.0413` n `50` status `ready` deltaP `31.506` edge `-0.0357` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.4228` n `50` status `ready` deltaP `19.2473` edge `0.0673` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.324` n `50` status `ready` deltaP `18.1078` edge `0.0066` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3107` n `50` status `ready` deltaP `17.1138` edge `0.0232` maxDD `-0.2455`
- `market_context_high->unknown_1h` score `1.1819` n `137` status `ready` deltaP `12.2525` edge `0.0617` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.5129` n `50` status `ready` deltaP `14.1497` edge `0.0027` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1038` n `50` status `ready` deltaP `6.7605` edge `0.0022` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0848` n `50` status `ready` deltaP `6.2549` edge `0.0051` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0633` n `50` status `ready` deltaP `4.9521` edge `-0.0023` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1223` n `50` status `ready` deltaP `7.5781` edge `-0.0076` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4185` n `137` status `ready` deltaP `3.0421` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->unknown_24h` score `-0.7066` n `133` status `ready` deltaP `5.5567` edge `-0.0232` maxDD `-3.1513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
