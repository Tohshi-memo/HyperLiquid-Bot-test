# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T13:07:12.936915+00:00`
- Price records: `672`
- Market context records: `1014`
- Flow alert records: `4829`
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

- `market_context_high->crypto_major_24h` score `13.3889` n `198` status `ready` deltaP `32.3092` edge `0.9592` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.2623` n `198` status `ready` deltaP `11.069` edge `0.4048` maxDD `-9.5387`
- `market_context_high->index_24h` score `0.1671` n `198` status `ready` deltaP `5.794` edge `0.157` maxDD `-4.8697`
- `market_context_high->equity_24h` score `0.1284` n `198` status `ready` deltaP `6.4534` edge `0.1828` maxDD `-9.2097`
- `market_context_high->fx_1h` score `-0.2264` n `198` status `ready` deltaP `2.4678` edge `0.0001` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4745` n `198` status `ready` deltaP `2.7506` edge `0.0229` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7614` n `198` status `ready` deltaP `-0.5671` edge `0.0172` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7698` n `198` status `ready` deltaP `2.2954` edge `0.0059` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.9415` n `198` status `ready` deltaP `2.7732` edge `0.0027` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2932` n `198` status `ready` deltaP `4.0208` edge `-0.0203` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.3639` n `198` status `ready` deltaP `2.3775` edge `0.0857` maxDD `-10.5498`
- `market_context_high->crypto_alt_1h` score `-1.3986` n `198` status `ready` deltaP `-1.686` edge `-0.0241` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5847` n `198` status `ready` deltaP `-1.0532` edge `0.0226` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.817` n `198` status `ready` deltaP `0.372` edge `-0.0395` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.94` n `198` status `ready` deltaP `6.7951` edge `0.0803` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-3.0397` n `198` status `ready` deltaP `-0.8546` edge `0.0302` maxDD `-15.2248`
- `market_context_high->commodity_4h` score `-3.153` n `198` status `ready` deltaP `-1.7831` edge `0.0659` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.3323` n `198` status `ready` deltaP `0.1824` edge `-0.0208` maxDD `-19.2774`
- `market_context_high->metal_4h` score `-4.4883` n `198` status `ready` deltaP `-3.1812` edge `-0.166` maxDD `-24.3905`
- `market_context_high->metal_24h` score `-8.0963` n `198` status `ready` deltaP `-9.61` edge `0.1951` maxDD `-52.7912`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
