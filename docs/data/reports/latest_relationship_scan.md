# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T13:52:26.629292+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2484.8576` n `108` status `ready` deltaP `-7.9282` edge `207.1673` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `83.5859` n `101` status `ready` deltaP `-6.237` edge `7.0357` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `63.4848` n `108` status `ready` deltaP `0.988` edge `5.2971` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.3956` n `49` status `ready` deltaP `45.3976` edge `1.1521` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.0215` n `108` status `ready` deltaP `27.0255` edge `1.014` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.7359` n `108` status `ready` deltaP `42.5347` edge `0.1294` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.6074` n `98` status `ready` deltaP `17.1136` edge `0.4085` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.7815` n `108` status `ready` deltaP `22.177` edge `0.0431` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.2653` n `108` status `ready` deltaP `7.5711` edge `0.1943` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.6617` n `108` status `ready` deltaP `7.0803` edge `0.0955` maxDD `-2.3383`
- `market_context_high->metal_1h` score `0.6295` n `108` status `ready` deltaP `13.8334` edge `0.0175` maxDD `-0.3209`
- `market_context_high->crypto_major_1h` score `0.5918` n `108` status `ready` deltaP `10.2129` edge `0.084` maxDD `-5.2213`
- `news_risk_high->crypto_alt_1h` score `0.4076` n `101` status `ready` deltaP `5.7108` edge `0.0913` maxDD `-3.9659`
- `market_context_high->fx_1h` score `0.1755` n `108` status `ready` deltaP `7.4629` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->metal_24h` score `0.1719` n `108` status `ready` deltaP `14.5254` edge `0.1899` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `0.0674` n `108` status `ready` deltaP `16.8643` edge `0.1672` maxDD `-14.5879`
- `market_context_high->commodity_4h` score `0.0085` n `108` status `ready` deltaP `10.5861` edge `0.0524` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.0001` n `108` status `ready` deltaP `5.8943` edge `-0.0002` maxDD `-0.1285`
- `market_context_high->index_1h` score `-0.3059` n `108` status `ready` deltaP `4.2083` edge `0.0023` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4664` n `108` status `ready` deltaP `-0.2606` edge `0.0143` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
