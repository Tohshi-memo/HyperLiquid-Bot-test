# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T11:22:31.346241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `1.4503` n `115` status `ready` deltaP `19.914` edge `0.671` maxDD `-42.426`
- `news_risk_high->crypto_alt_4h` score `0.4815` n `137` status `ready` deltaP `7.0778` edge `0.2369` maxDD `-11.7882`
- `news_risk_high->fx_1h` score `-0.5105` n `146` status `ready` deltaP `1.0705` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5431` n `146` status `ready` deltaP `1.2837` edge `0.0446` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.7964` n `115` status `ready` deltaP `13.9946` edge `0.1302` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.1239` n `146` status `ready` deltaP `-1.0479` edge `-0.0067` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2614` n `137` status `ready` deltaP `-3.6541` edge `-0.0122` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2891` n `146` status `ready` deltaP `-5.098` edge `-0.0091` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.2641` n `115` status `ready` deltaP `-16.2455` edge `-0.0111` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2754` n `137` status `ready` deltaP `-5.1785` edge `-0.0271` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3745` n `146` status `ready` deltaP `-8.4776` edge `-0.0047` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.9502` n `146` status `ready` deltaP `-7.8336` edge `-0.0584` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-3.0478` n `115` status `ready` deltaP `-11.7377` edge `-0.0283` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.3386` n `146` status `ready` deltaP `-8.7544` edge `-0.0473` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0627` n `137` status `ready` deltaP `-13.4948` edge `-0.0188` maxDD `-9.0501`
- `news_risk_high->metal_4h` score `-4.4678` n `137` status `ready` deltaP `-3.4839` edge `-0.0286` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.8502` n `115` status `ready` deltaP `5.4877` edge `0.2229` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.3176` n `137` status `ready` deltaP `-14.8434` edge `-0.1089` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.474` n `137` status `ready` deltaP `-3.9912` edge `-0.2237` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.0294` n `115` status `ready` deltaP `-25.5013` edge `-0.1417` maxDD `-26.2594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
