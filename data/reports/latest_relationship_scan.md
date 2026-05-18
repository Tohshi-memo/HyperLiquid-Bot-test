# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T04:07:15.897176+00:00`
- Price records: `672`
- Market context records: `1081`
- Flow alert records: `5018`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.4817` n `158` status `ready` deltaP `35.2988` edge `1.1845` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.7806` n `158` status `ready` deltaP `12.1222` edge `0.5243` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.4885` n `158` status `ready` deltaP `14.7206` edge `0.4089` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.5921` n `158` status `ready` deltaP `-2.5661` edge `0.5665` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.5306` n `158` status `ready` deltaP `14.8433` edge `0.3094` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5305` n `160` status `ready` deltaP `9.0701` edge `0.1459` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.5053` n `160` status `ready` deltaP `13.5213` edge `0.2039` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.8592` n `160` status `ready` deltaP `7.4848` edge `0.09` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5982` n `172` status `ready` deltaP `7.9863` edge `0.0283` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4627` n `172` status `ready` deltaP `2.8686` edge `0.0572` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.0744` n `172` status `ready` deltaP `6.6251` edge `0.0386` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0053` n `172` status `ready` deltaP `6.7226` edge `0.0012` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1491` n `172` status `ready` deltaP `7.0673` edge `0.0015` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2781` n `172` status `ready` deltaP `2.8652` edge `0.042` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3692` n `160` status `ready` deltaP `7.2104` edge `0.1716` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6917` n `160` status `ready` deltaP `1.4939` edge `0.001` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7033` n `172` status `ready` deltaP `-1.5423` edge `0.0009` maxDD `-3.7959`
- `market_context_high->unknown_4h` score `-1.3494` n `160` status `ready` deltaP `9.4207` edge `-0.0536` maxDD `-6.7322`
- `market_context_high->metal_4h` score `-1.9688` n `160` status `ready` deltaP `4.6037` edge `-0.0877` maxDD `-9.2991`
- `market_context_high->fx_24h` score `-3.1044` n `158` status `ready` deltaP `4.7597` edge `-0.0221` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
