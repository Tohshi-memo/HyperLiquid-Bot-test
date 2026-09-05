# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T11:37:29.909776+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11019`

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

- `risk_on_high->unknown_4h` score `21.8549` n `143` status `ready` deltaP `7.106` edge `1.8357` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.8549` n `143` status `ready` deltaP `7.106` edge `1.8357` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `11.0193` n `228` status `ready` deltaP `7.8145` edge `0.9392` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.4783` n `37` status `ready` deltaP `25.1783` edge `0.4823` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.053` n `37` status `ready` deltaP `22.2222` edge `0.1896` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6162` n `37` status `ready` deltaP `17.1803` edge `0.2281` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.2054` n `37` status `ready` deltaP `22.1696` edge `0.0581` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `2.0214` n `37` status `ready` deltaP `12.8008` edge `0.1032` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.623` n `37` status `ready` deltaP `13.5338` edge `0.0841` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.1966` n `37` status `ready` deltaP `6.3158` edge `0.0759` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1862` n `37` status `ready` deltaP `14.873` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1843` n `37` status `ready` deltaP `14.1164` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_major_24h` score `0.9128` n `37` status `ready` deltaP `16.0567` edge `0.2876` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `0.8818` n `37` status `ready` deltaP `8.5775` edge `0.0428` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.5795` n `37` status `ready` deltaP `6.3983` edge `0.0385` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.4398` n `37` status `ready` deltaP `14.4003` edge `0.0422` maxDD `-3.1244`
- `risk_on_high->crypto_major_24h` score `0.4194` n `125` status `ready` deltaP `21.3972` edge `0.7667` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.4194` n `125` status `ready` deltaP `21.3972` edge `0.7667` maxDD `-56.9519`
- `market_context_high->equity_24h` score `0.1518` n `192` status `ready` deltaP `15.7986` edge `0.3487` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1363` n `152` status `ready` deltaP `13.0673` edge `0.0016` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
