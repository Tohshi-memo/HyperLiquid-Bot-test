# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T10:08:29.646057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.057` n `13`; crypto_alt avg `0.162` n `237`; crypto_major avg `0.1984` n `8`; equity avg `0.0924` n `151`; fx avg `0.0087` n `6`; index avg `0.0252` n `26`; metal avg `-0.004` n `20`; unknown avg `0.7893` n `1196`
- 1h: commodity avg `-0.0531` n `13`; crypto_alt avg `0.1307` n `237`; crypto_major avg `0.1792` n `8`; equity avg `0.0713` n `151`; fx avg `0.0325` n `6`; index avg `0.0376` n `26`; metal avg `-0.0401` n `20`; unknown avg `0.6898` n `1196`
- 4h: commodity avg `0.0903` n `13`; crypto_alt avg `-0.2216` n `237`; crypto_major avg `-0.172` n `8`; equity avg `-0.1176` n `151`; fx avg `0.001` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0368` n `20`; unknown avg `-0.5714` n `1180`
- 24h: commodity avg `0.1903` n `13`; crypto_alt avg `-0.5126` n `237`; crypto_major avg `-1.1129` n `8`; equity avg `-1.8611` n `151`; fx avg `0.0123` n `6`; index avg `-0.2705` n `26`; metal avg `-0.3193` n `20`; unknown avg `0.9545` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
