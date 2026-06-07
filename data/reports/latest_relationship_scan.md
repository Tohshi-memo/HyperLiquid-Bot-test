# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T08:22:21.950244+00:00`
- Price records: `672`
- Market context records: `3160`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8854`

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

- `market_context_high->commodity_24h` score `13.8883` n `105` status `ready` deltaP `47.247` edge `0.8852` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.115` n `105` status `ready` deltaP `15.2728` edge `2.449` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.7964` n `105` status `ready` deltaP `21.245` edge `0.8902` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.3703` n `105` status `ready` deltaP `30.2777` edge `0.8703` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.8654` n `105` status `ready` deltaP `13.4226` edge `1.3759` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.9286` n `138` status `ready` deltaP `18.6528` edge `0.1655` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.4167` n `105` status `ready` deltaP `10.8085` edge `0.0021` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.1995` n `138` status `ready` deltaP `4.3478` edge `0.0299` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3538` n `138` status `ready` deltaP `6.4198` edge `0.1248` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4535` n `138` status `ready` deltaP `4.6711` edge `0.017` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.878` n `138` status `ready` deltaP `3.4974` edge `0.0127` maxDD `-8.8863`
- `market_context_high->unknown_4h` score `-0.9875` n `138` status `ready` deltaP `8.9298` edge `0.0804` maxDD `-14.7778`
- `market_context_high->index_4h` score `-1.0433` n `138` status `ready` deltaP `13.8079` edge `0.0651` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0438` n `138` status `ready` deltaP `2.5145` edge `0.0757` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1275` n `138` status `ready` deltaP `-10.6483` edge `-0.0053` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.4052` n `138` status `ready` deltaP `-12.6259` edge `-0.0075` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.1052` n `138` status `ready` deltaP `-4.3001` edge `-0.0074` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.9051` n `138` status `ready` deltaP `14.073` edge `0.0643` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.9459` n `138` status `ready` deltaP `19.6337` edge `0.4281` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.3664` n `138` status `ready` deltaP `1.3061` edge `-0.0866` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
