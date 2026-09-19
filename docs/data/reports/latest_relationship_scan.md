# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T20:07:25.716399+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8478`

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

- `news_risk_high->crypto_major_24h` score `51.1714` n `72` status `ready` deltaP `27.4305` edge `4.1706` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.6919` n `72` status `ready` deltaP `33.6806` edge `3.6377` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `40.3157` n `118` status `ready` deltaP `-3.7851` edge `3.4082` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.8854` n `72` status `ready` deltaP `37.1528` edge `0.497` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8254` n `118` status `ready` deltaP `40.3101` edge `0.4359` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.5328` n `98` status `ready` deltaP `20.5512` edge `0.445` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2505` n `98` status `ready` deltaP `21.3134` edge `0.3379` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.216` n `98` status `ready` deltaP `18.4743` edge `0.1914` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.6115` n `118` status `ready` deltaP `26.7957` edge `0.0808` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.348` n `98` status `ready` deltaP `19.5222` edge `0.1178` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7261` n `72` status `ready` deltaP `22.5694` edge `0.0778` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4312` n `118` status `ready` deltaP `17.6951` edge `0.0265` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.8356` n `98` status `ready` deltaP `19.2819` edge `0.0465` maxDD `-2.0994`
- `market_context_high->fx_4h` score `0.7493` n `118` status `ready` deltaP `16.5822` edge `-0.0013` maxDD `-0.0779`
- `news_risk_high->metal_1h` score `0.7315` n `98` status `ready` deltaP `15.7552` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.5025` n `98` status `ready` deltaP `7.5645` edge `0.032` maxDD `-0.9112`
- `news_risk_high->fx_24h` score `0.3927` n `72` status `ready` deltaP `1.9098` edge `0.0382` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.2325` n `118` status `ready` deltaP `8.0067` edge `-0.0298` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.0093` n `118` status `ready` deltaP `3.8339` edge `0.001` maxDD `-0.063`
- `news_risk_high->equity_4h` score `0.0049` n `98` status `ready` deltaP `9.361` edge `0.0824` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
