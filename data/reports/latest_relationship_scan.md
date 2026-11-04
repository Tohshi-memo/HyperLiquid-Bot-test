# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T21:52:28.516040+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3872`

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

- `news_risk_high->crypto_alt_4h` score `0.2137` n `146` status `ready` deltaP `8.6765` edge `0.2332` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4122` n `146` status `ready` deltaP `3.2298` edge `0.0484` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6724` n `146` status `ready` deltaP `-2.0732` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8376` n `146` status `ready` deltaP `1.9461` edge `-0.0028` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4231` n `146` status `ready` deltaP `-6.8944` edge `-0.0143` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4916` n `146` status `ready` deltaP `-8.2317` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8971` n `146` status `ready` deltaP `-0.378` edge `-0.0106` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1766` n `146` status `ready` deltaP `-7.8788` edge `0.0078` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3667` n `146` status `ready` deltaP `-7.1455` edge `0.0284` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4574` n `146` status `ready` deltaP `-18.8368` edge `-0.0186` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.615` n `146` status `ready` deltaP `-6.4863` edge `-0.0244` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1721` n `146` status `ready` deltaP `-6.6586` edge `-0.0474` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.243` n `146` status `ready` deltaP `-10.1884` edge `0.0331` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-4.2205` n `146` status `ready` deltaP `1.0167` edge `-0.0003` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.9421` n `146` status `ready` deltaP `-6.2333` edge `-0.0498` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0463` n `146` status `ready` deltaP `-11.1824` edge `-0.1107` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.8833` n `146` status `ready` deltaP `12.7459` edge `0.3474` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9521` n `146` status `ready` deltaP `0.0793` edge `-0.0771` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.7379` n `146` status `ready` deltaP `11.8809` edge `0.393` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-11.7437` n `146` status `ready` deltaP `-20.6807` edge `-0.0147` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
