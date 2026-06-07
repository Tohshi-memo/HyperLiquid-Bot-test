# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T10:22:19.019795+00:00`
- Price records: `672`
- Market context records: `3168`
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

- `market_context_high->commodity_24h` score `13.8259` n `101` status `ready` deltaP `47.2171` edge `0.8802` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.8221` n `101` status `ready` deltaP `15.2795` edge `2.4114` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.8008` n `101` status `ready` deltaP `20.2643` edge `0.8971` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.1945` n `101` status `ready` deltaP `29.2216` edge `0.8548` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6494` n `101` status `ready` deltaP `13.8442` edge `1.3454` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.0384` n `134` status `ready` deltaP `19.0503` edge `0.172` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7813` n `101` status `ready` deltaP `12.7011` edge `0.0032` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.2243` n `134` status `ready` deltaP `4.4776` edge `0.0311` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.1578` n `134` status `ready` deltaP `11.0506` edge `0.1354` maxDD `-14.7778`
- `market_context_high->crypto_alt_1h` score `-0.349` n `134` status `ready` deltaP `6.4215` edge `0.1254` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.3888` n `134` status `ready` deltaP `5.6752` edge `0.0186` maxDD `-4.5023`
- `market_context_high->index_4h` score `-0.9578` n `134` status `ready` deltaP `15.1665` edge `0.067` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0108` n `134` status `ready` deltaP `3.3001` edge `0.0747` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0693` n `134` status `ready` deltaP `-9.5451` edge `-0.0052` maxDD `-0.7941`
- `market_context_high->equity_1h` score `-1.3177` n `134` status `ready` deltaP `3.881` edge `0.0129` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3552` n `134` status `ready` deltaP `-11.7401` edge `-0.007` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.0608` n `134` status `ready` deltaP `-3.5794` edge `-0.0085` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.1435` n `134` status `ready` deltaP `17.9651` edge `0.4099` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.8155` n `134` status `ready` deltaP `2.9717` edge `-0.0518` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6009` n `134` status `ready` deltaP `11.2077` edge `0.256` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
