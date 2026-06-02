# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T07:37:23.127983+00:00`
- Price records: `672`
- Market context records: `2642`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.6289` n `135` status `ready` deltaP `17.9051` edge `0.5492` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.2828` n `135` status `ready` deltaP `24.965` edge `0.5417` maxDD `-15.4319`
- `market_context_high->crypto_alt_24h` score `3.8052` n `135` status `ready` deltaP `6.9445` edge `0.7583` maxDD `-30.6663`
- `market_context_high->crypto_major_4h` score `3.7559` n `135` status `ready` deltaP `15.359` edge `0.3916` maxDD `-10.1468`
- `market_context_high->index_24h` score `1.1923` n `135` status `ready` deltaP `11.5856` edge `0.1202` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.0552` n `135` status `ready` deltaP `9.7006` edge `0.142` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0506` n `135` status `ready` deltaP `6.5583` edge `0.1488` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.5423` n `135` status `ready` deltaP `11.5267` edge `0.0525` maxDD `-2.3986`
- `market_context_high->crypto_major_1h` score `0.5238` n `135` status `ready` deltaP `6.8796` edge `0.1172` maxDD `-4.2199`
- `market_context_high->unknown_1h` score `0.0164` n `135` status `ready` deltaP `3.3023` edge `0.0335` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.1949` n `135` status `ready` deltaP `3.2945` edge `0.0112` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.304` n `135` status `ready` deltaP `4.3338` edge `0.0274` maxDD `-2.5301`
- `market_context_high->commodity_1h` score `-0.36` n `135` status `ready` deltaP `5.7053` edge `0.0198` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4485` n `135` status `ready` deltaP `0.0787` edge `0.0059` maxDD `-2.114`
- `market_context_high->fx_1h` score `-0.4634` n `135` status `ready` deltaP `0.3471` edge `0.0037` maxDD `-0.2373`
- `market_context_high->fx_24h` score `-0.7131` n `135` status `ready` deltaP `4.5833` edge `-0.0008` maxDD `-0.8011`
- `market_context_high->fx_4h` score `-0.8889` n `135` status `ready` deltaP `-0.2822` edge `0.0109` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-0.9855` n `135` status `ready` deltaP `-1.9605` edge `0.0148` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.0984` n `135` status `ready` deltaP `4.1622` edge `0.0257` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.2984` n `135` status `ready` deltaP `2.5564` edge `0.0152` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
