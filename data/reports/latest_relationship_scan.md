# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T18:37:29.818378+00:00`
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

- `market_context_high->equity_24h` score `2.9604` n `103` status `ready` deltaP `4.5729` edge `0.5222` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3719` n `103` status `ready` deltaP `12.0382` edge `0.175` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.5092` n `103` status `ready` deltaP `14.4387` edge `0.0968` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.999` n `103` status `ready` deltaP `24.0055` edge `0.0547` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.9798` n `109` status `ready` deltaP `11.4679` edge `0.0395` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.4011` n `103` status `ready` deltaP `9.1002` edge `0.1439` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5169` n `109` status `ready` deltaP `-3.0956` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.5436` n `109` status `ready` deltaP `2.843` edge `0.0186` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.5664` n `109` status `ready` deltaP `1.2072` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6169` n `109` status `ready` deltaP `-3.5255` edge `-0.006` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.7063` n `103` status `ready` deltaP `-2.7957` edge `-0.0114` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8039` n `103` status `ready` deltaP `2.0897` edge `-0.0056` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0304` n `103` status `ready` deltaP `-2.7631` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9917` n `109` status `ready` deltaP `-11.3333` edge `-0.0275` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.178` n `103` status `ready` deltaP `0.4544` edge `-0.0508` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.4749` n `109` status `ready` deltaP `-7.8902` edge `-0.054` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-3.3395` n `103` status `ready` deltaP `6.7405` edge `-0.0738` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.817` n `103` status `ready` deltaP `-12.4461` edge `-0.0908` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.4724` n `103` status `ready` deltaP `-12.2558` edge `-0.1258` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0617` n `103` status `ready` deltaP `-14.7111` edge `-0.2346` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
