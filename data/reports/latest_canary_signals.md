# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T12:07:29.615916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1009` n `13`; crypto_alt avg `-0.1793` n `239`; crypto_major avg `-0.2145` n `8`; equity avg `-0.2215` n `164`; fx avg `0.0015` n `6`; index avg `-0.0242` n `27`; metal avg `-0.0451` n `20`; unknown avg `9.1458` n `1254`
- 1h: commodity avg `-0.0191` n `13`; crypto_alt avg `0.1843` n `239`; crypto_major avg `0.2557` n `8`; equity avg `0.1061` n `164`; fx avg `-0.0466` n `6`; index avg `0.0107` n `27`; metal avg `-0.0873` n `20`; unknown avg `10.5036` n `1256`
- 4h: commodity avg `0.0585` n `13`; crypto_alt avg `0.301` n `239`; crypto_major avg `0.2053` n `8`; equity avg `0.689` n `164`; fx avg `0.0168` n `6`; index avg `0.1388` n `27`; metal avg `-0.0934` n `20`; unknown avg `299.9363` n `1252`
- 24h: commodity avg `0.0038` n `13`; crypto_alt avg `0.3346` n `239`; crypto_major avg `0.1182` n `8`; equity avg `0.9946` n `164`; fx avg `0.0326` n `6`; index avg `0.3161` n `27`; metal avg `-0.3231` n `20`; unknown avg `3.6445` n `1163`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
