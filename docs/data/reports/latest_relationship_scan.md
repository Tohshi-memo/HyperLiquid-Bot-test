# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T23:37:33.520039+00:00`
- Price records: `672`
- Market context records: `5089`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10352`

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

- `market_context_high->unknown_24h` score `16.7542` n `76` status `ready` deltaP `27.3209` edge `1.2483` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `9.4856` n `109` status `ready` deltaP `2.4625` edge `0.8382` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.8841` n `97` status `ready` deltaP `22.2089` edge `0.6945` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.2892` n `97` status `ready` deltaP `14.9767` edge `0.4765` maxDD `-7.513`
- `market_context_high->crypto_major_4h` score `4.3525` n `97` status `ready` deltaP `14.4031` edge `0.4759` maxDD `-12.4039`
- `market_context_high->equity_4h` score `2.5267` n `97` status `ready` deltaP `14.4912` edge `0.2271` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.207` n `109` status `ready` deltaP `11.1685` edge `0.0793` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.5374` n `97` status `ready` deltaP `10.6644` edge `0.0498` maxDD `-1.0893`
- `market_context_high->crypto_alt_1h` score `0.5343` n `109` status `ready` deltaP `5.3068` edge `0.1053` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.4283` n `109` status `ready` deltaP `7.1994` edge `0.0175` maxDD `-0.3843`
- `market_context_high->metal_1h` score `0.3678` n `109` status `ready` deltaP `9.8555` edge `0.0311` maxDD `-1.3057`
- `market_context_high->crypto_major_1h` score `0.3054` n `109` status `ready` deltaP `6.6156` edge `0.1196` maxDD `-6.9639`
- `market_context_high->metal_4h` score `0.1425` n `97` status `ready` deltaP `6.7655` edge `0.0845` maxDD `-2.24`
- `market_context_high->commodity_1h` score `-0.9119` n `109` status `ready` deltaP `-0.6661` edge `0.0005` maxDD `-1.7641`
- `market_context_high->commodity_4h` score `-0.979` n `97` status `ready` deltaP `6.8377` edge `-0.0041` maxDD `-4.8457`
- `market_context_high->fx_24h` score `-1.3417` n `76` status `ready` deltaP `-2.3118` edge `-0.0077` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.4444` n `76` status `ready` deltaP `9.6491` edge `0.0467` maxDD `-15.0303`
- `market_context_high->fx_1h` score `-1.8018` n `109` status `ready` deltaP `-12.1436` edge `-0.0051` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-2.2223` n `97` status `ready` deltaP `-10.2149` edge `-0.0108` maxDD `-1.8367`
- `market_context_high->metal_24h` score `-4.517` n `76` status `ready` deltaP `-5.7475` edge `0.0047` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
