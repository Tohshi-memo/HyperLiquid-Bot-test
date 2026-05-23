# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T21:52:17.762665+00:00`
- Price records: `672`
- Market context records: `1671`
- Flow alert records: `6719`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `9.4454` n `162` status `ready` deltaP `28.2177` edge `0.8416` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.0338` n `195` status `ready` deltaP `22.8901` edge `0.5333` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8369` n `162` status `ready` deltaP `19.7915` edge `0.3256` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.135` n `195` status `ready` deltaP `18.9955` edge `0.4055` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.3024` n `195` status `ready` deltaP `13.2028` edge `0.2133` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8405` n `162` status `ready` deltaP `19.0525` edge `0.5162` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7692` n `205` status `ready` deltaP `6.7453` edge `0.1215` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.5782` n `162` status `ready` deltaP `25.8896` edge `1.0565` maxDD `-88.8062`
- `market_context_high->crypto_major_24h` score `0.3675` n `162` status `ready` deltaP `25.0054` edge `0.739` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1191` n `205` status `ready` deltaP `3.5293` edge `0.0474` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.1328` n `195` status `ready` deltaP `4.2354` edge `0.0696` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.2515` n `205` status `ready` deltaP `4.3399` edge `0.0775` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4404` n `162` status `ready` deltaP `6.8115` edge `0.0228` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6312` n `205` status `ready` deltaP `-0.4841` edge `0.0138` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.843` n `205` status `ready` deltaP `-0.6492` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.973` n `195` status `ready` deltaP `10.845` edge `0.1158` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-1.0711` n `205` status `ready` deltaP `5.0884` edge `0.0104` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.2587` n `195` status `ready` deltaP `-8.3224` edge `-0.013` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-2.1086` n `162` status `ready` deltaP `10.8035` edge `0.2968` maxDD `-35.8966`
- `market_context_high->commodity_1h` score `-2.2292` n `205` status `ready` deltaP `-1.1421` edge `-0.0335` maxDD `-14.9083`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
