# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T02:52:26.479062+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6730`

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

- `market_context_high->unknown_1h` score `318.4696` n `50` status `ready` deltaP `6.8323` edge `26.4985` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.5314` n `50` status `ready` deltaP `6.7073` edge `23.3329` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.988` n `135` status `ready` deltaP `29.2477` edge `1.4083` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9511` n `50` status `ready` deltaP `18.9146` edge `0.5235` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4855` n `135` status `ready` deltaP `23.6459` edge `0.6982` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.4363` n `135` status `ready` deltaP `24.9074` edge `0.6052` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.9929` n `50` status `ready` deltaP `14.6646` edge `0.3643` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0286` n `50` status `ready` deltaP `15.6467` edge `0.1931` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8297` n `135` status `ready` deltaP `21.8866` edge `0.2173` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.8291` n `50` status `ready` deltaP `31.9268` edge `0.0364` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.7228` n `135` status `ready` deltaP `25.8912` edge `0.1021` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6962` n `50` status `ready` deltaP `13.4551` edge `0.2013` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.003` n `135` status `ready` deltaP `24.1407` edge `0.1661` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3801` n `50` status `ready` deltaP `19.5928` edge `0.0108` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.6155` n `135` status `ready` deltaP `7.3054` edge `0.0649` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5981` n `135` status `ready` deltaP `7.4551` edge `0.0912` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.3651` n `135` status `ready` deltaP `8.3683` edge `0.2406` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.3436` n `135` status `ready` deltaP `7.3209` edge `0.0086` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0051` n `50` status `ready` deltaP `8.8982` edge `-0.0063` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1145` n `50` status `ready` deltaP `-0.6946` edge `0.055` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
