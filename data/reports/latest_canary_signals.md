# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T07:37:28.226599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `0.4148` n `232`; crypto_major avg `0.3014` n `8`; equity avg `-0.0357` n `134`; fx avg `-0.0229` n `6`; index avg `-0.0234` n `26`; metal avg `-0.0589` n `20`; unknown avg `1.1572` n `797`
- 1h: commodity avg `0.1435` n `12`; crypto_alt avg `0.6276` n `232`; crypto_major avg `0.5543` n `8`; equity avg `0.2091` n `134`; fx avg `-0.0322` n `6`; index avg `0.0231` n `26`; metal avg `0.0369` n `20`; unknown avg `0.5974` n `795`
- 4h: commodity avg `0.2689` n `12`; crypto_alt avg `0.1139` n `232`; crypto_major avg `0.0463` n `8`; equity avg `-0.8914` n `134`; fx avg `0.0983` n `6`; index avg `-0.2671` n `26`; metal avg `-0.19` n `20`; unknown avg `0.7069` n `747`
- 24h: commodity avg `0.425` n `12`; crypto_alt avg `1.2609` n `232`; crypto_major avg `-0.3476` n `8`; equity avg `-0.1543` n `134`; fx avg `-0.1881` n `6`; index avg `-0.1082` n `26`; metal avg `0.1232` n `20`; unknown avg `7509.041` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
