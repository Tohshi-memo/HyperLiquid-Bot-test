# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T06:07:27.203627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0382` n `12`; crypto_alt avg `-0.1368` n `232`; crypto_major avg `-0.2363` n `8`; equity avg `0.1278` n `128`; fx avg `-0.0111` n `6`; index avg `0.0131` n `26`; metal avg `-0.055` n `20`; unknown avg `0.074` n `773`
- 1h: commodity avg `0.0782` n `12`; crypto_alt avg `0.4553` n `232`; crypto_major avg `0.4594` n `8`; equity avg `0.2938` n `128`; fx avg `-0.0385` n `6`; index avg `0.0085` n `26`; metal avg `0.0184` n `20`; unknown avg `0.241` n `773`
- 4h: commodity avg `0.0721` n `12`; crypto_alt avg `1.0303` n `231`; crypto_major avg `0.5394` n `8`; equity avg `0.7322` n `128`; fx avg `-0.0411` n `6`; index avg `0.1657` n `26`; metal avg `0.0318` n `20`; unknown avg `0.2119` n `773`
- 24h: commodity avg `0.5256` n `12`; crypto_alt avg `-0.181` n `231`; crypto_major avg `-1.5678` n `8`; equity avg `-0.4734` n `128`; fx avg `-0.0782` n `6`; index avg `-0.11` n `26`; metal avg `-0.3278` n `20`; unknown avg `13.8936` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
