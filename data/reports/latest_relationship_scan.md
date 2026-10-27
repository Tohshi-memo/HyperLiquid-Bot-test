# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T13:07:30.278953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8856`

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

- `market_context_high->unknown_4h` score `81.0463` n `135` status `ready` deltaP `5.3094` edge `6.7337` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.0036` n `135` status `ready` deltaP `1.069` edge `1.2921` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9217` n `132` status `ready` deltaP `26.7055` edge `0.0509` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4835` n `135` status `ready` deltaP `10.906` edge `0.0034` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4079` n `135` status `ready` deltaP `12.5915` edge `0.0099` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0359` n `135` status `ready` deltaP `10.346` edge `0.0103` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3405` n `135` status `ready` deltaP `1.6789` edge `0.0105` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4615` n `135` status `ready` deltaP `6.1854` edge `0.0279` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5609` n `135` status `ready` deltaP `-0.2129` edge `-0.0022` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.6646` n `132` status `ready` deltaP `8.0589` edge `0.0183` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.6727` n `135` status `ready` deltaP `4.0978` edge `0.0385` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.7629` n `135` status `ready` deltaP `8.4711` edge `-0.0002` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.1382` n `132` status `ready` deltaP `14.3479` edge `0.0873` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3856` n `135` status `ready` deltaP `2.3397` edge `-0.002` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9452` n `135` status `ready` deltaP `-1.0413` edge `-0.0061` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.4782` n `132` status `ready` deltaP `7.2015` edge `0.0419` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.6257` n `135` status `ready` deltaP `-4.4885` edge `-0.0267` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5845` n `135` status `ready` deltaP `4.4219` edge `-0.0571` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.3613` n `132` status `ready` deltaP `-0.8443` edge `-0.0678` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.985` n `135` status `ready` deltaP `2.395` edge `-0.1317` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
