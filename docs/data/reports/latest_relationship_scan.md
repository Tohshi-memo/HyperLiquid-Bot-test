# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T17:37:26.731498+00:00`
- Price records: `672`
- Market context records: `7587`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14550`

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

- `market_context_high->commodity_4h` score `0.098` n `155` status `ready` deltaP `9.0263` edge `0.024` maxDD `-2.4139`
- `market_context_high->commodity_24h` score `0.0402` n `147` status `ready` deltaP `13.4395` edge `0.0721` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0268` n `155` status `ready` deltaP `5.9508` edge `0.0126` maxDD `-0.9072`
- `market_context_high->unknown_24h` score `-0.1754` n `148` status `ready` deltaP `10.3792` edge `0.0999` maxDD `-7.6597`
- `market_context_high->commodity_1h` score `-0.2349` n `155` status `ready` deltaP `5.2116` edge `0.0029` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.4388` n `155` status `ready` deltaP `0.6683` edge `0.0139` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.4527` n `155` status `ready` deltaP `6.3715` edge `0.0147` maxDD `-5.5504`
- `market_context_high->fx_24h` score `-0.4592` n `147` status `ready` deltaP `8.6611` edge `0.0162` maxDD `-3.3097`
- `market_context_high->equity_1h` score `-0.591` n `155` status `ready` deltaP `5.7561` edge `0.0554` maxDD `-8.8965`
- `market_context_high->index_4h` score `-0.6059` n `155` status `ready` deltaP `9.5936` edge `0.031` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.6176` n `155` status `ready` deltaP `-0.0503` edge `-0.0012` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.8873` n `155` status `ready` deltaP `1.8766` edge `0.0181` maxDD `-1.0307`
- `market_context_high->unknown_1h` score `-0.9768` n `155` status `ready` deltaP `-0.1159` edge `-0.0621` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.1801` n `155` status `ready` deltaP `1.6483` edge `0.0475` maxDD `-10.1158`
- `market_context_high->crypto_major_4h` score `-1.602` n `155` status `ready` deltaP `6.4693` edge `0.0552` maxDD `-16.63`
- `market_context_high->metal_4h` score `-1.6593` n `155` status `ready` deltaP `-1.5667` edge `0.0459` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.7217` n `155` status `ready` deltaP `2.1575` edge `0.2016` maxDD `-21.9375`
- `market_context_high->fx_4h` score `-2.3155` n `155` status `ready` deltaP `-3.2534` edge `-0.0028` maxDD `-2.1439`
- `market_context_high->equity_24h` score `-2.69` n `147` status `ready` deltaP `15.9449` edge `0.4461` maxDD `-64.4486`
- `market_context_high->unknown_4h` score `-2.7367` n `155` status `ready` deltaP `10.4435` edge `-0.1933` maxDD `-5.5077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
