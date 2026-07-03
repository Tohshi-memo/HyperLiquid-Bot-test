# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T13:19:06.148901+00:00`
- Price records: `672`
- Market context records: `5560`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11380`

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

- `market_context_high->equity_24h` score `4.361` n `185` status `ready` deltaP `15.3022` edge `0.7693` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4648` n `191` status `ready` deltaP `11.3428` edge `0.2757` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.4239` n `185` status `ready` deltaP `15.5077` edge `0.4693` maxDD `-29.6555`
- `market_context_high->equity_4h` score `1.0029` n `191` status `ready` deltaP `7.6706` edge `0.1963` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.9898` n `191` status `ready` deltaP `6.7896` edge `0.2013` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.7158` n `185` status `ready` deltaP `16.5494` edge `0.0467` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.0474` n `201` status `ready` deltaP `7.0464` edge `0.0535` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0513` n `201` status `ready` deltaP `5.215` edge `0.0103` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2792` n `201` status `ready` deltaP `2.1286` edge `0.0587` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.2833` n `201` status `ready` deltaP `1.6884` edge `0.0008` maxDD `-0.5364`
- `market_context_high->fx_4h` score `-0.3723` n `191` status `ready` deltaP `5.5964` edge `0.0087` maxDD `-1.1629`
- `market_context_high->crypto_major_1h` score `-0.4536` n `201` status `ready` deltaP `3.6829` edge `0.0622` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5054` n `201` status `ready` deltaP `-0.2972` edge `0.0047` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-1.3865` n `201` status `ready` deltaP `-4.3786` edge `-0.0098` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5805` n `191` status `ready` deltaP `1.7726` edge `0.0174` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0411` n `185` status `ready` deltaP `12.0908` edge `0.0564` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.1294` n `191` status `ready` deltaP `-13.417` edge `-0.0593` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.6855` n `191` status `ready` deltaP `-9.5861` edge `-0.059` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.6522` n `185` status `ready` deltaP `-5.7742` edge `-0.2048` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-8.0178` n `185` status `ready` deltaP `6.22` edge `0.1601` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
