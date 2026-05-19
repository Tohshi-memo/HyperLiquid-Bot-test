# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T19:52:18.945391+00:00`
- Price records: `672`
- Market context records: `1251`
- Flow alert records: `5508`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_major_24h` score `18.133` n `128` status `ready` deltaP `42.1006` edge `1.3436` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.1419` n `128` status `ready` deltaP `2.4306` edge `0.829` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `8.0083` n `128` status `ready` deltaP `5.221` edge `0.7542` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.6607` n `128` status `ready` deltaP `22.309` edge `0.6913` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.0382` n `128` status `ready` deltaP `23.4375` edge `0.2889` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.4147` n `128` status `ready` deltaP `-8.6806` edge `0.4906` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.3164` n `128` status `ready` deltaP `17.5495` edge `0.2257` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.2567` n `128` status `ready` deltaP `22.3958` edge `0.5009` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.0526` n `128` status `ready` deltaP `1.5625` edge `0.4336` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5289` n `128` status `ready` deltaP `13.891` edge `0.1031` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7356` n `128` status `ready` deltaP `10.3481` edge `0.024` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6985` n `128` status `ready` deltaP `6.3575` edge `0.0527` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.354` n `128` status `ready` deltaP `11.6158` edge `0.0131` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.2997` n `128` status `ready` deltaP `15.9109` edge `0.062` maxDD `-6.4478`
- `market_context_high->fx_24h` score `0.2796` n `128` status `ready` deltaP `5.4688` edge `0.0333` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `-0.0031` n `128` status `ready` deltaP `6.917` edge `0.1456` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0965` n `128` status `ready` deltaP `5.7495` edge `-0.0008` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2541` n `128` status `ready` deltaP `1.2444` edge `0.0434` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3965` n `128` status `ready` deltaP `2.5262` edge `0.0089` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6576` n `128` status `ready` deltaP `8.0983` edge `0.1582` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
