# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T14:46:13.670316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `12`; crypto_alt avg `0.1909` n `230`; crypto_major avg `0.2988` n `8`; equity avg `0.2145` n `107`; fx avg `0.0007` n `6`; index avg `0.0081` n `25`; metal avg `0.0461` n `20`; unknown avg `0.0119` n `782`
- 1h: commodity avg `0.0973` n `12`; crypto_alt avg `-0.0293` n `230`; crypto_major avg `0.3318` n `8`; equity avg `0.319` n `107`; fx avg `0.0356` n `6`; index avg `0.0319` n `25`; metal avg `-0.0572` n `20`; unknown avg `0.0474` n `782`
- 4h: commodity avg `-1.0257` n `12`; crypto_alt avg `-0.3184` n `230`; crypto_major avg `0.2612` n `8`; equity avg `1.2285` n `107`; fx avg `-0.0565` n `6`; index avg `0.3324` n `25`; metal avg `0.4321` n `20`; unknown avg `-0.2163` n `781`
- 24h: commodity avg `-0.9249` n `12`; crypto_alt avg `-0.0385` n `230`; crypto_major avg `0.5715` n `8`; equity avg `3.4804` n `107`; fx avg `0.0973` n `6`; index avg `0.6618` n `25`; metal avg `1.0394` n `20`; unknown avg `0.6073` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
