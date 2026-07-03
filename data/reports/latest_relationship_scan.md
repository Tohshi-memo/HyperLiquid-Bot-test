# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T00:07:31.278358+00:00`
- Price records: `672`
- Market context records: `5506`
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

- `market_context_high->crypto_major_24h` score `2.97` n `190` status `ready` deltaP `16.2189` edge `0.5934` maxDD `-29.6555`
- `market_context_high->equity_24h` score `2.4717` n `190` status `ready` deltaP `10.7511` edge `0.6422` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.4655` n `193` status `ready` deltaP `14.3411` edge `0.3391` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.3092` n `193` status `ready` deltaP `11.5348` edge `0.2794` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.9905` n `193` status `ready` deltaP `10.1036` edge `0.2626` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5327` n `193` status `ready` deltaP `8.8828` edge `0.0817` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3826` n `190` status `ready` deltaP `12.9312` edge `0.0384` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1356` n `193` status `ready` deltaP `6.5457` edge `0.017` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2748` n `193` status `ready` deltaP `1.2837` edge `0.0647` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3463` n `193` status `ready` deltaP `0.6275` edge `0.0003` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4103` n `193` status `ready` deltaP `2.873` edge `0.0712` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5523` n `193` status `ready` deltaP `1.3644` edge `0.0124` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7665` n `193` status `ready` deltaP `4.1285` edge `0.0067` maxDD `-1.5143`
- `market_context_high->index_4h` score `-0.927` n `193` status `ready` deltaP `6.4467` edge `0.0407` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.4716` n `193` status `ready` deltaP `-2.8265` edge `-0.009` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8107` n `190` status `ready` deltaP `14.2708` edge `0.0714` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8961` n `193` status `ready` deltaP `-10.8658` edge `-0.0464` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5115` n `193` status `ready` deltaP `-8.486` edge `-0.0521` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.2098` n `190` status `ready` deltaP `7.2442` edge `0.2206` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2853` n `190` status `ready` deltaP `-4.2379` edge `-0.168` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
