# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T16:52:24.523484+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4354.3299` n `68` status `ready` deltaP `26.2357` edge `362.728` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.2017` n `40` status `ready` deltaP `57.3611` edge `1.0908` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.9374` n `40` status `ready` deltaP `51.3194` edge `0.5821` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.7746` n `68` status `ready` deltaP `18.203` edge `0.3529` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7557` n `68` status `ready` deltaP `17.4408` edge `0.0681` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0499` n `40` status `ready` deltaP `13.4451` edge `0.1296` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7366` n `68` status `ready` deltaP `10.6904` edge `0.0724` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.7082` n `40` status `ready` deltaP `8.9634` edge `0.1216` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.636` n `40` status `ready` deltaP `20.1524` edge `0.0268` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.6124` n `40` status `ready` deltaP `11.497` edge `0.0393` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.47` n `40` status `ready` deltaP `14.2964` edge `0.0027` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2928` n `68` status `ready` deltaP `14.123` edge `0.026` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1988` n `68` status `ready` deltaP `6.6894` edge `0.0285` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1388` n `68` status `ready` deltaP `6.9303` edge `0.0398` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0349` n `68` status `ready` deltaP `3.0645` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.042` n `68` status `ready` deltaP `3.267` edge `0.0051` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1069` n `68` status `ready` deltaP `3.0645` edge `0.0062` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1221` n `68` status `ready` deltaP `3.5664` edge `0.0326` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3692` n `40` status `ready` deltaP `1.0479` edge `0.0084` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6646` n `68` status `ready` deltaP `2.9676` edge `-0.027` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
