# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T18:22:26.912255+00:00`
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

- `market_context_high->equity_24h` score `2.9652` n `103` status `ready` deltaP `4.5729` edge `0.5226` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3683` n `103` status `ready` deltaP `12.0382` edge `0.1747` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.5092` n `103` status `ready` deltaP `14.4387` edge `0.0968` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0194` n `108` status `ready` deltaP `11.8873` edge `0.04` maxDD `-0.7439`
- `market_context_high->fx_24h` score `1.0096` n `103` status `ready` deltaP `24.1791` edge `0.0549` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.3996` n `103` status `ready` deltaP `9.1002` edge `0.1437` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4865` n `108` status `ready` deltaP `3.4376` edge `0.0194` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4995` n `108` status `ready` deltaP `-2.7611` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.6043` n `108` status `ready` deltaP `0.7485` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6324` n `108` status `ready` deltaP `-3.809` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.7063` n `103` status `ready` deltaP `-2.7957` edge `-0.0114` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8039` n `103` status `ready` deltaP `2.0897` edge `-0.0056` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0304` n `103` status `ready` deltaP `-2.7631` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9536` n `108` status `ready` deltaP `-10.917` edge `-0.0271` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.161` n `103` status `ready` deltaP `0.6068` edge `-0.0504` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.42` n `108` status `ready` deltaP `-7.4739` edge `-0.0522` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-3.292` n `103` status `ready` deltaP `6.9141` edge `-0.071` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.787` n `103` status `ready` deltaP `-12.4461` edge `-0.0883` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.4506` n `103` status `ready` deltaP `-12.1034` edge `-0.125` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0641` n `103` status `ready` deltaP `-14.7111` edge `-0.2348` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
