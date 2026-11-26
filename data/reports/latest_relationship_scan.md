# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T01:22:37.778859+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3887`

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

- `market_context_high->unknown_1h` score `32137.6814` n `45` status `ready` deltaP `1.5668` edge `2678.1391` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21783.5806` n `45` status `ready` deltaP `1.958` edge `1815.2992` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `902.7264` n `31` status `ready` deltaP `1.7819` edge `75.2329` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `530.6331` n `31` status `ready` deltaP `3.1766` edge `44.2039` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `130.2085` n `31` status `ready` deltaP `6.0764` edge `10.8102` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.7026` n `31` status `ready` deltaP `50.8681` edge `3.3861` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.4949` n `31` status `ready` deltaP `51.7361` edge `3.113` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.5577` n `31` status `ready` deltaP `51.0417` edge `2.7062` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.1415` n `31` status `ready` deltaP `37.416` edge `0.7065` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8859` n `31` status `ready` deltaP `26.6079` edge `0.8168` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.2289` n `31` status `ready` deltaP `37.2247` edge `0.6523` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.2958` n `31` status `ready` deltaP `52.2569` edge `0.2596` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7109` n `31` status `ready` deltaP `17.2354` edge `0.8872` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2726` n `31` status `ready` deltaP `44.8365` edge `0.1533` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5216` n `31` status `ready` deltaP `19.3886` edge `0.1829` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3136` n `31` status `ready` deltaP `36.1576` edge `0.0611` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6135` n `31` status `ready` deltaP `31.0943` edge `0.019` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4057` n `31` status `ready` deltaP `9.8609` edge `0.2888` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3693` n `45` status `ready` deltaP `29.3259` edge `0.0304` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2027` n `31` status `ready` deltaP `12.5555` edge `0.2344` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
