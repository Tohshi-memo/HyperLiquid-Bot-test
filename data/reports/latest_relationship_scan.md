# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T09:52:11.860785+00:00`
- Price records: `539`
- Market context records: `635`
- Flow alert records: `1798`
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

- `market_context_high->crypto_major_24h` score `5.9947` n `146` status `ready` deltaP `17.063` edge `0.4192` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.4565` n `146` status `ready` deltaP `7.4415` edge `0.4099` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.094` n `146` status `ready` deltaP `8.8936` edge `0.0158` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3406` n `146` status `ready` deltaP `1.6704` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.48` n `146` status `ready` deltaP `2.1825` edge `0.0429` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6988` n `146` status `ready` deltaP `-0.2464` edge `-0.0026` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1455` n `146` status `ready` deltaP `-4.1428` edge `-0.0075` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2111` n `146` status `ready` deltaP `5.692` edge `-0.0074` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3392` n `146` status `ready` deltaP `-2.6946` edge `-0.0126` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7168` n `146` status `ready` deltaP `5.5703` edge `-0.0079` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0837` n `146` status `ready` deltaP `4.0402` edge `0.0564` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3979` n `146` status `ready` deltaP `-1.5982` edge `-0.0369` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.545` n `146` status `ready` deltaP `13.218` edge `0.0704` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0519` n `146` status `ready` deltaP `-8.4922` edge `0.0018` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.3971` n `146` status `ready` deltaP `-5.4451` edge `0.1033` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4419` n `146` status `ready` deltaP `-5.2042` edge `-0.0562` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4601` n `146` status `ready` deltaP `-4.2957` edge `-0.0445` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.3409` n `146` status `ready` deltaP `-3.3514` edge `-0.017` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7909` n `146` status `ready` deltaP `1.5571` edge `-0.2218` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.9236` n `146` status `ready` deltaP `-11.6734` edge `-0.072` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
