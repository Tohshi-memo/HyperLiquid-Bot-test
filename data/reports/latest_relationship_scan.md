# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T22:07:27.876053+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6685`

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

- `market_context_high->unknown_24h` score `3424.045` n `90` status `ready` deltaP `-11.0764` edge `285.4539` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `132.9637` n `90` status `ready` deltaP `1.2601` edge `11.0852` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.4796` n `108` status `ready` deltaP `-5.1951` edge `6.5199` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.7828` n `82` status `ready` deltaP `44.7832` edge `1.2718` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7044` n `90` status `ready` deltaP `23.4375` edge `1.0115` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.5258` n `108` status `ready` deltaP `20.8841` edge `0.4599` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9721` n `90` status `ready` deltaP `43.9584` edge `0.1396` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.5202` n `90` status `ready` deltaP `18.8651` edge `0.0434` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8511` n `90` status `ready` deltaP `12.0958` edge `0.0193` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.8361` n `108` status `ready` deltaP `8.8767` edge `0.1059` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.7658` n `90` status `ready` deltaP `16.7954` edge `0.0644` maxDD `-0.5881`
- `market_context_high->fx_4h` score `0.4848` n `90` status `ready` deltaP `11.7005` edge `0.0015` maxDD `-0.1285`
- `market_context_high->equity_4h` score `0.4719` n `90` status `ready` deltaP `1.46` edge `0.1901` maxDD `-4.48`
- `market_context_high->fx_1h` score `0.4313` n `90` status `ready` deltaP `11.0878` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.4202` n `90` status `ready` deltaP `5.5556` edge `0.1044` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.2635` n `90` status `ready` deltaP `7.9275` edge `0.0837` maxDD `-5.2213`
- `market_context_high->metal_24h` score `-0.3785` n `90` status `ready` deltaP `8.125` edge `0.162` maxDD `-10.5088`
- `market_context_high->commodity_1h` score `-0.4502` n `90` status `ready` deltaP `-3.0739` edge `0.0142` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.5067` n `90` status `ready` deltaP `1.7731` edge `0.0018` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-0.559` n `90` status `ready` deltaP `14.2277` edge `0.1075` maxDD `-14.5879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
