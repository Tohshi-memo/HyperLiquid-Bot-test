# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T23:37:21.500999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `-0.0808` n `231`; crypto_major avg `-0.0667` n `8`; equity avg `-0.0003` n `127`; fx avg `-0.0009` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.0189` n `792`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0222` n `231`; crypto_major avg `0.1551` n `8`; equity avg `-0.1136` n `127`; fx avg `0.0007` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0509` n `20`; unknown avg `-0.0953` n `792`
- 4h: commodity avg `-0.08` n `12`; crypto_alt avg `0.216` n `231`; crypto_major avg `0.1124` n `8`; equity avg `-0.2411` n `127`; fx avg `0.0027` n `6`; index avg `0.012` n `26`; metal avg `-0.0236` n `20`; unknown avg `-0.0968` n `792`
- 24h: commodity avg `0.3463` n `12`; crypto_alt avg `1.1225` n `231`; crypto_major avg `2.4511` n `8`; equity avg `-0.4348` n `127`; fx avg `-0.0295` n `6`; index avg `-0.1236` n `26`; metal avg `0.0326` n `20`; unknown avg `0.9528` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
