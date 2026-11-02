# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T11:07:32.355725+00:00`
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

- `news_risk_high->crypto_alt_24h` score `1.8423` n `114` status `ready` deltaP `20.3582` edge `0.687` maxDD `-40.2553`
- `news_risk_high->crypto_alt_4h` score `0.5686` n `136` status `ready` deltaP `7.3709` edge `0.2376` maxDD `-11.4402`
- `news_risk_high->fx_1h` score `-0.5105` n `146` status `ready` deltaP `1.0705` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.547` n `146` status `ready` deltaP `1.2837` edge `0.0441` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8115` n `114` status `ready` deltaP `13.8249` edge `0.1294` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.1263` n `146` status `ready` deltaP `-1.0479` edge `-0.0069` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2836` n `136` status `ready` deltaP `-4.0352` edge `-0.0125` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2899` n `146` status `ready` deltaP `-5.098` edge `-0.0092` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.293` n `114` status `ready` deltaP `-16.5753` edge `-0.0126` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.3007` n `136` status `ready` deltaP `-5.5596` edge `-0.0278` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.39` n `146` status `ready` deltaP `-8.6273` edge `-0.005` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.9697` n `146` status `ready` deltaP `-7.9833` edge `-0.0599` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-3.0982` n `114` status `ready` deltaP `-12.2716` edge `-0.0312` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.3578` n `146` status `ready` deltaP `-8.9041` edge `-0.0479` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0174` n `136` status `ready` deltaP `-13.4057` edge `-0.0181` maxDD `-8.8516`
- `news_risk_high->metal_4h` score `-4.4583` n `136` status `ready` deltaP `-3.3357` edge `-0.0288` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.9538` n `114` status `ready` deltaP `5.1444` edge `0.2119` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.3255` n `136` status `ready` deltaP `-14.7328` edge `-0.1103` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.5317` n `136` status `ready` deltaP `-4.3669` edge `-0.2286` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-10.9076` n `114` status `ready` deltaP `-25.4021` edge `-0.1394` maxDD `-25.6842`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
