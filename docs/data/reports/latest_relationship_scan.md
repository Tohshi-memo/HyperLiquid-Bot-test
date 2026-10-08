# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T01:07:27.445592+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.5788` n `90` status `ready` deltaP `-4.3224` edge `3.2976` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8653` n `62` status `ready` deltaP `38.1245` edge `0.6716` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9349` n `62` status `ready` deltaP `22.1725` edge `0.5645` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.7659` n `62` status `ready` deltaP `14.1366` edge `0.3962` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.6495` n `62` status `ready` deltaP `33.564` edge `0.1637` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.1238` n `90` status `ready` deltaP `10.0461` edge `0.7591` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.879` n `62` status `ready` deltaP `31.6975` edge `0.0548` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.442` n `62` status `ready` deltaP `10.0251` edge `0.1722` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3605` n `90` status `ready` deltaP `16.189` edge `0.1852` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0514` n `62` status `ready` deltaP `17.1666` edge `0.1163` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9541` n `62` status `ready` deltaP `24.5751` edge `0.014` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4786` n `62` status `ready` deltaP `21.0956` edge `0.0905` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.3584` n `62` status `ready` deltaP `-7.2974` edge `0.2864` maxDD `-5.6309`
- `market_context_high->equity_24h` score `1.2613` n `90` status `ready` deltaP `11.6993` edge `0.07` maxDD `-1.0977`
- `market_context_high->metal_24h` score `1.1355` n `90` status `ready` deltaP `20.0807` edge `0.1602` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0351` n `62` status `ready` deltaP `2.5594` edge `0.1211` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0049` n `90` status `ready` deltaP `21.0637` edge `0.018` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7082` n `90` status `ready` deltaP `11.9461` edge `0.0036` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1222` n `90` status `ready` deltaP `9.9534` edge `0.0382` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.085` n `62` status `ready` deltaP `6.1522` edge `0.0079` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
