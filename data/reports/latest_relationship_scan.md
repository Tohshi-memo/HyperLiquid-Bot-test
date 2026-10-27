# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T08:22:27.528911+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9438`

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

- `market_context_high->unknown_4h` score `87.2619` n `135` status `ready` deltaP `5.0045` edge `7.2537` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `26.0735` n `135` status `ready` deltaP `1.6678` edge `2.2106` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.6926` n `121` status `ready` deltaP `25.7459` edge `0.0382` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4727` n `135` status `ready` deltaP `10.7563` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4493` n `135` status `ready` deltaP `13.0488` edge `0.0103` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.1091` n `135` status `ready` deltaP `11.5436` edge `0.0117` maxDD `-1.3073`
- `market_context_high->metal_24h` score `-0.3061` n `121` status `ready` deltaP `16.4716` edge `0.1035` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.3165` n `135` status `ready` deltaP `1.9783` edge `0.0105` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.5043` n `135` status `ready` deltaP `5.2872` edge `0.0284` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5219` n `135` status `ready` deltaP `0.3859` edge `-0.0012` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.58` n `121` status `ready` deltaP `9.3115` edge `0.0208` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5852` n `135` status `ready` deltaP `5.0124` edge `0.0397` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.65` n `135` status `ready` deltaP `10.1479` edge `0.0031` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.2968` n `135` status `ready` deltaP `2.9385` edge `0.0054` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9881` n `135` status `ready` deltaP `-1.4904` edge `-0.0086` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.0072` n `121` status `ready` deltaP `4.4846` edge `0.0092` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.4838` n `135` status `ready` deltaP `-3.269` edge `-0.023` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.668` n `135` status `ready` deltaP `3.5072` edge `-0.0617` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.6214` n `121` status `ready` deltaP `-0.1003` edge `-0.1061` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7162` n `135` status `ready` deltaP `3.9194` edge `-0.1074` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
