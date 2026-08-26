# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T13:42:27.736922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `45.0462` n `53` status `ready` deltaP `11.6319` edge `3.6763` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.1918` n `53` status `ready` deltaP `24.8274` edge `0.8604` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `10.689` n `53` status `ready` deltaP `31.9903` edge `0.7216` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.8374` n `53` status `ready` deltaP `29.2453` edge `0.4679` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0241` n `53` status `ready` deltaP `40.114` edge `0.0831` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.9558` n `53` status `ready` deltaP `35.573` edge `0.0226` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.8249` n `136` status `ready` deltaP `23.1349` edge `0.122` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7819` n `53` status `ready` deltaP `15.5632` edge `0.1636` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `1.8152` n `53` status `ready` deltaP `29.1896` edge `-0.0391` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.6959` n `53` status `ready` deltaP `19.7365` edge `0.0868` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1165` n `53` status `ready` deltaP `15.6197` edge `0.0059` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0943` n `137` status `ready` deltaP `11.8034` edge `0.0574` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.432` n `53` status `ready` deltaP `10.6768` edge `-0.0039` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4107` n `53` status `ready` deltaP `12.7754` edge `0.0039` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1767` n `53` status `ready` deltaP `7.1186` edge `0.007` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0721` n `53` status `ready` deltaP `3.8499` edge `0.0004` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.121` n `53` status `ready` deltaP `6.9489` edge `-0.0033` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.2593` n `53` status `ready` deltaP `1.1835` edge `-0.0069` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4348` n `137` status `ready` deltaP `2.7427` edge `-0.0008` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.9502` n `136` status `ready` deltaP `4.4656` edge `-0.0295` maxDD `-2.6898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
