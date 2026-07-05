# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T09:52:25.139876+00:00`
- Price records: `672`
- Market context records: `5759`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8666`

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

- `market_context_high->equity_24h` score `0.7614` n `226` status `ready` deltaP `15.181` edge `0.5043` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1559` n `284` status `ready` deltaP `7.403` edge `0.1275` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2069` n `295` status `ready` deltaP `3.0706` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4327` n `295` status `ready` deltaP `1.9126` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.652` n `295` status `ready` deltaP `2.9641` edge `0.0266` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6585` n `295` status `ready` deltaP `-0.1918` edge `0.0037` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7751` n `295` status `ready` deltaP `-1.9436` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8189` n `295` status `ready` deltaP `3.4096` edge `0.0332` maxDD `-5.6002`
- `market_context_high->crypto_alt_1h` score `-0.8898` n `295` status `ready` deltaP `2.0623` edge `0.0325` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-0.9207` n `226` status `ready` deltaP `14.5956` edge `0.043` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1459` n `284` status `ready` deltaP `1.6232` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2283` n `284` status `ready` deltaP `3.1583` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6279` n `284` status `ready` deltaP `-7.5317` edge `-0.0493` maxDD `-11.6581`
- `market_context_high->crypto_major_4h` score `-2.6772` n `284` status `ready` deltaP `7.9247` edge `0.1546` maxDD `-25.1094`
- `market_context_high->index_24h` score `-2.9488` n `226` status `ready` deltaP `1.0816` edge `0.0292` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7493` n `284` status `ready` deltaP `-2.5786` edge `-0.0277` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.7889` n `284` status `ready` deltaP `6.6107` edge `0.1092` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.7778` n `226` status `ready` deltaP `6.6065` edge `0.0035` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.744` n `226` status `ready` deltaP `-9.8113` edge `-0.2501` maxDD `-30.8514`
- `market_context_high->commodity_24h` score `-11.7047` n `226` status `ready` deltaP `-12.7197` edge `-0.0846` maxDD `-43.8127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
