# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T19:07:29.757971+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11590`

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

- `market_context_high->equity_24h` score `2.9568` n `103` status `ready` deltaP `4.5729` edge `0.5219` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3791` n `103` status `ready` deltaP `12.0382` edge `0.1756` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.5068` n `103` status `ready` deltaP `14.4387` edge `0.0966` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0066` n `111` status `ready` deltaP `11.8628` edge `0.0391` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.9778` n `103` status `ready` deltaP `23.6583` edge `0.0543` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.405` n `103` status `ready` deltaP `9.1002` edge `0.1444` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5034` n `111` status `ready` deltaP `1.9502` edge `-0.0054` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.519` n `111` status `ready` deltaP `-3.1369` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.63` n `111` status `ready` deltaP `-3.733` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.6446` n `111` status `ready` deltaP `1.8356` edge `0.0169` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.7229` n `103` status `ready` deltaP `-3.1006` edge `-0.0115` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8161` n `103` status `ready` deltaP `1.9373` edge `-0.0056` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0383` n `103` status `ready` deltaP `-2.9156` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0541` n `111` status `ready` deltaP `-11.9936` edge `-0.0283` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2132` n `103` status `ready` deltaP `0.1495` edge `-0.0517` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.6112` n `111` status `ready` deltaP `-8.4008` edge `-0.0566` maxDD `-5.0665`
- `market_context_high->crypto_major_24h` score `-3.4157` n `103` status `ready` deltaP `6.5669` edge `-0.079` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.877` n `103` status `ready` deltaP `-12.4461` edge `-0.0958` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.5196` n `103` status `ready` deltaP `-12.5607` edge `-0.1277` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0459` n `103` status `ready` deltaP `-14.5587` edge `-0.2343` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
