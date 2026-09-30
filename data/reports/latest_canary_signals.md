# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T22:07:31.849952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.3058` n `234`; crypto_major avg `-0.1286` n `8`; equity avg `0.0191` n `142`; fx avg `-0.005` n `6`; index avg `0.0177` n `26`; metal avg `0.0064` n `20`; unknown avg `0.6491` n `973`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.3503` n `234`; crypto_major avg `-0.1166` n `8`; equity avg `0.0076` n `142`; fx avg `0.0001` n `6`; index avg `0.0124` n `26`; metal avg `-0.0127` n `20`; unknown avg `0.4837` n `973`
- 4h: commodity avg `-0.1443` n `12`; crypto_alt avg `-0.8665` n `234`; crypto_major avg `-0.0124` n `8`; equity avg `-0.1595` n `142`; fx avg `0.0173` n `6`; index avg `-0.0663` n `26`; metal avg `0.1013` n `20`; unknown avg `1.3529` n `887`
- 24h: commodity avg `0.3499` n `12`; crypto_alt avg `-0.4958` n `234`; crypto_major avg `0.5641` n `8`; equity avg `-0.5378` n `142`; fx avg `0.0833` n `6`; index avg `-0.0787` n `26`; metal avg `-0.2516` n `20`; unknown avg `766.3378` n `812`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
