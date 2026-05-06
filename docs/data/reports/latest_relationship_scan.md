# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T19:52:21.798958+00:00`
- Price records: `483`
- Market context records: `575`
- Flow alert records: `1624`
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

- `market_context_high->crypto_alt_24h` score `4.798` n `146` status `ready` deltaP `7.3254` edge `0.3558` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9157` n `146` status `ready` deltaP `9.6103` edge `0.2123` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0336` n `146` status `ready` deltaP `10.703` edge `0.0201` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2731` n `146` status `ready` deltaP `2.744` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5145` n `146` status `ready` deltaP `2.261` edge `0.0395` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6893` n `146` status `ready` deltaP `0.1168` edge `-0.0038` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1445` n `146` status `ready` deltaP `-3.9208` edge `-0.0089` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2661` n `146` status `ready` deltaP `4.8846` edge `-0.0066` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2971` n `146` status `ready` deltaP `-2.199` edge `-0.0124` maxDD `-4.4826`
- `market_context_high->index_24h` score `-1.8532` n `146` status `ready` deltaP `-5.6279` edge `0.0826` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9279` n `146` status `ready` deltaP `4.0566` edge `-0.0154` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.174` n `146` status `ready` deltaP `0.7056` edge `-0.0336` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2008` n `146` status `ready` deltaP `2.9671` edge `0.0538` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.0393` n `146` status `ready` deltaP `11.1041` edge `0.0433` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.2666` n `146` status `ready` deltaP `-3.182` edge `-0.0358` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3093` n `146` status `ready` deltaP `-4.6716` edge `-0.0487` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5127` n `146` status `ready` deltaP `-5.4942` edge `0.094` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.7133` n `146` status `ready` deltaP `-9.775` edge `0.0162` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.6011` n `146` status `ready` deltaP `-5.1755` edge `-0.0382` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.1883` n `146` status `ready` deltaP `0.7436` edge `-0.2495` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
