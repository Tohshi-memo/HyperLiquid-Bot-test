# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T08:52:27.358505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0608` n `12`; crypto_alt avg `0.1601` n `232`; crypto_major avg `0.0563` n `8`; equity avg `-0.0066` n `134`; fx avg `0.0034` n `6`; index avg `0.0031` n `26`; metal avg `-0.0602` n `20`; unknown avg `-0.0306` n `796`
- 1h: commodity avg `-0.0573` n `12`; crypto_alt avg `0.5965` n `232`; crypto_major avg `0.1809` n `8`; equity avg `0.0968` n `134`; fx avg `-0.124` n `6`; index avg `-0.0025` n `26`; metal avg `0.0422` n `20`; unknown avg `1.0735` n `788`
- 4h: commodity avg `-0.171` n `12`; crypto_alt avg `0.1855` n `232`; crypto_major avg `-0.0979` n `8`; equity avg `0.0276` n `134`; fx avg `-0.156` n `6`; index avg `0.0495` n `26`; metal avg `0.1685` n `20`; unknown avg `1.3165` n `758`
- 24h: commodity avg `-0.102` n `12`; crypto_alt avg `0.4377` n `232`; crypto_major avg `-0.5745` n `8`; equity avg `0.4481` n `134`; fx avg `-0.1417` n `6`; index avg `0.0583` n `26`; metal avg `-0.0506` n `20`; unknown avg `383.0512` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
