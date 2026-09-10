# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T01:07:29.167769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `0.3576` n `233`; crypto_major avg `0.2761` n `8`; equity avg `-0.0833` n `134`; fx avg `-0.0026` n `6`; index avg `-0.0379` n `26`; metal avg `0.052` n `20`; unknown avg `8.5456` n `795`
- 1h: commodity avg `-0.0889` n `12`; crypto_alt avg `-0.2151` n `233`; crypto_major avg `0.0487` n `8`; equity avg `-0.3904` n `134`; fx avg `-0.0228` n `6`; index avg `-0.1029` n `26`; metal avg `0.0681` n `20`; unknown avg `8.1301` n `789`
- 4h: commodity avg `-0.0831` n `12`; crypto_alt avg `-1.5358` n `233`; crypto_major avg `-0.6631` n `8`; equity avg `-0.4865` n `134`; fx avg `-0.0148` n `6`; index avg `-0.0551` n `26`; metal avg `0.025` n `20`; unknown avg `-0.1114` n `729`
- 24h: commodity avg `0.0112` n `12`; crypto_alt avg `-2.9857` n `233`; crypto_major avg `-2.0668` n `8`; equity avg `-1.2601` n `134`; fx avg `-0.0299` n `6`; index avg `-0.2661` n `26`; metal avg `0.452` n `20`; unknown avg `0.6633` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
