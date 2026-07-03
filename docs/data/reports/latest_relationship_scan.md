# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T13:52:30.162887+00:00`
- Price records: `672`
- Market context records: `5563`
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

- `market_context_high->equity_24h` score `4.3583` n `183` status `ready` deltaP `15.4486` edge `0.7681` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.376` n `191` status `ready` deltaP `11.3428` edge `0.2683` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.2863` n `183` status `ready` deltaP `15.2123` edge `0.4598` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `0.889` n `191` status `ready` deltaP `6.7896` edge `0.1929` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.8721` n `191` status `ready` deltaP `7.6706` edge `0.1854` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.7331` n `183` status `ready` deltaP `16.6012` edge `0.0478` maxDD `-1.457`
- `market_context_high->index_1h` score `-0.0899` n `201` status `ready` deltaP `4.8671` edge `0.0094` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.0971` n `201` status `ready` deltaP `6.3508` edge `0.0461` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.3068` n `201` status `ready` deltaP `2.1286` edge `0.0564` maxDD `-5.0257`
- `market_context_high->fx_4h` score `-0.3201` n `191` status `ready` deltaP `5.9674` edge `0.0091` maxDD `-1.0447`
- `market_context_high->fx_1h` score `-0.431` n `201` status `ready` deltaP `1.6884` edge `0.0009` maxDD `-0.5123`
- `market_context_high->crypto_major_1h` score `-0.498` n `201` status `ready` deltaP `3.6829` edge `0.0585` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5642` n `201` status `ready` deltaP `-0.9928` edge `0.0018` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-1.3152` n `201` status `ready` deltaP `-3.6829` edge `-0.0085` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5961` n `191` status `ready` deltaP `1.7726` edge `0.0161` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0524` n `183` status `ready` deltaP `11.9336` edge `0.056` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.1961` n `191` status `ready` deltaP `-14.1593` edge `-0.0629` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.6166` n `191` status `ready` deltaP `-8.8438` edge `-0.0582` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.7182` n `183` status `ready` deltaP `-6.4122` edge `-0.209` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-8.2306` n `183` status `ready` deltaP `5.7946` edge `0.1452` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
