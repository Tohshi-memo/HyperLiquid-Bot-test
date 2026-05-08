# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T01:07:17.999429+00:00`
- Price records: `600`
- Market context records: `703`
- Flow alert records: `1987`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `10.7358` n `146` status `ready` deltaP `26.1062` edge `0.754` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5599` n `146` status `ready` deltaP `8.2437` edge `0.4965` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2117` n `149` status `ready` deltaP `7.2009` edge `0.012` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2783` n `149` status `ready` deltaP `2.9884` edge `0.0022` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5072` n `149` status `ready` deltaP `2.2028` edge `0.0405` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6181` n `149` status `ready` deltaP `0.4365` edge `0.0032` maxDD `-2.8282`
- `market_context_high->index_24h` score `-1.1543` n `146` status `ready` deltaP `-3.2822` edge `0.1252` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.1576` n `149` status `ready` deltaP `16.0177` edge `0.1154` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1686` n `149` status `ready` deltaP `-4.0269` edge `-0.0102` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1812` n `149` status `ready` deltaP `-1.755` edge `-0.0057` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.4062` n `149` status `ready` deltaP `4.3624` edge `-0.0148` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.6446` n `149` status `ready` deltaP `5.8725` edge `-0.0039` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.6657` n `149` status `ready` deltaP `2.3791` edge `-0.0024` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9859` n `149` status `ready` deltaP `4.0176` edge `0.0647` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.2863` n `146` status `ready` deltaP `-5.2575` edge `0.105` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.56` n `149` status `ready` deltaP `-0.7244` edge `0.0067` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3418` n `149` status `ready` deltaP `-5.0335` edge `-0.049` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8708` n `149` status `ready` deltaP `-6.6709` edge `0.072` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.3012` n `149` status `ready` deltaP `2.9983` edge `-0.1906` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0165` n `146` status `ready` deltaP `-11.6329` edge `-0.0484` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
