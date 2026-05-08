# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T09:07:19.502592+00:00`
- Price records: `632`
- Market context records: `739`
- Flow alert records: `2087`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.5974` n `146` status `ready` deltaP `30.0271` edge `0.883` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.582` n `146` status `ready` deltaP `7.7106` edge `0.5019` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.0824` n `146` status `ready` deltaP `1.2411` edge `0.1981` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.2806` n `155` status `ready` deltaP `6.2502` edge `0.0095` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3688` n `159` status `ready` deltaP `3.6708` edge `0.0026` maxDD `-0.291`
- `market_context_high->equity_24h` score `-0.6229` n `146` status `ready` deltaP `-0.4094` edge `0.2113` maxDD `-10.5047`
- `market_context_high->equity_1h` score `-0.6386` n `159` status `ready` deltaP `-0.3961` edge `0.0018` maxDD `-4.4826`
- `market_context_high->commodity_1h` score `-0.6465` n `159` status `ready` deltaP `1.016` edge `0.0368` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.8433` n `159` status `ready` deltaP `1.527` edge `0.0049` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.06` n `159` status `ready` deltaP `5.7915` edge `-0.0022` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4261` n `159` status `ready` deltaP `4.2944` edge `-0.016` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5229` n `159` status `ready` deltaP `-4.4306` edge `-0.0202` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5386` n `155` status `ready` deltaP `17.5629` edge `0.1253` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7594` n `155` status `ready` deltaP `1.7626` edge `-0.0061` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1545` n `155` status `ready` deltaP `2.4655` edge `0.061` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5628` n `155` status `ready` deltaP `-1.1786` edge `0.0095` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.0782` n `159` status `ready` deltaP `-3.388` edge `-0.038` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7215` n `155` status `ready` deltaP `-5.8392` edge `0.0789` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7543` n `155` status `ready` deltaP `5.1089` edge `-0.1591` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3464` n `146` status `ready` deltaP `-15.2179` edge `-0.0668` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
