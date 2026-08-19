# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T12:07:31.302306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `-0.0146` n `230`; crypto_major avg `-0.0183` n `8`; equity avg `0.1437` n `120`; fx avg `-0.0139` n `6`; index avg `0.0385` n `25`; metal avg `0.0364` n `20`; unknown avg `0.0124` n `792`
- 1h: commodity avg `0.0577` n `12`; crypto_alt avg `-0.0034` n `230`; crypto_major avg `-0.0169` n `8`; equity avg `-0.2981` n `120`; fx avg `-0.0118` n `6`; index avg `-0.0082` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0569` n `792`
- 4h: commodity avg `0.1473` n `12`; crypto_alt avg `0.1874` n `230`; crypto_major avg `0.3432` n `8`; equity avg `-0.9254` n `120`; fx avg `-0.033` n `6`; index avg `-0.0714` n `25`; metal avg `0.0746` n `20`; unknown avg `0.1137` n `789`
- 24h: commodity avg `0.4088` n `12`; crypto_alt avg `0.2853` n `230`; crypto_major avg `0.2551` n `8`; equity avg `-2.1917` n `120`; fx avg `-0.215` n `6`; index avg `-0.2361` n `25`; metal avg `-0.3875` n `20`; unknown avg `-0.0753` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
