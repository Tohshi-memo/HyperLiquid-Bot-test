# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T02:22:29.546640+00:00`
- Price records: `672`
- Market context records: `5411`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11492`

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

- `market_context_high->crypto_major_24h` score `4.1769` n `194` status `ready` deltaP `19.9348` edge `0.6692` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.9173` n `205` status `ready` deltaP `16.7683` edge `0.4439` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.148` n `205` status `ready` deltaP `12.3781` edge `0.3439` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.4362` n `205` status `ready` deltaP `12.0427` edge `0.2866` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3649` n `205` status `ready` deltaP `7.3105` edge `0.0782` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1173` n `205` status `ready` deltaP `4.9233` edge `0.1015` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.0604` n `205` status `ready` deltaP `5.8756` edge `0.0152` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `0.0372` n `205` status `ready` deltaP `2.5281` edge `0.0824` maxDD `-5.0257`
- `market_context_high->fx_24h` score `-0.0555` n `194` status `ready` deltaP `8.2063` edge `0.0302` maxDD `-0.8294`
- `market_context_high->equity_24h` score `-0.2084` n `194` status `ready` deltaP `8.0327` edge `0.5128` maxDD `-40.0306`
- `market_context_high->fx_1h` score `-0.4641` n `205` status `ready` deltaP `-1.4028` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.561` n `205` status `ready` deltaP `1.4802` edge `0.0109` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9337` n `205` status `ready` deltaP `6.7073` edge `0.0384` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2499` n `205` status `ready` deltaP `-0.3658` edge `0.0012` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4579` n `205` status `ready` deltaP `-3.021` edge `-0.0069` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6307` n `194` status `ready` deltaP `12.8275` edge `0.0772` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.503` n `205` status `ready` deltaP `-6.0671` edge `-0.028` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2669` n `205` status `ready` deltaP `-6.9817` edge `-0.0452` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.9839` n `194` status `ready` deltaP `11.1988` edge `0.2964` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0289` n `194` status `ready` deltaP `-4.4226` edge `-0.1339` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
