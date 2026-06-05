# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T10:07:23.442065+00:00`
- Price records: `672`
- Market context records: `2959`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.2945` n `123` status `ready` deltaP `12.7329` edge `1.748` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.7308` n `123` status `ready` deltaP `17.2553` edge `0.659` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.9955` n `123` status `ready` deltaP `18.1445` edge `0.7457` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `6.5874` n `123` status `ready` deltaP `26.1475` edge `0.5013` maxDD `-4.1336`
- `market_context_high->index_24h` score `3.2373` n `123` status `ready` deltaP `13.7322` edge `0.2763` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.0779` n `124` status `ready` deltaP `15.9618` edge `0.2005` maxDD `-1.7002`
- `market_context_high->crypto_alt_4h` score `2.5912` n `124` status `ready` deltaP `22.9002` edge `0.5194` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.8588` n `124` status `ready` deltaP `6.5401` edge `0.1333` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6607` n `124` status `ready` deltaP `13.2081` edge `0.0808` maxDD `-2.3986`
- `market_context_high->equity_1h` score `0.2826` n `124` status `ready` deltaP `3.1244` edge `0.053` maxDD `-1.6892`
- `market_context_high->index_1h` score `0.0617` n `124` status `ready` deltaP `5.4617` edge `0.0209` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.2662` n `124` status `ready` deltaP `0.6809` edge `0.004` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.333` n `124` status `ready` deltaP `6.1522` edge `0.0923` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.5131` n `124` status `ready` deltaP `5.114` edge `0.0704` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.5402` n `124` status `ready` deltaP `-1.0817` edge `0.0005` maxDD `-3.3365`
- `market_context_high->unknown_1h` score `-0.5676` n `124` status `ready` deltaP `2.5932` edge `0.0085` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-0.5717` n `124` status `ready` deltaP `12.0231` edge `0.3591` maxDD `-33.6701`
- `market_context_high->commodity_4h` score `-0.7549` n `124` status `ready` deltaP `6.0434` edge `0.0419` maxDD `-8.9839`
- `market_context_high->metal_1h` score `-0.7967` n `124` status `ready` deltaP `-1.695` edge `-0.0021` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.8512` n `124` status `ready` deltaP `-0.3688` edge `0.0094` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
