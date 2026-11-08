# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T23:22:30.569564+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6535`

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

- `market_context_high->unknown_4h` score `27.7387` n `46` status `ready` deltaP `-1.8425` edge `2.3686` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.6476` n `37` status `ready` deltaP `11.2472` edge `0.7418` maxDD `-31.3588`
- `market_context_high->fx_4h` score `1.1975` n `46` status `ready` deltaP `16.6358` edge `0.0299` maxDD `-0.281`
- `market_context_high->index_24h` score `1.1796` n `37` status `ready` deltaP `14.8649` edge `0.1152` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8942` n `37` status `ready` deltaP `10.9422` edge `0.0104` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.349` n `46` status `ready` deltaP `13.693` edge `0.0213` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `0.2254` n `58` status `ready` deltaP `10.35` edge `0.0145` maxDD `-1.7019`
- `market_context_high->equity_1h` score `0.2006` n `58` status `ready` deltaP `3.0714` edge `0.1204` maxDD `-5.2128`
- `market_context_high->commodity_4h` score `0.1772` n `46` status `ready` deltaP `4.2351` edge `0.0399` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0764` n `58` status `ready` deltaP `2.1732` edge `0.0085` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `-0.1638` n `37` status `ready` deltaP `2.2195` edge `0.0837` maxDD `-6.5601`
- `market_context_high->index_1h` score `-0.3984` n `58` status `ready` deltaP `-1.9513` edge `0.0201` maxDD `-0.6537`
- `market_context_high->fx_1h` score `-0.4125` n `58` status `ready` deltaP `-3.5154` edge `0.0063` maxDD `-0.1928`
- `market_context_high->metal_4h` score `-1.4835` n `46` status `ready` deltaP `-5.1896` edge `-0.0365` maxDD `-1.2025`
- `market_context_high->metal_24h` score `-1.5367` n `37` status `ready` deltaP `8.0472` edge `-0.1264` maxDD `-1.4245`
- `market_context_high->crypto_alt_1h` score `-1.6547` n `58` status `ready` deltaP `2.2403` edge `-0.0378` maxDD `-10.1421`
- `market_context_high->crypto_major_1h` score `-2.3027` n `58` status `ready` deltaP `-0.1549` edge `-0.0843` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-3.3169` n `46` status `ready` deltaP `12.8513` edge `-0.0216` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-5.5487` n `46` status `ready` deltaP `8.192` edge `-0.2279` maxDD `-19.462`
- `market_context_high->crypto_major_24h` score `-8.3509` n `37` status `ready` deltaP `-9.0841` edge `-0.1593` maxDD `-32.0839`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
