# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T09:07:31.661241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `0.0103` n `228`; crypto_major avg `0.0667` n `8`; equity avg `0.1134` n `79`; fx avg `0.0194` n `6`; index avg `0.028` n `23`; metal avg `0.1369` n `18`; unknown avg `-0.0356` n `701`
- 1h: commodity avg `-0.21` n `12`; crypto_alt avg `0.0777` n `228`; crypto_major avg `-0.0808` n `8`; equity avg `0.2407` n `79`; fx avg `0.0342` n `6`; index avg `0.0606` n `23`; metal avg `0.1992` n `18`; unknown avg `-0.0319` n `701`
- 4h: commodity avg `0.0744` n `12`; crypto_alt avg `0.2177` n `228`; crypto_major avg `0.4058` n `8`; equity avg `0.4156` n `79`; fx avg `0.0229` n `6`; index avg `0.0872` n `23`; metal avg `0.3755` n `18`; unknown avg `0.2558` n `661`
- 24h: commodity avg `-0.2565` n `12`; crypto_alt avg `0.1468` n `228`; crypto_major avg `0.3697` n `8`; equity avg `-0.0946` n `79`; fx avg `0.028` n `6`; index avg `0.0449` n `23`; metal avg `0.5131` n `18`; unknown avg `0.1231` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
