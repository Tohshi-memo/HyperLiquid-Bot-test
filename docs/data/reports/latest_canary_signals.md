# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T09:36:50.868079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `80.61` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0745` n `234`; crypto_major avg `-0.4199` n `8`; equity avg `-0.0213` n `140`; fx avg `0.0066` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.4455` n `942`
- 1h: commodity avg `-0.023` n `12`; crypto_alt avg `0.095` n `234`; crypto_major avg `-0.3532` n `8`; equity avg `-0.0399` n `140`; fx avg `0.0373` n `6`; index avg `-0.0109` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.8857` n `940`
- 4h: commodity avg `-0.0214` n `12`; crypto_alt avg `0.3182` n `234`; crypto_major avg `-0.4602` n `8`; equity avg `-0.0495` n `140`; fx avg `0.0114` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0171` n `20`; unknown avg `1.9173` n `898`
- 24h: commodity avg `0.2042` n `12`; crypto_alt avg `3.1463` n `234`; crypto_major avg `3.4726` n `8`; equity avg `0.2403` n `140`; fx avg `-0.0392` n `6`; index avg `-0.025` n `26`; metal avg `-0.2034` n `20`; unknown avg `2.6818` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
