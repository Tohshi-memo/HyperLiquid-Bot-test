# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T14:52:29.676531+00:00`
- Price records: `672`
- Market context records: `5465`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11460`

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

- `market_context_high->crypto_major_24h` score `3.6338` n `194` status `ready` deltaP `16.7615` edge `0.6451` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.4041` n `197` status `ready` deltaP `14.3679` edge `0.3338` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0287` n `197` status `ready` deltaP `11.8237` edge `0.2541` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.9119` n `197` status `ready` deltaP `9.7963` edge `0.2581` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.3438` n `197` status `ready` deltaP `8.1864` edge `0.0706` maxDD `-5.0555`
- `market_context_high->equity_24h` score `0.2344` n `194` status `ready` deltaP `8.8846` edge `0.4682` maxDD `-31.6316`
- `market_context_high->index_1h` score `0.1372` n `197` status `ready` deltaP `6.7616` edge `0.0157` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.063` n `194` status `ready` deltaP `10.0015` edge `0.0313` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.355` n `197` status `ready` deltaP `0.5205` edge `-0.0001` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.3685` n `197` status `ready` deltaP `3.3322` edge `0.0146` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4908` n `197` status `ready` deltaP `0.7287` edge `0.0504` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6849` n `197` status `ready` deltaP `1.9005` edge `0.0548` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.9166` n `197` status `ready` deltaP `6.9062` edge `0.0385` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0549` n `197` status `ready` deltaP `1.5158` edge `0.0045` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.405` n `197` status `ready` deltaP `-2.3686` edge `-0.0065` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9427` n `194` status `ready` deltaP `12.8275` edge `0.0641` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.0474` n `197` status `ready` deltaP `-8.1195` edge `-0.0307` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.1725` n `197` status `ready` deltaP `-5.3191` edge `-0.0408` maxDD `-14.3822`
- `market_context_high->metal_24h` score `-7.0348` n `194` status `ready` deltaP `-3.0659` edge `-0.1437` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.0837` n `194` status `ready` deltaP `8.0255` edge `0.2259` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
