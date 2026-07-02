# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T13:07:30.113588+00:00`
- Price records: `672`
- Market context records: `5457`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11440`

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

- `market_context_high->crypto_major_24h` score `3.8008` n `194` status `ready` deltaP `17.1087` edge `0.6567` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.4236` n `197` status `ready` deltaP `14.6728` edge `0.3334` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0691` n `197` status `ready` deltaP `11.7734` edge `0.2578` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8635` n `197` status `ready` deltaP `9.7461` edge `0.2544` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.2988` n `199` status `ready` deltaP `7.7137` edge `0.07` maxDD `-5.0555`
- `market_context_high->equity_24h` score `0.2548` n `194` status `ready` deltaP `8.3745` edge `0.4733` maxDD `-31.6316`
- `market_context_high->index_1h` score `0.0959` n `199` status `ready` deltaP `6.3348` edge `0.0151` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0528` n `194` status `ready` deltaP `9.8171` edge `0.0309` maxDD `-1.0224`
- `market_context_high->metal_1h` score `-0.3013` n `199` status `ready` deltaP `3.8117` edge `0.017` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4904` n `199` status `ready` deltaP `0.5078` edge `0.0519` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.5417` n `199` status `ready` deltaP `0.5612` edge `0.0` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.6222` n `199` status `ready` deltaP `1.6948` edge `0.0614` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.928` n `197` status `ready` deltaP `6.7034` edge `0.0389` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0561` n `197` status `ready` deltaP `1.5158` edge `0.0044` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3409` n `199` status `ready` deltaP `-1.8227` edge `-0.0048` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8181` n `194` status `ready` deltaP `12.8275` edge `0.0659` maxDD `-16.4274`
- `market_context_high->metal_4h` score `-2.6151` n `197` status `ready` deltaP `-7.9671` edge `-0.0297` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.215` n `197` status `ready` deltaP `-5.7764` edge `-0.0413` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-6.9995` n `194` status `ready` deltaP `8.3727` edge `0.2306` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0465` n `194` status `ready` deltaP `-3.0659` edge `-0.1452` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
