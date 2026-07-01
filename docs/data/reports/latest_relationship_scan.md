# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T12:07:33.359352+00:00`
- Price records: `672`
- Market context records: `5350`
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

- `market_context_high->unknown_24h` score `16.0396` n `159` status `ready` deltaP `20.509` edge `1.2089` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.6424` n `159` status `ready` deltaP `22.0289` edge `0.7753` maxDD `-29.4899`
- `market_context_high->equity_24h` score `4.587` n `159` status `ready` deltaP `17.7804` edge `0.8266` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.8111` n `194` status `ready` deltaP `13.3361` edge `0.3746` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.5562` n `194` status `ready` deltaP `10.6644` edge `0.306` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7688` n `194` status `ready` deltaP `9.9399` edge `0.245` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.8271` n `159` status `ready` deltaP `24.9509` edge `0.1032` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.4263` n `195` status `ready` deltaP `7.538` edge `0.0818` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.136` n `159` status `ready` deltaP `9.3849` edge `0.0383` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.0549` n `195` status `ready` deltaP `4.534` edge `0.0989` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.0261` n `195` status `ready` deltaP `6.0663` edge `0.0121` maxDD `-1.0296`
- `market_context_high->crypto_alt_1h` score `0.0229` n `195` status `ready` deltaP `1.8394` edge `0.0858` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3943` n `195` status `ready` deltaP `-0.1512` edge `-0.0006` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4039` n `194` status `ready` deltaP `5.7644` edge `0.0257` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.4705` n `195` status `ready` deltaP `0.8552` edge `0.0015` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7095` n `194` status `ready` deltaP `1.3735` edge `0.0028` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2773` n `194` status `ready` deltaP `7.7555` edge `-0.0399` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4742` n `195` status `ready` deltaP `-3.655` edge `-0.0067` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.6179` n `194` status `ready` deltaP `-7.3768` edge `-0.034` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-3.8298` n `194` status `ready` deltaP `-7.1662` edge `-0.043` maxDD `-11.937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
