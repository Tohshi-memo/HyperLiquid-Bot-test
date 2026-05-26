# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T10:16:18.411733+00:00`
- Price records: `672`
- Market context records: `1936`
- Flow alert records: `7472`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7541`

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

- `market_context_high->crypto_alt_4h` score `6.9899` n `215` status `ready` deltaP `22.1788` edge `0.5491` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.3594` n `215` status `ready` deltaP `25.7629` edge `0.4828` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.0676` n `215` status `ready` deltaP `15.4991` edge `0.3547` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0327` n `215` status `ready` deltaP `13.6267` edge `0.188` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.6962` n `197` status `ready` deltaP `14.7534` edge `0.4917` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5576` n `227` status `ready` deltaP `7.5424` edge `0.0948` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4408` n `227` status `ready` deltaP `7.2002` edge `0.1001` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2041` n `197` status `ready` deltaP `11.8664` edge `0.1805` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1473` n `197` status `ready` deltaP `4.3218` edge `0.1063` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.0871` n `215` status `ready` deltaP `7.8538` edge `0.0638` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1825` n `227` status `ready` deltaP `4.8861` edge `0.0316` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2926` n `197` status `ready` deltaP `9.7831` edge `0.0153` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.599` n `227` status `ready` deltaP `-2.1407` edge `0.0007` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6615` n `227` status `ready` deltaP `0.2328` edge `0.0065` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7676` n `227` status `ready` deltaP `3.4451` edge `0.0122` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.9184` n `215` status `ready` deltaP `-4.2038` edge `-0.0009` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.0748` n `197` status `ready` deltaP `7.9015` edge `0.3476` maxDD `-33.1875`
- `market_context_high->metal_4h` score `-1.4244` n `215` status `ready` deltaP `7.4829` edge `0.1006` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.4309` n `227` status `ready` deltaP `0.7419` edge `-0.029` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.9771` n `227` status `ready` deltaP `1.2339` edge `-0.0059` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
