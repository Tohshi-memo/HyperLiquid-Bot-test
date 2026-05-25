# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T02:37:18.672409+00:00`
- Price records: `672`
- Market context records: `1801`
- Flow alert records: `7081`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `6.944` n `186` status `ready` deltaP `28.3154` edge `0.6325` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.4678` n `30` status `ready` deltaP `29.2582` edge `0.4094` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.9328` n `191` status `ready` deltaP `21.4891` edge `0.5175` maxDD `-8.6419`
- `market_context_high->crypto_major_4h` score `4.9716` n `191` status `ready` deltaP `24.3983` edge `0.4612` maxDD `-9.0979`
- `market_context_high->unknown_4h` score `4.1553` n `191` status `ready` deltaP `16.651` edge `0.4509` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2326` n `30` status `ready` deltaP `24.5709` edge `0.1373` maxDD `-1.2043`
- `market_context_high->index_24h` score `2.9033` n `186` status `ready` deltaP `14.2921` edge `0.2695` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.8731` n `191` status `ready` deltaP `15.9415` edge `0.2426` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9394` n `186` status `ready` deltaP `16.7339` edge `0.5399` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.2243` n `186` status `ready` deltaP `11.8896` edge `0.5548` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.8995` n `30` status `ready` deltaP `21.6362` edge `-0.0017` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8252` n `191` status `ready` deltaP `11.9652` edge `0.0979` maxDD `-3.7119`
- `news_risk_high->unknown_4h` score `0.3611` n `30` status `ready` deltaP `9.8272` edge `0.0531` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `0.3362` n `191` status `ready` deltaP `5.72` edge `0.0885` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.2587` n `191` status `ready` deltaP `6.5422` edge `0.0891` maxDD `-4.8924`
- `market_context_high->equity_1h` score `-0.2508` n `191` status `ready` deltaP `3.4721` edge `0.0368` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.4282` n `191` status `ready` deltaP `1.903` edge `0.0148` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4575` n `30` status `ready` deltaP `16.7066` edge `-0.1228` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.46` n `186` status `ready` deltaP `8.5909` edge `0.0093` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4718` n `30` status `ready` deltaP `-5.1297` edge `-0.0001` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
