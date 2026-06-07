# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T13:52:22.575943+00:00`
- Price records: `672`
- Market context records: `3183`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.7976` n `104` status `ready` deltaP `47.329` edge `0.8771` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.3242` n `104` status `ready` deltaP `19.9519` edge `0.9428` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.5607` n `104` status `ready` deltaP `14.6768` edge `2.3819` maxDD `-71.142`
- `market_context_high->index_24h` score `6.2415` n `104` status `ready` deltaP `30.0213` edge `0.8555` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.519` n `104` status `ready` deltaP `12.9274` edge `1.3348` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.133` n `135` status `ready` deltaP `20.0226` edge `0.1734` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.6775` n `104` status `ready` deltaP `11.5385` edge `0.0023` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.5695` n `135` status `ready` deltaP `11.1574` edge `0.1953` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3456` n `140` status `ready` deltaP `5.9795` edge `0.0312` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3244` n `140` status `ready` deltaP `6.6125` edge `0.0206` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4876` n `140` status `ready` deltaP `5.7827` edge `0.1119` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.7997` n `135` status `ready` deltaP `17.081` edge `0.0745` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0516` n `140` status `ready` deltaP `3.2806` edge `0.0696` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2538` n `140` status `ready` deltaP `4.3199` edge `0.0153` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3369` n `135` status `ready` deltaP `-11.4171` edge `-0.0068` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6359` n `140` status `ready` deltaP `-9.367` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0834` n `140` status `ready` deltaP `-3.9521` edge `-0.0079` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.3099` n `135` status `ready` deltaP `17.0766` edge `0.3945` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1063` n `140` status `ready` deltaP `2.6519` edge `-0.0739` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6934` n `135` status `ready` deltaP `10.1027` edge `0.2515` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
