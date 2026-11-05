# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T01:52:30.764052+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.4269` n `146` status `ready` deltaP `6.5424` edge `0.1653` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5666` n `146` status `ready` deltaP `2.3316` edge `0.0346` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7253` n `146` status `ready` deltaP `-2.9714` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7921` n `146` status `ready` deltaP `2.3952` edge `-0.002` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4792` n `146` status `ready` deltaP `-7.6429` edge `-0.0165` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5627` n `146` status `ready` deltaP `-9.2988` edge `-0.0132` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9453` n `146` status `ready` deltaP `-1.1402` edge `-0.0117` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1119` n `146` status `ready` deltaP `-7.28` edge `0.0092` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.439` n `146` status `ready` deltaP `-18.6638` edge `-0.0174` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5768` n `146` status `ready` deltaP `-6.0372` edge `-0.0225` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.5914` n `146` status `ready` deltaP `-9.7407` edge `0.0169` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.202` n `146` status `ready` deltaP `-10.036` edge `0.0355` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4012` n `146` status `ready` deltaP `-7.7065` edge `-0.0595` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-5.0852` n `146` status `ready` deltaP `-1.7514` edge `-0.0539` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.1676` n `146` status `ready` deltaP `-8.0626` edge `-0.0564` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.8038` n `146` status `ready` deltaP `-13.3165` edge `-0.1596` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.199` n `146` status `ready` deltaP `-0.6828` edge `-0.0926` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.2037` n `146` status `ready` deltaP `-20.6807` edge `0.0303` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-11.9203` n `146` status `ready` deltaP `9.9778` edge `0.1047` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-12.5534` n `146` status `ready` deltaP `11.7079` edge `0.3262` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
