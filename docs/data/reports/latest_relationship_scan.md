# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T10:37:32.710707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9402`

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

- `market_context_high->unknown_4h` score `84.9897` n `135` status `ready` deltaP `5.4619` edge `7.0613` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.4452` n `135` status `ready` deltaP `1.3684` edge `1.3269` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9283` n `130` status `ready` deltaP `26.7725` edge `0.051` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4967` n `135` status `ready` deltaP `11.0557` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4627` n `135` status `ready` deltaP `13.2012` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0834` n `135` status `ready` deltaP `11.0945` edge `0.0114` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3142` n `135` status `ready` deltaP `2.128` edge `0.0097` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.456` n `135` status `ready` deltaP `5.886` edge `0.0306` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5399` n `135` status `ready` deltaP `0.0865` edge `-0.0015` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.6509` n `135` status `ready` deltaP `9.9955` edge `0.004` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.7155` n `130` status `ready` deltaP `7.095` edge `0.0182` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.7657` n `135` status `ready` deltaP `3.6405` edge `0.0338` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-1.1417` n `130` status `ready` deltaP `13.7875` edge `0.0855` maxDD `-7.8047`
- `market_context_high->equity_1h` score `-1.3295` n `135` status `ready` deltaP `2.6391` edge `0.0032` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9195` n `135` status `ready` deltaP `-0.8916` edge `-0.0038` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.468` n `135` status `ready` deltaP `-3.1166` edge `-0.0227` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-2.5807` n `130` status `ready` deltaP `7.0004` edge `0.0347` maxDD `-15.7143`
- `market_context_high->crypto_major_4h` score `-3.5383` n `135` status `ready` deltaP `4.7267` edge `-0.0532` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.6359` n `130` status `ready` deltaP `-1.5491` edge `-0.0983` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7076` n `135` status `ready` deltaP `3.9194` edge `-0.1063` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
