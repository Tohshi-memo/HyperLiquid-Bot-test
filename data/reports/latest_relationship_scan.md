# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T03:52:17.461410+00:00`
- Price records: `515`
- Market context records: `610`
- Flow alert records: `1724`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `5.0188` n `146` status `ready` deltaP `7.4297` edge `0.3735` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.3839` n `146` status `ready` deltaP `12.7832` edge `0.3135` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0304` n `146` status `ready` deltaP `9.9364` edge `0.017` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3408` n `146` status `ready` deltaP `1.6225` edge `0.0033` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6318` n `146` status `ready` deltaP `1.1996` edge `0.0368` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6767` n `146` status `ready` deltaP `0.2094` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0225` n `146` status `ready` deltaP `-3.1311` edge `-0.004` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.0382` n `146` status `ready` deltaP `6.2623` edge `0.0032` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2238` n `146` status `ready` deltaP `-1.763` edge `-0.0092` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.5786` n `146` status `ready` deltaP `4.9839` edge `0.0922` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6213` n `146` status `ready` deltaP `6.1643` edge `-0.0039` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.2548` n `146` status `ready` deltaP `-0.184` edge `-0.0344` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3378` n `146` status `ready` deltaP `14.2024` edge `0.0811` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.6481` n `146` status `ready` deltaP `-7.3593` edge `0.0279` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.1517` n `146` status `ready` deltaP `-2.8103` edge `-0.0287` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3083` n `146` status `ready` deltaP `-4.5989` edge `-0.0491` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7438` n `146` status `ready` deltaP `-6.7635` edge `0.0832` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2638` n `146` status `ready` deltaP `-2.5582` edge `-0.0124` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6691` n `146` status `ready` deltaP `-10.9226` edge `-0.0558` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.7742` n `146` status `ready` deltaP `1.9752` edge `-0.2232` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
