# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T06:22:24.725055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.0927` n `232`; crypto_major avg `-0.2059` n `8`; equity avg `-0.0995` n `130`; fx avg `-0.0162` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0565` n `20`; unknown avg `-0.0199` n `792`
- 1h: commodity avg `-0.024` n `12`; crypto_alt avg `0.1793` n `232`; crypto_major avg `0.1089` n `8`; equity avg `0.2813` n `130`; fx avg `-0.0083` n `6`; index avg `0.0622` n `26`; metal avg `0.0625` n `20`; unknown avg `0.1341` n `772`
- 4h: commodity avg `0.0485` n `12`; crypto_alt avg `0.7581` n `232`; crypto_major avg `0.496` n `8`; equity avg `0.2959` n `130`; fx avg `0.0176` n `6`; index avg `0.0484` n `26`; metal avg `-0.0562` n `20`; unknown avg `0.1855` n `772`
- 24h: commodity avg `0.3325` n `12`; crypto_alt avg `1.5986` n `232`; crypto_major avg `1.3922` n `8`; equity avg `0.5606` n `130`; fx avg `0.0526` n `6`; index avg `0.0178` n `26`; metal avg `-0.1302` n `20`; unknown avg `0.2198` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
