# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T20:22:31.435504+00:00`
- Price records: `672`
- Market context records: `5808`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9076`

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

- `market_context_high->equity_24h` score `0.2321` n `248` status `ready` deltaP `15.3954` edge `0.4246` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.0658` n `292` status `ready` deltaP `5.6549` edge `0.1181` maxDD `-7.0251`
- `market_context_high->fx_1h` score `-0.2082` n `292` status `ready` deltaP `3.0822` edge `0.0013` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.626` n `292` status `ready` deltaP `-1.4786` edge `-0.0033` maxDD `-2.7017`
- `market_context_high->index_1h` score `-0.6478` n `292` status `ready` deltaP `0.0882` edge `0.0032` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6646` n `292` status `ready` deltaP `1.9707` edge `-0.001` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6925` n `292` status `ready` deltaP `2.5326` edge `0.0261` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9385` n `292` status `ready` deltaP `2.8484` edge `0.0349` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1256` n `292` status `ready` deltaP `1.2222` edge `0.0315` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2539` n `292` status `ready` deltaP `-0.1984` edge `0.0093` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.3556` n `248` status `ready` deltaP `10.8199` edge `0.033` maxDD `-5.3147`
- `market_context_high->fx_4h` score `-1.4117` n `292` status `ready` deltaP `1.443` edge `0.0043` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2713` n `292` status `ready` deltaP `-4.4228` edge `-0.045` maxDD `-10.0034`
- `market_context_high->crypto_major_4h` score `-2.758` n `292` status `ready` deltaP `7.9812` edge `0.1542` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.8627` n `292` status `ready` deltaP `-2.2302` edge `-0.0186` maxDD `-9.0741`
- `market_context_high->index_24h` score `-4.3225` n `248` status `ready` deltaP `3.7131` edge `0.0295` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4155` n `292` status `ready` deltaP `5.6987` edge `0.0949` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.8082` n `248` status `ready` deltaP `-4.9955` edge `-0.2388` maxDD `-21.1362`
- `market_context_high->commodity_24h` score `-9.4626` n `248` status `ready` deltaP `-13.1496` edge `-0.0679` maxDD `-33.3057`
- `market_context_high->crypto_major_24h` score `-10.9964` n `248` status `ready` deltaP `-1.9937` edge `-0.2497` maxDD `-34.9364`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
