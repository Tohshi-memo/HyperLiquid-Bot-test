# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T12:07:25.633961+00:00`
- Price records: `672`
- Market context records: `7026`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.3105` n `218` status `ready` deltaP `1.1688` edge `0.0009` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6024` n `218` status `ready` deltaP `1.2649` edge `0.0278` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6862` n `218` status `ready` deltaP `-1.8294` edge `0.001` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.6869` n `218` status `ready` deltaP `10.9868` edge `0.0071` maxDD `-1.8062`
- `market_context_high->index_1h` score `-0.7175` n `218` status `ready` deltaP `-0.1154` edge `-0.0001` maxDD `-2.2895`
- `market_context_high->unknown_24h` score `-0.8755` n `205` status `ready` deltaP `-6.9495` edge `0.3891` maxDD `-18.7342`
- `market_context_high->crypto_major_1h` score `-1.1179` n `218` status `ready` deltaP `2.7715` edge `0.0236` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.242` n `218` status `ready` deltaP `-2.8388` edge `0.0001` maxDD `-3.1072`
- `market_context_high->commodity_1h` score `-1.4369` n `218` status `ready` deltaP `-4.2589` edge `-0.0192` maxDD `-2.4388`
- `market_context_high->commodity_4h` score `-1.4852` n `218` status `ready` deltaP `-4.2627` edge `-0.0379` maxDD `-3.5939`
- `market_context_high->index_4h` score `-1.8449` n `218` status `ready` deltaP `7.0178` edge `-0.0134` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.962` n `218` status `ready` deltaP `5.6067` edge `0.0094` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.2025` n `218` status `ready` deltaP `-6.0039` edge `0.0789` maxDD `-9.1264`
- `market_context_high->commodity_24h` score `-2.6871` n `205` status `ready` deltaP `-3.1115` edge `-0.0723` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.7384` n `218` status `ready` deltaP `0.909` edge `0.0214` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-3.036` n `218` status `ready` deltaP `2.4872` edge `-0.0178` maxDD `-15.4757`
- `market_context_high->crypto_major_4h` score `-3.1054` n `218` status `ready` deltaP `1.9831` edge `0.0171` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.8931` n `205` status `ready` deltaP `-3.7331` edge `-0.0138` maxDD `-4.1926`
- `market_context_high->equity_4h` score `-7.2904` n `218` status `ready` deltaP `4.1047` edge `-0.075` maxDD `-63.963`
- `market_context_high->metal_24h` score `-13.5415` n `205` status `ready` deltaP `-11.4482` edge `-0.0552` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
