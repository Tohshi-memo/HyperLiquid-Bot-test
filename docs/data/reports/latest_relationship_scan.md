# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T14:52:28.835932+00:00`
- Price records: `672`
- Market context records: `4837`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.7643` n `109` status `ready` deltaP `11.038` edge `1.1152` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.7788` n `100` status `ready` deltaP `22.2378` edge `0.7795` maxDD `-4.0284`
- `market_context_high->unknown_24h` score `3.9045` n `95` status `ready` deltaP `19.9415` edge `0.2531` maxDD `-2.1866`
- `market_context_high->crypto_alt_4h` score `0.6013` n `100` status `ready` deltaP `13.6098` edge `0.1994` maxDD `-14.043`
- `market_context_high->index_4h` score `0.4447` n `100` status `ready` deltaP `7.7439` edge `0.0321` maxDD `-0.7334`
- `market_context_high->equity_1h` score `0.419` n `109` status `ready` deltaP `4.5775` edge `0.066` maxDD `-2.928`
- `market_context_high->equity_4h` score `0.0372` n `100` status `ready` deltaP `9.6768` edge `0.0784` maxDD `-6.3852`
- `market_context_high->commodity_1h` score `-0.0012` n `109` status `ready` deltaP `3.7329` edge `0.0273` maxDD `-1.1869`
- `market_context_high->commodity_4h` score `-0.0026` n `100` status `ready` deltaP `12.5366` edge `0.0333` maxDD `-4.377`
- `market_context_high->fx_4h` score `-0.1383` n `100` status `ready` deltaP `6.4573` edge `0.0074` maxDD `-0.788`
- `market_context_high->crypto_major_4h` score `-0.4192` n `100` status `ready` deltaP `9.9817` edge `0.1634` maxDD `-20.0289`
- `market_context_high->index_1h` score `-0.7993` n `109` status `ready` deltaP `-0.5892` edge `0.0128` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.3079` n `109` status `ready` deltaP `-5.8905` edge `-0.0048` maxDD `-0.8607`
- `market_context_high->crypto_alt_1h` score `-1.3127` n `109` status `ready` deltaP `4.09` edge `-0.0032` maxDD `-12.7225`
- `market_context_high->metal_4h` score `-1.9116` n `100` status `ready` deltaP `9.0976` edge `-0.0414` maxDD `-17.8128`
- `market_context_high->crypto_major_1h` score `-1.9458` n `109` status `ready` deltaP `2.8155` edge `-0.0107` maxDD `-17.9354`
- `market_context_high->fx_24h` score `-1.9675` n `95` status `ready` deltaP `-7.4598` edge `-0.0132` maxDD `-2.749`
- `market_context_high->metal_1h` score `-2.0816` n `109` status `ready` deltaP `0.8309` edge `-0.0621` maxDD `-13.4916`
- `market_context_high->commodity_24h` score `-3.0861` n `95` status `ready` deltaP `13.3845` edge `0.026` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.4779` n `95` status `ready` deltaP `-6.7544` edge `-0.1319` maxDD `-23.7729`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
