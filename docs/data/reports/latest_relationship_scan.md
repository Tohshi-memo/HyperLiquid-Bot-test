# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T02:07:29.161299+00:00`
- Price records: `672`
- Market context records: `5514`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->equity_24h` score `2.9285` n `190` status `ready` deltaP `12.14` edge `0.671` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.622` n `190` status `ready` deltaP `16.2189` edge `0.5644` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.3569` n `193` status `ready` deltaP `13.8838` edge `0.3331` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.9562` n `193` status `ready` deltaP `10.4677` edge `0.2571` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.7949` n `193` status `ready` deltaP `9.189` edge `0.2524` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.391` n `190` status `ready` deltaP `12.9312` edge `0.0391` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2773` n `193` status `ready` deltaP `7.8349` edge `0.0674` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0433` n `193` status `ready` deltaP `5.7972` edge `0.0143` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3471` n `193` status `ready` deltaP `0.6275` edge `0.0002` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.5434` n `193` status `ready` deltaP `0.3855` edge `0.0483` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6646` n `193` status `ready` deltaP `1.9748` edge `0.056` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7165` n `193` status `ready` deltaP `0.3165` edge `0.0057` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8638` n `193` status `ready` deltaP `3.0614` edge `0.0057` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.0723` n `193` status `ready` deltaP `5.3796` edge `0.0357` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5578` n `193` status `ready` deltaP `-3.7247` edge `-0.0102` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8318` n `190` status `ready` deltaP `14.2708` edge `0.0687` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0305` n `193` status `ready` deltaP `-12.0853` edge `-0.0555` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5709` n `193` status `ready` deltaP `-8.9433` edge `-0.054` maxDD `-14.0497`
- `market_context_high->metal_24h` score `-7.322` n `190` status `ready` deltaP `-4.2379` edge `-0.1727` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.3478` n `190` status `ready` deltaP `7.2442` edge `0.2091` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
