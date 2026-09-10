# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T10:22:29.779510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.0481` n `233`; crypto_major avg `-0.0705` n `8`; equity avg `-0.0258` n `134`; fx avg `-0.0083` n `6`; index avg `0.0097` n `26`; metal avg `-0.0677` n `20`; unknown avg `0.1629` n `797`
- 1h: commodity avg `0.0225` n `12`; crypto_alt avg `-0.2779` n `233`; crypto_major avg `-0.1825` n `8`; equity avg `-0.0557` n `134`; fx avg `0.0046` n `6`; index avg `0.01` n `26`; metal avg `-0.0947` n `20`; unknown avg `0.1276` n `795`
- 4h: commodity avg `0.277` n `12`; crypto_alt avg `-0.4279` n `233`; crypto_major avg `-0.2842` n `8`; equity avg `-0.3176` n `134`; fx avg `0.0586` n `6`; index avg `-0.0677` n `26`; metal avg `-0.3113` n `20`; unknown avg `-0.0249` n `787`
- 24h: commodity avg `-0.0026` n `12`; crypto_alt avg `-4.1724` n `233`; crypto_major avg `-2.7141` n `8`; equity avg `-0.7943` n `134`; fx avg `0.0833` n `6`; index avg `-0.0263` n `26`; metal avg `-0.021` n `20`; unknown avg `-0.6377` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
