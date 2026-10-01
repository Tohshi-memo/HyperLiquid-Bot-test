# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T18:07:35.201838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2476` n `13`; crypto_alt avg `-0.3298` n `234`; crypto_major avg `-0.3251` n `8`; equity avg `-0.5076` n `142`; fx avg `0.0445` n `6`; index avg `-0.0992` n `26`; metal avg `-0.1066` n `20`; unknown avg `0.7963` n `973`
- 1h: commodity avg `0.2083` n `13`; crypto_alt avg `0.7234` n `234`; crypto_major avg `0.355` n `8`; equity avg `0.3207` n `142`; fx avg `0.037` n `6`; index avg `0.0584` n `26`; metal avg `-0.029` n `20`; unknown avg `-0.376` n `973`
- 4h: commodity avg `0.2168` n `13`; crypto_alt avg `0.8268` n `234`; crypto_major avg `0.2573` n `8`; equity avg `1.013` n `142`; fx avg `-0.1352` n `6`; index avg `0.1334` n `26`; metal avg `-0.0309` n `20`; unknown avg `0.5811` n `909`
- 24h: commodity avg `0.0301` n `13`; crypto_alt avg `-0.2579` n `234`; crypto_major avg `0.1004` n `8`; equity avg `0.6484` n `142`; fx avg `-0.0923` n `6`; index avg `0.058` n `26`; metal avg `-0.0625` n `20`; unknown avg `-0.2036` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
