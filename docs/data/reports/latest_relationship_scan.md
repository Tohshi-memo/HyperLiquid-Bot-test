# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T12:22:35.601653+00:00`
- Price records: `672`
- Market context records: `5556`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11378`

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

- `market_context_high->equity_24h` score `4.4422` n `189` status `ready` deltaP `14.9967` edge `0.7781` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.8368` n `191` status `ready` deltaP `11.3428` edge `0.3067` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.7613` n `189` status `ready` deltaP `16.0797` edge `0.4936` maxDD `-29.6555`
- `market_context_high->equity_4h` score `1.3293` n `191` status `ready` deltaP `7.6706` edge `0.2235` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.315` n `191` status `ready` deltaP `6.7896` edge `0.2284` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.6832` n `189` status `ready` deltaP `16.4269` edge `0.0448` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.2455` n `203` status `ready` deltaP `7.4526` edge `0.0673` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0302` n `203` status `ready` deltaP `5.2838` edge `0.0116` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.1314` n `203` status `ready` deltaP `2.4151` edge `0.0691` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2894` n `203` status `ready` deltaP `3.8443` edge `0.0748` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3072` n `203` status `ready` deltaP `1.3185` edge `0.0007` maxDD `-0.577`
- `market_context_high->fx_4h` score `-0.5394` n `191` status `ready` deltaP `4.1118` edge `0.0075` maxDD `-1.3888`
- `market_context_high->metal_1h` score `-0.7005` n `203` status `ready` deltaP `0.2463` edge `0.0075` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.5421` n `191` status `ready` deltaP `1.7726` edge `0.0206` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6002` n `203` status `ready` deltaP `-5.5153` edge `-0.0117` maxDD `-3.7906`
- `market_context_high->index_24h` score `-2.0204` n `189` status `ready` deltaP `12.3843` edge `0.0571` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5961` n `191` status `ready` deltaP `-11.9325` edge `-0.051` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7155` n `191` status `ready` deltaP `-9.9572` edge `-0.0604` maxDD `-13.9606`
- `market_context_high->metal_24h` score `-7.5131` n `189` status `ready` deltaP `-4.5387` edge `-0.1952` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.5427` n `189` status `ready` deltaP `7.0437` edge `0.1942` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
