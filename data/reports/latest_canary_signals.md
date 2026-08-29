# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T09:52:23.432060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.0084` n `231`; crypto_major avg `-0.0026` n `8`; equity avg `0.0171` n `127`; fx avg `-0.0114` n `6`; index avg `-0.004` n `26`; metal avg `-0.0138` n `20`; unknown avg `0.0006` n `793`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `0.1269` n `231`; crypto_major avg `0.1094` n `8`; equity avg `0.0386` n `127`; fx avg `-0.0138` n `6`; index avg `-0.0103` n `26`; metal avg `-0.007` n `20`; unknown avg `0.0402` n `791`
- 4h: commodity avg `0.0485` n `12`; crypto_alt avg `-0.7244` n `231`; crypto_major avg `-0.3395` n `8`; equity avg `0.0371` n `127`; fx avg `-0.0172` n `6`; index avg `-0.0145` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.0449` n `761`
- 24h: commodity avg `0.0058` n `12`; crypto_alt avg `-1.9081` n `231`; crypto_major avg `-1.9155` n `8`; equity avg `-1.3213` n `127`; fx avg `-0.0338` n `6`; index avg `-0.1505` n `26`; metal avg `-0.7404` n `20`; unknown avg `-0.3818` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
