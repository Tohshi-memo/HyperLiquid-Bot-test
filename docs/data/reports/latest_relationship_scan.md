# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T03:07:28.140828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.8397` n `69` status `ready` deltaP `34.1787` edge `0.127` maxDD `-0.4576`
- `market_context_high->equity_24h` score `1.8391` n `69` status `ready` deltaP `16.8251` edge `0.062` maxDD `-0.6726`
- `market_context_high->crypto_major_24h` score `1.5949` n `69` status `ready` deltaP `2.7551` edge `0.2522` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4769` n `69` status `ready` deltaP `21.7014` edge `-0.0216` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.3009` n `100` status `ready` deltaP `14.3415` edge `0.0604` maxDD `-0.808`
- `market_context_high->commodity_1h` score `-0.2459` n `108` status `ready` deltaP `0.3826` edge `0.0105` maxDD `-0.8998`
- `market_context_high->metal_4h` score `-0.3747` n `100` status `ready` deltaP `15.1037` edge `0.0088` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.3753` n `108` status `ready` deltaP `-1.375` edge `-0.0019` maxDD `-0.2968`
- `market_context_high->metal_1h` score `-0.4768` n `108` status `ready` deltaP `4.3857` edge `0.0026` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.7044` n `100` status `ready` deltaP `-3.3537` edge `-0.0071` maxDD `-0.5351`
- `market_context_high->index_1h` score `-1.0` n `108` status `ready` deltaP `-4.4355` edge `-0.0016` maxDD `-0.5064`
- `market_context_high->equity_1h` score `-1.1761` n `108` status `ready` deltaP `-6.2042` edge `-0.0263` maxDD `-3.3165`
- `market_context_high->crypto_major_4h` score `-1.4882` n `100` status `ready` deltaP `1.1524` edge `-0.0109` maxDD `-4.6638`
- `market_context_high->crypto_alt_1h` score `-1.811` n `108` status `ready` deltaP `-5.2284` edge `-0.0151` maxDD `-4.4101`
- `market_context_high->crypto_major_1h` score `-1.8954` n `108` status `ready` deltaP `-5.2284` edge `-0.0227` maxDD `-4.0312`
- `market_context_high->index_4h` score `-1.9519` n `100` status `ready` deltaP `-11.5` edge `-0.0051` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-3.1899` n `69` status `ready` deltaP `-30.7971` edge `-0.0429` maxDD `-1.8596`
- `market_context_high->equity_4h` score `-3.5722` n `100` status `ready` deltaP `-19.4817` edge `-0.1474` maxDD `-8.1221`
- `market_context_high->metal_24h` score `-5.5216` n `69` status `ready` deltaP `-23.196` edge `-0.0543` maxDD `-7.0954`
- `market_context_high->crypto_alt_4h` score `-5.9769` n `100` status `ready` deltaP `-9.9329` edge `-0.0637` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
