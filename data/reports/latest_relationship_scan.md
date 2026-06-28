# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T10:52:26.922135+00:00`
- Price records: `672`
- Market context records: `5032`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10182`

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

- `market_context_high->unknown_1h` score `14.5752` n `94` status `ready` deltaP `2.9239` edge `1.2452` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0857` n `93` status `ready` deltaP `22.0594` edge `0.7123` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4551` n `93` status `ready` deltaP `16.4897` edge `0.5031` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2792` n `93` status `ready` deltaP `14.1785` edge `0.4848` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2526` n `93` status `ready` deltaP `13.3916` edge `0.123` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8135` n `94` status `ready` deltaP `7.7303` edge `0.0736` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.6874` n `94` status `ready` deltaP `5.5548` edge `0.112` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.4002` n `93` status `ready` deltaP `2.6636` edge `0.1717` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3237` n `94` status `ready` deltaP `5.8542` edge `0.0376` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1421` n `94` status `ready` deltaP `4.6885` edge `0.0892` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0314` n `74` status `ready` deltaP `9.7316` edge `0.0073` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1521` n `93` status `ready` deltaP `3.5618` edge `0.0397` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3517` n `94` status `ready` deltaP `1.032` edge `0.014` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5822` n `94` status `ready` deltaP `1.962` edge `0.0125` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.798` n `93` status `ready` deltaP `3.6979` edge `-0.0017` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0181` n `93` status `ready` deltaP `-4.3732` edge `-0.0025` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7622` n `94` status `ready` deltaP `-12.0493` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.7178` n `74` status `ready` deltaP `5.5556` edge `0.0318` maxDD `-32.9721`
- `market_context_high->unknown_24h` score `-4.0214` n `74` status `ready` deltaP `27.0364` edge `-0.4811` maxDD `-1.4072`
- `market_context_high->commodity_24h` score `-4.6001` n `74` status `ready` deltaP `0.9337` edge `-0.0851` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
