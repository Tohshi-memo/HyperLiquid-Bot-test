# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T11:37:33.417811+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9164`

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

- `market_context_high->unknown_4h` score `31.9921` n `58` status `ready` deltaP `1.23` edge `2.6728` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `21.2183` n `101` status `ready` deltaP `8.8387` edge `2.3951` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `15.5615` n `101` status `ready` deltaP `9.2237` edge `1.7234` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.5117` n `101` status `ready` deltaP `16.6324` edge `0.3027` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.2057` n `101` status `ready` deltaP `19.8337` edge `0.2607` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4404` n `101` status `ready` deltaP `15.0338` edge `0.1497` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8362` n `101` status `ready` deltaP `16.9799` edge `0.0921` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2752` n `101` status `ready` deltaP `23.8913` edge `0.1348` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7575` n `58` status `ready` deltaP `5.7093` edge `0.0504` maxDD `-0.36`
- `market_context_high->index_1h` score `0.643` n `58` status `ready` deltaP `9.8286` edge `0.0136` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5598` n `101` status `ready` deltaP `14.1489` edge `0.0125` maxDD `-0.8144`
- `news_risk_high->fx_4h` score `0.4048` n `101` status `ready` deltaP `10.7748` edge `0.0255` maxDD `-0.421`
- `market_context_high->fx_1h` score `0.3846` n `58` status `ready` deltaP `9.2247` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.2847` n `101` status `ready` deltaP `14.6598` edge `0.0314` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2818` n `58` status `ready` deltaP `5.699` edge `0.0163` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.2467` n `58` status `ready` deltaP `13.5618` edge `0.0049` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1645` n `101` status `ready` deltaP `3.5913` edge `0.0067` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3173` n `101` status `ready` deltaP `1.3221` edge `0.0053` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.3728` n `58` status `ready` deltaP `2.5809` edge `-0.0026` maxDD `-0.6588`
- `market_context_high->crypto_major_1h` score `-0.4487` n `58` status `ready` deltaP `-2.8391` edge `0.0534` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
