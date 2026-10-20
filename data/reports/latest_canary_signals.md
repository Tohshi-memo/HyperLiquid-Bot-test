# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T11:07:27.551107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `0.1673` n `237`; crypto_major avg `0.1337` n `8`; equity avg `-0.119` n `151`; fx avg `0.0058` n `6`; index avg `-0.0174` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.092` n `1196`
- 1h: commodity avg `0.0668` n `13`; crypto_alt avg `0.1109` n `237`; crypto_major avg `0.0184` n `8`; equity avg `-0.308` n `151`; fx avg `-0.0127` n `6`; index avg `-0.0455` n `26`; metal avg `0.0235` n `20`; unknown avg `3.6909` n `1196`
- 4h: commodity avg `0.2319` n `13`; crypto_alt avg `-0.5032` n `237`; crypto_major avg `-0.3258` n `8`; equity avg `-0.8346` n `151`; fx avg `-0.0028` n `6`; index avg `-0.1525` n `26`; metal avg `-0.1389` n `20`; unknown avg `1.2149` n `1180`
- 24h: commodity avg `0.1688` n `13`; crypto_alt avg `0.37` n `237`; crypto_major avg `-0.4043` n `8`; equity avg `-2.1079` n `151`; fx avg `-0.0166` n `6`; index avg `-0.3079` n `26`; metal avg `-0.3398` n `20`; unknown avg `0.6025` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
