# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T22:22:15.007921+00:00`
- Price records: `493`
- Market context records: `586`
- Flow alert records: `1657`
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

- `market_context_high->crypto_alt_24h` score `4.6619` n `146` status `ready` deltaP `7.1237` edge `0.3458` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.2078` n `146` status `ready` deltaP `9.9168` edge `0.2346` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.089` n `146` status `ready` deltaP `11.7076` edge `0.0205` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2794` n `146` status `ready` deltaP `2.6225` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6107` n `146` status `ready` deltaP `1.5534` edge `0.0362` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6484` n `146` status `ready` deltaP `0.7527` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.2016` n `146` status `ready` deltaP `-1.5153` edge `-0.009` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.219` n `146` status `ready` deltaP `-4.6726` edge `-0.0101` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3017` n `146` status `ready` deltaP `4.8744` edge `-0.0095` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.9104` n `146` status `ready` deltaP `4.1698` edge `-0.0147` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1677` n `146` status `ready` deltaP `2.9451` edge `0.0567` maxDD `-15.2248`
- `market_context_high->index_24h` score `-2.1917` n `146` status `ready` deltaP `-6.1992` edge `0.0582` maxDD `-5.9609`
- `market_context_high->index_4h` score `-2.2823` n `146` status `ready` deltaP `-0.0478` edge `-0.0376` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.9516` n `146` status `ready` deltaP `11.5404` edge `0.0477` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2911` n `146` status `ready` deltaP `-4.52` edge `-0.0482` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3767` n `146` status `ready` deltaP `-3.8533` edge `-0.0405` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.6564` n `146` status `ready` deltaP `-6.3454` edge `0.0877` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.2092` n `146` status `ready` deltaP `-10.1537` edge `-0.0226` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.4665` n `146` status `ready` deltaP `-4.3118` edge `-0.0267` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.091` n `146` status `ready` deltaP `1.0152` edge `-0.2432` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
