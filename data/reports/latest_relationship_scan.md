# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T08:22:16.483168+00:00`
- Price records: `672`
- Market context records: `994`
- Flow alert records: `4769`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `12.8577` n `211` status `ready` deltaP `31.4892` edge `0.9204` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1364` n `211` status `ready` deltaP `10.7705` edge `0.3963` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3522` n `211` status `ready` deltaP `1.9823` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5092` n `211` status `ready` deltaP `2.7819` edge `0.0198` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6419` n `211` status `ready` deltaP `1.106` edge `0.016` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.6971` n `211` status `ready` deltaP `3.0333` edge `0.1212` maxDD `-5.9609`
- `market_context_high->index_1h` score `-0.7452` n `211` status `ready` deltaP `2.7527` edge `0.0049` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7477` n `211` status `ready` deltaP `0.4619` edge `0.0007` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-1.203` n `211` status `ready` deltaP `4.5035` edge `0.1302` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2378` n `211` status `ready` deltaP `4.5017` edge `-0.0164` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.5184` n `211` status `ready` deltaP `1.7664` edge `0.0769` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7536` n `211` status `ready` deltaP `-1.7493` edge `0.0178` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8983` n `211` status `ready` deltaP `-1.3111` edge `-0.0387` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0806` n `211` status `ready` deltaP `-0.8875` edge `-0.0235` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9652` n `211` status `ready` deltaP `6.8404` edge `0.0779` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.2906` n `211` status `ready` deltaP `-2.0478` edge `0.0562` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3519` n `211` status `ready` deltaP `-2.0876` edge `0.0124` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5949` n `211` status `ready` deltaP `-1.6129` edge `-0.0222` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.6091` n `211` status `ready` deltaP `-4.8921` edge `-0.1626` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.2573` n `211` status `ready` deltaP `2.6184` edge `0.3887` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
