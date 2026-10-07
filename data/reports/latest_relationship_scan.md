# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T16:37:32.807720+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8742`

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

- `market_context_high->unknown_4h` score `37.4193` n `90` status `ready` deltaP `-5.5707` edge `3.2093` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.782` n `62` status `ready` deltaP `37.2932` edge `0.6702` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5237` n `62` status `ready` deltaP `24.2378` edge `0.5998` maxDD `-6.4195`
- `news_risk_high->index_24h` score `4.1018` n `62` status `ready` deltaP `29.4627` edge `0.1454` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.9436` n `62` status `ready` deltaP `9.4929` edge `0.2753` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.073` n `62` status `ready` deltaP `33.763` edge `0.0572` maxDD `-0.4296`
- `market_context_high->crypto_major_24h` score `2.5206` n `90` status `ready` deltaP `7.7007` edge `0.5692` maxDD `-16.7906`
- `news_risk_high->crypto_major_1h` score `2.3808` n `62` status `ready` deltaP `9.7257` edge `0.1691` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.3259` n `62` status `ready` deltaP `19.5488` edge `0.1233` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.2772` n `90` status `ready` deltaP `15.3577` edge `0.1838` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0547` n `62` status `ready` deltaP `25.7727` edge `0.0144` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4489` n `62` status `ready` deltaP `20.4055` edge `0.0913` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2342` n `62` status `ready` deltaP `3.757` edge `0.1297` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.852` n `90` status `ready` deltaP `19.452` edge `0.016` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.7928` n `90` status `ready` deltaP `18.9659` edge `0.1237` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7645` n `90` status `ready` deltaP `12.6946` edge `0.0033` maxDD `-0.271`
- `news_risk_high->unknown_4h` score `0.1989` n `62` status `ready` deltaP `-8.5457` edge `0.1981` maxDD `-5.6309`
- `news_risk_high->metal_1h` score `0.1209` n `62` status `ready` deltaP `6.6013` edge `0.0079` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.0825` n `90` status `ready` deltaP `9.654` edge `0.0351` maxDD `-3.7778`
- `market_context_high->crypto_alt_4h` score `0.0141` n `90` status `ready` deltaP `-4.7945` edge `0.2055` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
