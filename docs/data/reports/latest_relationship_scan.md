# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T17:07:30.279136+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5042`

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

- `market_context_high->unknown_1h` score `96.248` n `97` status `ready` deltaP `-0.6096` edge `8.0662` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.2276` n `97` status `ready` deltaP `2.2991` edge `6.5348` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.6375` n `65` status `ready` deltaP `37.887` edge `0.6542` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `9.5756` n `46` status `ready` deltaP `31.6651` edge `0.6521` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `9.5613` n `46` status `ready` deltaP `25.2265` edge `0.7559` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `7.6943` n `65` status `ready` deltaP `22.6656` edge `0.5001` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.493` n `65` status `ready` deltaP `24.6646` edge `0.5944` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `4.9709` n `97` status `ready` deltaP `21.868` edge `0.3388` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8717` n `65` status `ready` deltaP `26.7361` edge `0.1444` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.849` n `65` status `ready` deltaP `26.0647` edge `0.208` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.233` n `65` status `ready` deltaP `35.2674` edge `0.0605` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8681` n `65` status `ready` deltaP `12.4113` edge `0.1918` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6768` n `65` status `ready` deltaP `23.3467` edge `0.109` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1824` n `65` status `ready` deltaP `26.8148` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1296` n `97` status `ready` deltaP `15.3297` edge `0.1203` maxDD `-2.2692`
- `market_context_high->crypto_alt_4h` score `1.6062` n `97` status `ready` deltaP `6.5203` edge `0.2693` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.5894` n `65` status `ready` deltaP `5.4675` edge `0.1479` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.447` n `97` status `ready` deltaP `25.5831` edge `0.0257` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.363` n `46` status `ready` deltaP `25.536` edge `0.1063` maxDD `-1.8102`
- `market_context_high->equity_24h` score `1.153` n `46` status `ready` deltaP `2.7324` edge `0.177` maxDD `-6.264`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
