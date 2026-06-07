# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T20:37:27.069807+00:00`
- Price records: `672`
- Market context records: `3214`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `11248`

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

- `market_context_high->commodity_24h` score `13.7513` n `101` status `ready` deltaP `47.8599` edge `0.8697` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.8248` n `101` status `ready` deltaP `14.4304` edge `2.4174` maxDD `-71.142`
- `market_context_high->index_24h` score `9.3475` n `101` status `ready` deltaP `29.2216` edge `0.8396` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.2623` n `101` status `ready` deltaP `13.8115` edge `1.4242` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4655` n `127` status `ready` deltaP `22.6943` edge `0.1833` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.5041` n `139` status `ready` deltaP `6.8055` edge `0.0389` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.324` n `101` status `ready` deltaP `6.1176` edge `-0.0079` maxDD `-1.1239`
- `market_context_high->unknown_4h` score `-0.6162` n `127` status `ready` deltaP `9.2063` edge `0.1095` maxDD `-14.7778`
- `market_context_high->index_1h` score `-0.9781` n `139` status `ready` deltaP `2.6052` edge `0.0074` maxDD `-4.5023`
- `market_context_high->fx_4h` score `-1.028` n `127` status `ready` deltaP `-5.7783` edge `-0.0048` maxDD `-1.4115`
- `market_context_high->crypto_major_1h` score `-1.0956` n `139` status `ready` deltaP `4.1894` edge `0.0579` maxDD `-15.1032`
- `market_context_high->crypto_alt_1h` score `-1.4952` n `139` status `ready` deltaP `4.0441` edge `0.0739` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.6181` n `139` status `ready` deltaP `-9.2341` edge `-0.0046` maxDD `-0.8278`
- `market_context_high->index_4h` score `-1.7721` n `127` status `ready` deltaP `13.1445` edge `0.0556` maxDD `-17.6057`
- `market_context_high->equity_1h` score `-1.8304` n `139` status `ready` deltaP `1.1373` edge `-0.0032` maxDD `-8.8863`
- `market_context_high->metal_1h` score `-2.3261` n `139` status `ready` deltaP `-4.9466` edge `-0.0131` maxDD `-8.1543`
- `market_context_high->unknown_1h` score `-2.8576` n `139` status `ready` deltaP `0.7841` edge `-0.1237` maxDD `-17.8311`
- `market_context_high->crypto_major_24h` score `-4.0271` n `101` status `ready` deltaP `12.8438` edge `1.6974` maxDD `-166.279`
- `market_context_high->crypto_major_4h` score `-4.8324` n `127` status `ready` deltaP `4.3091` edge `0.1441` maxDD `-54.3896`
- `market_context_high->equity_4h` score `-5.0176` n `127` status `ready` deltaP `11.8242` edge `0.0336` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
