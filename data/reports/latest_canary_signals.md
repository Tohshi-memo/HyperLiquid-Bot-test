# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T20:07:37.518180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.029` n `13`; crypto_alt avg `-0.0395` n `237`; crypto_major avg `0.0527` n `8`; equity avg `-0.0973` n `151`; fx avg `0.0025` n `6`; index avg `0.007` n `26`; metal avg `0.0031` n `20`; unknown avg `43.9613` n `1183`
- 1h: commodity avg `0.0333` n `13`; crypto_alt avg `0.1762` n `237`; crypto_major avg `0.28` n `8`; equity avg `-0.2192` n `151`; fx avg `0.0019` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0153` n `20`; unknown avg `95.5249` n `1179`
- 4h: commodity avg `0.2738` n `13`; crypto_alt avg `-0.0468` n `237`; crypto_major avg `0.3021` n `8`; equity avg `-0.3715` n `151`; fx avg `0.0032` n `6`; index avg `-0.0385` n `26`; metal avg `-0.0475` n `20`; unknown avg `44.8846` n `1165`
- 24h: commodity avg `-0.0776` n `13`; crypto_alt avg `2.5985` n `237`; crypto_major avg `1.8217` n `8`; equity avg `0.1024` n `151`; fx avg `0.0269` n `6`; index avg `0.02` n `26`; metal avg `0.0192` n `20`; unknown avg `6.5407` n `1056`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
