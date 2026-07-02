# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T03:52:26.262196+00:00`
- Price records: `672`
- Market context records: `5417`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->crypto_major_4h` score `4.0581` n `205` status `ready` deltaP `17.0732` edge `0.4536` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.6243` n `194` status `ready` deltaP `18.8932` edge `0.6301` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `3.213` n `205` status `ready` deltaP `12.5305` edge `0.3483` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.5414` n `205` status `ready` deltaP `12.6525` edge `0.2913` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4536` n `205` status `ready` deltaP `8.059` edge `0.0806` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1394` n `205` status `ready` deltaP `6.7738` edge `0.0158` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0374` n `194` status `ready` deltaP `9.2479` edge `0.031` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.0334` n `205` status `ready` deltaP `4.3245` edge `0.0985` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.0347` n `205` status `ready` deltaP `1.9293` edge `0.0804` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4392` n `205` status `ready` deltaP `-0.9537` edge `-0.001` maxDD `-0.5823`
- `market_context_high->equity_24h` score `-0.5648` n `194` status `ready` deltaP `8.0327` edge `0.4831` maxDD `-40.0306`
- `market_context_high->metal_1h` score `-0.5706` n `205` status `ready` deltaP `1.3305` edge `0.0111` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9313` n `205` status `ready` deltaP `6.7073` edge `0.0386` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2913` n `205` status `ready` deltaP `-0.8231` edge `0.0008` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4292` n `205` status `ready` deltaP `-2.7216` edge `-0.0065` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6655` n `194` status `ready` deltaP `12.8275` edge `0.0743` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.5644` n `205` status `ready` deltaP `-6.6768` edge `-0.0318` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.1807` n `205` status `ready` deltaP `-6.2195` edge `-0.0431` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.6324` n `194` status `ready` deltaP `10.1571` edge `0.2493` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.154` n `194` status `ready` deltaP `-5.1171` edge `-0.1453` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
