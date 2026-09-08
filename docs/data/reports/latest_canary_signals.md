# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T23:52:29.586816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0375` n `12`; crypto_alt avg `0.0778` n `233`; crypto_major avg `0.0247` n `8`; equity avg `-0.0829` n `134`; fx avg `-0.0075` n `6`; index avg `-0.0321` n `26`; metal avg `-0.0269` n `20`; unknown avg `1.0719` n `797`
- 1h: commodity avg `0.0753` n `12`; crypto_alt avg `-0.0142` n `233`; crypto_major avg `-0.0046` n `8`; equity avg `-0.1763` n `134`; fx avg `-0.0226` n `6`; index avg `-0.0362` n `26`; metal avg `0.0013` n `20`; unknown avg `2.238` n `795`
- 4h: commodity avg `0.1329` n `12`; crypto_alt avg `0.1737` n `233`; crypto_major avg `0.4467` n `8`; equity avg `-0.0634` n `134`; fx avg `-0.0451` n `6`; index avg `-0.051` n `26`; metal avg `-0.0501` n `20`; unknown avg `1.0069` n `725`
- 24h: commodity avg `0.1303` n `12`; crypto_alt avg `-0.3288` n `232`; crypto_major avg `0.0754` n `8`; equity avg `0.2354` n `134`; fx avg `-0.0931` n `6`; index avg `-0.1678` n `26`; metal avg `-0.4301` n `20`; unknown avg `6.8068` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
