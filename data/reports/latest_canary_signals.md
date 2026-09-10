# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T08:22:31.318860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.1043` n `233`; crypto_major avg `0.0277` n `8`; equity avg `-0.039` n `134`; fx avg `0.0155` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0077` n `20`; unknown avg `-0.0046` n `797`
- 1h: commodity avg `0.0804` n `12`; crypto_alt avg `-0.1717` n `233`; crypto_major avg `0.0507` n `8`; equity avg `-0.1667` n `134`; fx avg `0.0211` n `6`; index avg `-0.033` n `26`; metal avg `-0.0411` n `20`; unknown avg `1.8292` n `795`
- 4h: commodity avg `0.0526` n `12`; crypto_alt avg `-0.5748` n `233`; crypto_major avg `-0.5026` n `8`; equity avg `-0.0997` n `134`; fx avg `0.0601` n `6`; index avg `0.0221` n `26`; metal avg `-0.1111` n `20`; unknown avg `0.6449` n `765`
- 24h: commodity avg `-0.0158` n `12`; crypto_alt avg `-4.7857` n `233`; crypto_major avg `-3.2675` n `8`; equity avg `-1.4463` n `134`; fx avg `0.0918` n `6`; index avg `-0.152` n `26`; metal avg `0.1325` n `20`; unknown avg `0.5434` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
