# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T04:22:27.071402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0383` n `12`; crypto_alt avg `0.0572` n `233`; crypto_major avg `0.0558` n `8`; equity avg `-0.0628` n `134`; fx avg `-0.0288` n `6`; index avg `-0.0115` n `26`; metal avg `-0.0052` n `20`; unknown avg `0.2547` n `798`
- 1h: commodity avg `-0.1099` n `12`; crypto_alt avg `0.6091` n `233`; crypto_major avg `0.5607` n `8`; equity avg `-0.2076` n `134`; fx avg `-0.0455` n `6`; index avg `-0.0316` n `26`; metal avg `-0.0669` n `20`; unknown avg `0.6115` n `795`
- 4h: commodity avg `-0.1293` n `12`; crypto_alt avg `-0.296` n `233`; crypto_major avg `0.0555` n `8`; equity avg `0.0376` n `134`; fx avg `-0.0379` n `6`; index avg `-0.0022` n `26`; metal avg `0.1084` n `20`; unknown avg `-0.0715` n `785`
- 24h: commodity avg `-0.0156` n `12`; crypto_alt avg `-0.1973` n `232`; crypto_major avg `0.9602` n `8`; equity avg `-0.0327` n `134`; fx avg `-0.0558` n `6`; index avg `-0.2351` n `26`; metal avg `-0.4501` n `20`; unknown avg `0.1258` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
