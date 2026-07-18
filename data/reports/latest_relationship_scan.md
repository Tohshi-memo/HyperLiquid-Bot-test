# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T03:07:30.147529+00:00`
- Price records: `672`
- Market context records: `7096`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.4358` n `159` status `ready` deltaP `16.7798` edge `0.014` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1317` n `159` status `ready` deltaP `4.6567` edge `0.0031` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2563` n `159` status `ready` deltaP `-0.4651` edge `0.0376` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.427` n `159` status `ready` deltaP `0.7043` edge `0.027` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4483` n `159` status `ready` deltaP `1.481` edge `-0.0054` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.5879` n `159` status `ready` deltaP `3.5194` edge `0.0364` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8259` n `159` status `ready` deltaP `-3.7576` edge `-0.0192` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3823` n `159` status `ready` deltaP `-4.5435` edge `-0.0434` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4332` n `159` status `ready` deltaP `-5.6774` edge `-0.0048` maxDD `-2.1427`
- `market_context_high->unknown_4h` score `-1.671` n `159` status `ready` deltaP `-7.7303` edge `-0.0025` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0649` n `159` status `ready` deltaP `2.7388` edge `-0.0407` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3612` n `159` status `ready` deltaP `1.2281` edge `-0.041` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-2.984` n `159` status `ready` deltaP `4.393` edge `0.0166` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.0545` n `159` status `ready` deltaP `-6.2041` edge `-0.0823` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.1532` n `159` status `ready` deltaP `-0.8869` edge `-0.0198` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.2101` n `159` status `ready` deltaP `-7.4292` edge `-0.0186` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.2703` n `159` status `ready` deltaP `-7.1599` edge `-0.0098` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.4193` n `159` status `ready` deltaP `1.0565` edge `-0.1994` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.8098` n `159` status `ready` deltaP `-23.2311` edge `-0.0646` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.0906` n `159` status `ready` deltaP `-24.7445` edge `-0.1337` maxDD `-43.3777`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
