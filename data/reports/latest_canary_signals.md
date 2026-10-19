# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T23:07:35.349447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `13`; crypto_alt avg `-0.0615` n `237`; crypto_major avg `-0.1094` n `8`; equity avg `0.0589` n `151`; fx avg `-0.0016` n `6`; index avg `0.0126` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.5925` n `1195`
- 1h: commodity avg `0.0232` n `13`; crypto_alt avg `0.0555` n `237`; crypto_major avg `-0.1211` n `8`; equity avg `0.085` n `151`; fx avg `-0.0283` n `6`; index avg `0.0085` n `26`; metal avg `-0.0473` n `20`; unknown avg `0.3648` n `1194`
- 4h: commodity avg `-0.0147` n `13`; crypto_alt avg `0.7464` n `237`; crypto_major avg `0.5823` n `8`; equity avg `0.227` n `151`; fx avg `-0.0138` n `6`; index avg `0.0377` n `26`; metal avg `-0.0845` n `20`; unknown avg `4.6572` n `1114`
- 24h: commodity avg `0.0056` n `13`; crypto_alt avg `1.1973` n `237`; crypto_major avg `0.685` n `8`; equity avg `1.7366` n `151`; fx avg `-0.023` n `6`; index avg `0.3607` n `26`; metal avg `-0.1891` n `20`; unknown avg `5.8038` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
