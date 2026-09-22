# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T14:22:32.941991+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9930`

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

- `market_context_high->unknown_4h` score `46.7458` n `46` status `ready` deltaP `7.3171` edge `3.8467` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.8588` n `46` status `ready` deltaP `15.7911` edge `2.4819` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2056` n `46` status `ready` deltaP `12.3189` edge `1.2784` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `16.0684` n `46` status `ready` deltaP `14.9306` edge `1.2395` maxDD `0.0`
- `market_context_high->index_24h` score `5.5356` n `46` status `ready` deltaP `20.1314` edge `0.3358` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.2587` n `101` status `ready` deltaP `38.9954` edge `0.2884` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `3.1417` n `101` status `ready` deltaP `-9.5641` edge `1.0114` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `2.2201` n `101` status `ready` deltaP `11.6019` edge `0.2286` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.0387` n `101` status `ready` deltaP `12.938` edge `0.1302` maxDD `-2.058`
- `market_context_high->index_4h` score `1.9202` n `46` status `ready` deltaP `22.7067` edge `0.022` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.5389` n `101` status `ready` deltaP `14.1934` edge `0.1594` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.3194` n `101` status `ready` deltaP `14.2853` edge `0.067` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `1.0672` n `101` status `ready` deltaP `17.3297` edge `0.037` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.9865` n `46` status `ready` deltaP `22.0939` edge `-0.0417` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.9542` n `46` status `ready` deltaP `7.3768` edge `0.061` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8113` n `46` status `ready` deltaP `7.2117` edge `0.0438` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.6646` n `46` status `ready` deltaP `7.2971` edge `0.0662` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.6435` n `46` status `ready` deltaP `10.3554` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5562` n `101` status `ready` deltaP `14.1489` edge `0.0122` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.4421` n `101` status `ready` deltaP `18.2841` edge `0.0192` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
