# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T18:37:16.049973+00:00`
- Price records: `672`
- Market context records: `1656`
- Flow alert records: `6677`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `9.7984` n `169` status `ready` deltaP `28.7607` edge `0.8674` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.309` n `190` status `ready` deltaP `22.1557` edge `0.4778` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7887` n `169` status `ready` deltaP `20.5841` edge `0.3163` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.5011` n `190` status `ready` deltaP `18.1671` edge `0.3582` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.8504` n `190` status `ready` deltaP `12.3832` edge `0.1811` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7386` n `169` status `ready` deltaP `19.7743` edge `0.5029` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.8137` n `169` status `ready` deltaP `25.5738` edge `0.7559` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.6425` n `169` status `ready` deltaP `26.228` edge `1.0596` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.5278` n `201` status `ready` deltaP `6.3068` edge `0.1043` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.255` n `201` status `ready` deltaP `1.719` edge `0.0367` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3885` n `190` status `ready` deltaP `1.1087` edge `0.0517` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.4272` n `201` status `ready` deltaP `2.4325` edge `0.0564` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4762` n `169` status `ready` deltaP `6.214` edge `0.0238` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.4787` n `201` status `ready` deltaP `-0.8699` edge `0.0076` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5282` n `201` status `ready` deltaP `-0.2093` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.7879` n `201` status `ready` deltaP `4.0747` edge `0.0054` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.9786` n `201` status `ready` deltaP `0.8915` edge `-0.0097` maxDD `-7.4032`
- `market_context_high->metal_4h` score `-1.3318` n `190` status `ready` deltaP `8.5357` edge `0.1013` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.9703` n `190` status `ready` deltaP `-8.7006` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.7734` n `190` status `ready` deltaP `11.0206` edge `-0.1608` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
