# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T13:07:31.262131+00:00`
- Price records: `672`
- Market context records: `5559`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11378`

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

- `market_context_high->equity_24h` score `4.3934` n `186` status `ready` deltaP `15.2273` edge `0.7725` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.5644` n `191` status `ready` deltaP `11.3428` edge `0.284` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.5279` n `186` status `ready` deltaP `15.653` edge `0.477` maxDD `-29.6555`
- `market_context_high->equity_4h` score `1.0965` n `191` status `ready` deltaP `7.6706` edge `0.2041` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.0822` n `191` status `ready` deltaP `6.7896` edge `0.209` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.7063` n `186` status `ready` deltaP `16.5211` edge `0.0461` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.1604` n `201` status `ready` deltaP `7.3942` edge `0.0606` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0405` n `201` status `ready` deltaP `5.215` edge `0.0112` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2108` n `201` status `ready` deltaP `2.1286` edge `0.0644` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3043` n `201` status `ready` deltaP `1.3406` edge `0.0007` maxDD `-0.5589`
- `market_context_high->crypto_major_1h` score `-0.3708` n `201` status `ready` deltaP `3.6829` edge `0.0691` maxDD `-6.9639`
- `market_context_high->fx_4h` score `-0.4162` n `191` status `ready` deltaP `5.2252` edge `0.0083` maxDD `-1.2255`
- `market_context_high->metal_1h` score `-0.4749` n `201` status `ready` deltaP `0.0506` edge `0.0063` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-1.4227` n `201` status `ready` deltaP `-4.7264` edge `-0.0105` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5697` n `191` status `ready` deltaP `1.7726` edge `0.0183` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0303` n `186` status `ready` deltaP `12.2536` edge `0.0567` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0937` n `191` status `ready` deltaP `-13.0459` edge `-0.0572` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7236` n `191` status `ready` deltaP `-9.9572` edge `-0.0597` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.6172` n `186` status `ready` deltaP `-5.4603` edge `-0.2024` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.8786` n `186` status `ready` deltaP `6.4292` edge `0.1703` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
