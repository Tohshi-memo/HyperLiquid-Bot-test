# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T15:37:27.017283+00:00`
- Price records: `672`
- Market context records: `5365`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `10.4833` n `173` status `ready` deltaP `17.1344` edge `0.7724` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.1098` n `173` status `ready` deltaP `22.146` edge `0.7322` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.4155` n `173` status `ready` deltaP `15.4655` edge `0.7444` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.1818` n `197` status `ready` deltaP `12.7446` edge `0.3261` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.7148` n `197` status `ready` deltaP `9.3421` edge `0.2447` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.283` n `197` status `ready` deltaP `8.6224` edge `0.2133` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.4505` n `173` status `ready` deltaP `17.8508` edge `0.0989` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.1395` n `205` status `ready` deltaP `6.1129` edge `0.0674` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.0784` n `173` status `ready` deltaP `9.2195` edge `0.0346` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.0446` n `205` status `ready` deltaP `4.0251` edge `0.094` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.0695` n `205` status `ready` deltaP `1.6299` edge `0.0795` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.0966` n `205` status `ready` deltaP `4.3786` edge `0.0121` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.4415` n `205` status `ready` deltaP `-0.9537` edge `-0.0013` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5442` n `205` status `ready` deltaP `1.3305` edge `0.0133` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6713` n `197` status `ready` deltaP `2.1241` edge `0.0027` maxDD `-1.567`
- `market_context_high->index_4h` score `-0.8068` n `197` status `ready` deltaP `5.0754` edge `0.0244` maxDD `-2.704`
- `market_context_high->unknown_4h` score `-1.4854` n `197` status `ready` deltaP `7.4486` edge `-0.055` maxDD `-6.1421`
- `market_context_high->commodity_1h` score `-1.5034` n `205` status `ready` deltaP `-3.6198` edge `-0.0067` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.8098` n `197` status `ready` deltaP `-8.5768` edge `-0.0506` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.6201` n `173` status `ready` deltaP `12.5542` edge `0.3219` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
