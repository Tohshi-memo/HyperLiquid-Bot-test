# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T06:52:25.890269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `13`; crypto_alt avg `-0.0939` n `237`; crypto_major avg `-0.0839` n `8`; equity avg `-0.1203` n `151`; fx avg `0.0` n `6`; index avg `-0.0155` n `26`; metal avg `-0.0346` n `20`; unknown avg `0.118` n `1198`
- 1h: commodity avg `-0.0632` n `13`; crypto_alt avg `0.3166` n `237`; crypto_major avg `0.1756` n `8`; equity avg `-0.0436` n `151`; fx avg `-0.0092` n `6`; index avg `0.0032` n `26`; metal avg `-0.1006` n `20`; unknown avg `-0.0177` n `1176`
- 4h: commodity avg `-0.0471` n `13`; crypto_alt avg `-0.191` n `237`; crypto_major avg `-0.2217` n `8`; equity avg `-0.2966` n `151`; fx avg `-0.0561` n `6`; index avg `-0.0896` n `26`; metal avg `-0.1529` n `20`; unknown avg `1.8257` n `1170`
- 24h: commodity avg `0.0214` n `13`; crypto_alt avg `2.6304` n `237`; crypto_major avg `1.7979` n `8`; equity avg `2.2267` n `151`; fx avg `-0.0155` n `6`; index avg `0.2519` n `26`; metal avg `-0.2833` n `20`; unknown avg `5282.0278` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
