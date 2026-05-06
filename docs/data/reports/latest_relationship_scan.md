# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T13:37:27.419077+00:00`
- Price records: `458`
- Market context records: `548`
- Flow alert records: `1547`
- Minimum samples: `30`
- Pattern count: `96`

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

- `market_context_high->crypto_alt_24h` score `4.9621` n `137` status `ready` deltaP `7.7866` edge `0.3664` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0562` n `137` status `ready` deltaP `10.1969` edge `0.2201` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0514` n `146` status `ready` deltaP `10.7306` edge `0.0222` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3269` n `146` status `ready` deltaP `1.7382` edge `0.0043` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.5626` n `146` status `ready` deltaP `1.8478` edge `0.0009` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.5851` n `146` status `ready` deltaP `1.723` edge `0.0372` maxDD `-3.7959`
- `market_context_high->unknown_1h` score `-0.8038` n `146` status `ready` deltaP `-2.8875` edge `0.0126` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1183` n `146` status `ready` deltaP `-0.8189` edge `-0.0067` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.4175` n `146` status `ready` deltaP `4.2514` edge `-0.015` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.8572` n `137` status `ready` deltaP `-6.0381` edge `0.085` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-2.1507` n `146` status `ready` deltaP `2.9811` edge `-0.0268` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.2736` n `146` status `ready` deltaP `0.0` edge `-0.0372` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.9298` n `146` status `ready` deltaP `0.4246` edge `0.01` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-2.972` n `146` status `ready` deltaP `0.8027` edge `-0.0652` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.2467` n `146` status `ready` deltaP `-4.7945` edge `0.1115` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.3019` n `146` status `ready` deltaP `-4.9696` edge `-0.0461` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.462` n `146` status `ready` deltaP `-4.1096` edge `-0.0459` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-3.7968` n `137` status `ready` deltaP `-10.4441` edge `0.0137` maxDD `-10.5047`
- `market_context_high->crypto_major_4h` score `-4.0379` n `146` status `ready` deltaP `7.8907` edge `-0.0185` maxDD `-22.648`
- `market_context_high->fx_24h` score `-4.1983` n `137` status `ready` deltaP `-5.4542` edge `-0.0399` maxDD `-16.6253`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
