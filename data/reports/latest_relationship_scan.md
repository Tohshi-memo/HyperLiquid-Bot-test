# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T11:07:13.291464+00:00`
- Price records: `672`
- Market context records: `1006`
- Flow alert records: `4803`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.053` n `206` status `ready` deltaP `31.9959` edge `0.9333` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1662` n `206` status `ready` deltaP `10.9475` edge `0.3976` maxDD `-9.5387`
- `market_context_high->index_24h` score `-0.4817` n `206` status `ready` deltaP `3.8095` edge `0.1303` maxDD `-5.6669`
- `market_context_high->fx_1h` score `-0.5022` n `206` status `ready` deltaP `2.4185` edge `0.0001` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.6203` n `206` status `ready` deltaP `1.8734` edge `0.0166` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.695` n `206` status `ready` deltaP `3.2905` edge `0.0055` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-0.7051` n `206` status `ready` deltaP `0.3008` edge `0.0161` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.7143` n `206` status `ready` deltaP `0.999` edge `0.0014` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-1.0695` n `206` status `ready` deltaP `4.4473` edge `0.1417` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2346` n `206` status `ready` deltaP `4.773` edge `-0.0178` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3813` n `206` status `ready` deltaP `-1.324` edge `-0.0243` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5113` n `206` status `ready` deltaP `1.6147` edge `0.0785` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7766` n `206` status `ready` deltaP `-1.9921` edge `0.0175` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8493` n `206` status `ready` deltaP `-0.3851` edge `-0.0386` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.9074` n `206` status `ready` deltaP `6.993` edge `0.0817` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.1533` n `206` status `ready` deltaP `-1.3365` edge `0.0629` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3023` n `206` status `ready` deltaP `-2.0528` edge `0.0163` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.4715` n `206` status `ready` deltaP `-1.2595` edge `-0.0221` maxDD `-19.8319`
- `market_context_high->metal_4h` score `-4.6039` n `206` status `ready` deltaP `-4.6531` edge `-0.1656` maxDD `-24.8228`
- `market_context_high->commodity_24h` score `-8.2885` n `206` status `ready` deltaP `2.3635` edge `0.3864` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
