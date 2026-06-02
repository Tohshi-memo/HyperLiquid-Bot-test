# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T13:22:26.567699+00:00`
- Price records: `672`
- Market context records: `2666`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->crypto_alt_24h` score `9.0995` n `112` status `ready` deltaP `15.9226` edge `1.0015` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.4343` n `112` status `ready` deltaP `17.1875` edge `0.6211` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.5776` n `121` status `ready` deltaP `23.1279` edge `0.4924` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `2.6376` n `121` status `ready` deltaP `11.2049` edge `0.3261` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.1859` n `121` status `ready` deltaP `6.7199` edge `0.159` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7389` n `132` status `ready` deltaP `8.7915` edge `0.1217` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.0643` n `132` status `ready` deltaP `6.0697` edge `0.0872` maxDD `-4.2199`
- `market_context_high->index_24h` score `-0.0544` n `112` status `ready` deltaP `7.9117` edge `0.0408` maxDD `-2.5127`
- `market_context_high->fx_24h` score `-0.099` n `112` status `ready` deltaP `11.2103` edge `0.0042` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-0.1602` n `132` status `ready` deltaP `2.6084` edge `0.0272` maxDD `-1.9684`
- `market_context_high->index_4h` score `-0.3234` n `121` status `ready` deltaP `6.8245` edge `0.0117` maxDD `-2.3986`
- `market_context_high->commodity_1h` score `-0.3705` n `132` status `ready` deltaP `3.3206` edge `0.0057` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.3876` n `132` status `ready` deltaP `1.7102` edge `0.0057` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.4598` n `121` status `ready` deltaP `2.0182` edge `0.0136` maxDD `-0.5631`
- `market_context_high->fx_1h` score `-0.5309` n `132` status `ready` deltaP `-0.5806` edge `0.004` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6121` n `132` status `ready` deltaP `-1.0661` edge `-0.001` maxDD `-1.9622`
- `market_context_high->commodity_24h` score `-0.6938` n `112` status `ready` deltaP `7.4157` edge `0.1807` maxDD `-13.1939`
- `market_context_high->metal_4h` score `-0.8263` n `121` status `ready` deltaP `1.5281` edge `0.0105` maxDD `-3.1635`
- `market_context_high->commodity_4h` score `-1.3122` n `121` status `ready` deltaP `2.6519` edge `0.0061` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.3311` n `132` status `ready` deltaP `-5.185` edge `0.0075` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
