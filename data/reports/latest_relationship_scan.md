# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T22:07:16.293454+00:00`
- Price records: `672`
- Market context records: `1672`
- Flow alert records: `6722`
- Minimum samples: `30`
- Pattern count: `96`

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

- `market_context_high->metal_24h` score `9.3432` n `161` status `ready` deltaP `28.1104` edge `0.8338` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.1106` n `195` status `ready` deltaP `22.8901` edge `0.5397` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8418` n `161` status `ready` deltaP `19.6726` edge `0.3268` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.1914` n `195` status `ready` deltaP `18.9955` edge `0.4102` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.3552` n `195` status `ready` deltaP `13.2028` edge `0.2177` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8489` n `161` status `ready` deltaP `18.9183` edge `0.5178` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.817` n `204` status `ready` deltaP `7.0418` edge `0.1235` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.5685` n `161` status `ready` deltaP `25.8129` edge `1.0562` maxDD `-88.8062`
- `market_context_high->crypto_major_24h` score `0.3282` n `161` status `ready` deltaP `24.8942` edge `0.7347` maxDD `-62.3533`
- `market_context_high->index_4h` score `-0.0739` n `195` status `ready` deltaP `4.5958` edge `0.0721` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1045` n `204` status `ready` deltaP `3.6809` edge `0.0476` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.2089` n `204` status `ready` deltaP `4.6172` edge `0.0792` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4573` n `161` status `ready` deltaP `6.7195` edge `0.022` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6192` n `204` status `ready` deltaP `-0.3493` edge `0.0139` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8618` n `204` status `ready` deltaP `-0.8835` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.919` n `195` status `ready` deltaP `11.2054` edge `0.1179` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-1.0393` n `204` status `ready` deltaP `5.3657` edge `0.0112` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.2579` n `195` status `ready` deltaP `-8.3224` edge `-0.0129` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-1.6219` n `161` status `ready` deltaP `11.2521` edge `0.3302` maxDD `-35.8966`
- `market_context_high->commodity_1h` score `-2.2158` n `204` status `ready` deltaP `-0.8982` edge `-0.0334` maxDD `-14.9083`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
