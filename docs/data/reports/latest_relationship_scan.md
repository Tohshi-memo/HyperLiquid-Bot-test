# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T21:51:54.211858+00:00`
- Price records: `491`
- Market context records: `584`
- Flow alert records: `1650`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.6806` n `146` status `ready` deltaP `7.1632` edge `0.3471` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.1027` n `146` status `ready` deltaP `9.5023` edge `0.2286` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0787` n `146` status `ready` deltaP `11.5101` edge `0.0205` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2695` n `146` status `ready` deltaP `2.812` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6321` n `146` status `ready` deltaP `1.3613` edge `0.0357` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.663` n `146` status `ready` deltaP `0.5034` edge `-0.003` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1835` n `146` status `ready` deltaP `-4.4837` edge `-0.0084` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2331` n `146` status `ready` deltaP `-1.774` edge `-0.0099` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3072` n `146` status `ready` deltaP `4.8353` edge `-0.0097` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.9358` n `146` status `ready` deltaP `3.9422` edge `-0.0153` maxDD `-11.4508`
- `market_context_high->index_24h` score `-2.1347` n `146` status `ready` deltaP `-6.0873` edge `0.0622` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-2.1573` n `146` status `ready` deltaP `3.0757` edge `0.0567` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2692` n `146` status `ready` deltaP `0.1003` edge `-0.0375` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.9635` n `146` status `ready` deltaP `11.4967` edge `0.047` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2959` n `146` status `ready` deltaP `-4.5498` edge `-0.0484` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3734` n `146` status `ready` deltaP `-3.7213` edge `-0.0411` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.6194` n `146` status `ready` deltaP `-6.0931` edge `0.0891` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.1433` n `146` status `ready` deltaP `-10.0795` edge `-0.0176` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.4956` n `146` status `ready` deltaP `-4.481` edge `-0.0293` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0628` n `146` status `ready` deltaP `1.1723` edge `-0.2419` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
