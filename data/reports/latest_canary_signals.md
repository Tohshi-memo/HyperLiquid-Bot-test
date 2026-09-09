# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T21:37:26.195882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3921` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.1197` n `233`; crypto_major avg `0.0364` n `8`; equity avg `-0.0026` n `134`; fx avg `0.0` n `6`; index avg `-0.0049` n `26`; metal avg `0.002` n `20`; unknown avg `0.6214` n `797`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.5589` n `233`; crypto_major avg `-0.2598` n `8`; equity avg `-0.1159` n `134`; fx avg `0.0048` n `6`; index avg `-0.004` n `26`; metal avg `0.0143` n `20`; unknown avg `34.7748` n `781`
- 4h: commodity avg `0.0876` n `12`; crypto_alt avg `-1.8267` n `233`; crypto_major avg `-1.3951` n `8`; equity avg `-0.3551` n `134`; fx avg `-0.021` n `6`; index avg `-0.003` n `26`; metal avg `-0.1621` n `20`; unknown avg `2.693` n `745`
- 24h: commodity avg `0.1016` n `12`; crypto_alt avg `-1.7316` n `233`; crypto_major avg `-1.1242` n `8`; equity avg `-0.4878` n `134`; fx avg `-0.0128` n `6`; index avg `-0.1242` n `26`; metal avg `0.4803` n `20`; unknown avg `7.7691` n `695`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
