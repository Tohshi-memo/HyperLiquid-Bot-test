# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T18:07:35.011274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0857` n `12`; crypto_alt avg `0.1434` n `228`; crypto_major avg `0.1981` n `8`; equity avg `0.1849` n `86`; fx avg `0.011` n `6`; index avg `0.019` n `23`; metal avg `-0.0283` n `20`; unknown avg `0.0594` n `765`
- 1h: commodity avg `0.1657` n `12`; crypto_alt avg `0.8357` n `228`; crypto_major avg `1.1558` n `8`; equity avg `0.2384` n `86`; fx avg `0.0177` n `6`; index avg `0.0305` n `23`; metal avg `-0.0813` n `20`; unknown avg `0.5062` n `765`
- 4h: commodity avg `0.3108` n `12`; crypto_alt avg `1.2246` n `228`; crypto_major avg `1.4473` n `8`; equity avg `0.2356` n `86`; fx avg `0.0713` n `6`; index avg `0.0506` n `23`; metal avg `0.2059` n `20`; unknown avg `0.6607` n `765`
- 24h: commodity avg `0.4995` n `12`; crypto_alt avg `1.4164` n `228`; crypto_major avg `1.3007` n `8`; equity avg `0.4602` n `86`; fx avg `0.0862` n `6`; index avg `0.5058` n `23`; metal avg `0.8411` n `20`; unknown avg `0.5331` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
