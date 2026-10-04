# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T14:52:27.371756+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5032`

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

- `market_context_high->unknown_4h` score `101.1778` n `89` status `ready` deltaP `3.0367` edge `8.4424` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `95.9384` n `97` status `ready` deltaP `-0.6096` edge `8.0404` maxDD `-0.9839`
- `news_risk_high->crypto_major_4h` score `10.5579` n `65` status `ready` deltaP `37.5821` edge `0.6496` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `10.4759` n `46` status `ready` deltaP `26.789` edge `0.8217` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `10.2322` n `46` status `ready` deltaP `33.2276` edge `0.6964` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.4889` n `65` status `ready` deltaP `24.2281` edge `0.5559` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.3067` n `65` status `ready` deltaP `24.3598` edge `0.5809` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.1622` n `89` status `ready` deltaP `21.6789` edge `0.356` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.977` n `65` status `ready` deltaP `27.2569` edge `0.1497` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8164` n `65` status `ready` deltaP `25.9123` edge `0.2063` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1172` n `65` status `ready` deltaP `33.8954` edge `0.06` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8896` n `65` status `ready` deltaP `12.561` edge `0.1926` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5878` n `65` status `ready` deltaP `22.2796` edge `0.1087` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.1512` n `97` status `ready` deltaP `15.4794` edge `0.1211` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.1082` n `65` status `ready` deltaP `25.9166` edge `0.0179` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.9476` n `46` status `ready` deltaP `4.2949` edge `0.2328` maxDD `-6.264`
- `market_context_high->crypto_alt_4h` score `1.5281` n `89` status `ready` deltaP `5.034` edge `0.2727` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.4827` n `65` status `ready` deltaP `4.8687` edge `0.143` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4185` n `89` status `ready` deltaP `25.077` edge `0.0267` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3607` n `46` status `ready` deltaP `25.536` edge `0.106` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
