# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T13:52:28.033039+00:00`
- Price records: `672`
- Market context records: `5046`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10242`

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

- `market_context_high->unknown_1h` score `11.8192` n `101` status `ready` deltaP `3.6491` edge `1.0107` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.6372` n `94` status `ready` deltaP `21.1177` edge `0.6812` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.547` n `94` status `ready` deltaP `17.4883` edge `0.5041` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3129` n `94` status `ready` deltaP `14.3001` edge `0.4868` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.1543` n `94` status `ready` deltaP `12.3281` edge `0.1219` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.7403` n `101` status `ready` deltaP `6.9662` edge `0.107` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.693` n `101` status `ready` deltaP `7.0344` edge `0.0682` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.3864` n `94` status `ready` deltaP `2.7439` edge `0.1694` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3346` n `101` status `ready` deltaP `6.2755` edge `0.0357` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1703` n `101` status `ready` deltaP `5.112` edge `0.09` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0537` n `76` status `ready` deltaP `9.1374` edge `0.0084` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.2266` n `94` status `ready` deltaP `2.7503` edge `0.0389` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3144` n `101` status `ready` deltaP `1.6008` edge `0.015` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4353` n `101` status `ready` deltaP `0.9441` edge `0.012` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-1.0129` n `94` status `ready` deltaP `-4.2586` edge `-0.0026` maxDD `-1.2426`
- `market_context_high->commodity_4h` score `-1.1061` n `94` status `ready` deltaP `4.7386` edge `0.0015` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.4851` n `101` status `ready` deltaP `-8.6915` edge `-0.0048` maxDD `-0.5482`
- `market_context_high->unknown_24h` score `-3.0638` n `76` status `ready` deltaP `27.3209` edge `-0.4032` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.5559` n `76` status `ready` deltaP `6.1495` edge `0.0486` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.6243` n `76` status `ready` deltaP `0.5574` edge `-0.0857` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
