# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T23:37:26.199714+00:00`
- Price records: `672`
- Market context records: `6136`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.8839` n `30` status `ready` deltaP `39.8611` edge `0.656` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7481` n `30` status `ready` deltaP `68.5764` edge `0.1885` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3335` n `32` status `ready` deltaP `45.1982` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4171` n `32` status `ready` deltaP `29.0419` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4586` n `195` status `ready` deltaP `0.8046` edge `0.217` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.1778` n `32` status `ready` deltaP `12.9304` edge `0.1115` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5886` n `32` status `ready` deltaP `8.1774` edge `0.0671` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.4043` n `195` status `ready` deltaP `3.9024` edge `0.0994` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1606` n `30` status `ready` deltaP `8.0208` edge `0.0131` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2591` n `195` status `ready` deltaP `1.7342` edge `-0.0002` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3883` n `195` status `ready` deltaP `-2.7643` edge `0.2393` maxDD `-11.925`
- `news_risk_high->crypto_major_24h` score `-0.4953` n `30` status `ready` deltaP `10.2083` edge `-0.0536` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `-0.5791` n `30` status `ready` deltaP `14.0973` edge `-0.1217` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6391` n `195` status `ready` deltaP `3.5421` edge `0.0132` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7727` n `195` status `ready` deltaP `-2.2885` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8034` n `32` status `ready` deltaP `-3.4431` edge `-0.0303` maxDD `-1.6464`
- `market_context_high->equity_1h` score `-0.839` n `195` status `ready` deltaP `-1.008` edge `0.0107` maxDD `-4.2573`
- `market_context_high->metal_1h` score `-0.8703` n `195` status `ready` deltaP `1.9415` edge `-0.0056` maxDD `-2.0564`
- `market_context_high->metal_24h` score `-0.8818` n `195` status `ready` deltaP `15.6891` edge `0.0392` maxDD `-11.8809`
- `market_context_high->crypto_alt_1h` score `-0.9873` n `195` status `ready` deltaP `3.1614` edge `0.0276` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
