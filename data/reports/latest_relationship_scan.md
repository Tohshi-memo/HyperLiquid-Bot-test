# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T12:22:27.751038+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7034`

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

- `market_context_high->unknown_24h` score `1808.7566` n `134` status `ready` deltaP `-2.7908` edge `150.7913` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `222.0485` n `43` status `ready` deltaP `-3.4048` edge `18.5393` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.5445` n `134` status `ready` deltaP `2.8554` edge `2.7063` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `9.2263` n `31` status `ready` deltaP `27.7243` edge `0.6187` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.2422` n `134` status `ready` deltaP `34.0485` edge `0.0615` maxDD `-0.1315`
- `market_context_high->equity_24h` score `2.4724` n `134` status `ready` deltaP `16.3117` edge `0.373` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `2.0989` n `43` status `ready` deltaP `12.4808` edge `0.1334` maxDD `-1.669`
- `news_risk_high->commodity_4h` score `0.6155` n `31` status `ready` deltaP `5.9058` edge `0.0733` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.3719` n `134` status `ready` deltaP `10.7539` edge `0.0139` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3058` n `134` status `ready` deltaP `15.5261` edge `0.0253` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1166` n `134` status `ready` deltaP `4.3324` edge `0.0684` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.0631` n `134` status `ready` deltaP `12.2611` edge `0.0454` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0073` n `134` status `ready` deltaP `7.0158` edge `0.0566` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1127` n `134` status `ready` deltaP `3.4297` edge `-0.0015` maxDD `-0.1986`
- `news_risk_high->metal_4h` score `-0.1467` n `31` status `ready` deltaP `8.93` edge `-0.0022` maxDD `-1.7575`
- `news_risk_high->index_1h` score `-0.178` n `43` status `ready` deltaP `5.5946` edge `-0.0039` maxDD `-0.4972`
- `market_context_high->equity_4h` score `-0.3023` n `134` status `ready` deltaP `1.7815` edge `0.1078` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3607` n `134` status `ready` deltaP `1.3451` edge `0.0124` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.4607` n `43` status `ready` deltaP `-7.5407` edge `0.0214` maxDD `-0.4158`
- `market_context_high->fx_4h` score `-0.5756` n `134` status `ready` deltaP `-1.3878` edge `-0.0047` maxDD `-0.4545`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
