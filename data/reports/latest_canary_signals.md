# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T09:52:34.167033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `13`; crypto_alt avg `-0.2673` n `235`; crypto_major avg `-0.0519` n `8`; equity avg `-0.1608` n `151`; fx avg `-0.0261` n `6`; index avg `-0.0143` n `26`; metal avg `0.0076` n `20`; unknown avg `0.7955` n `1135`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.7786` n `235`; crypto_major avg `-0.3837` n `8`; equity avg `-0.1456` n `151`; fx avg `-0.0128` n `6`; index avg `0.0059` n `26`; metal avg `0.0053` n `20`; unknown avg `-0.0588` n `1133`
- 4h: commodity avg `-0.166` n `13`; crypto_alt avg `-1.2246` n `235`; crypto_major avg `-0.5948` n `8`; equity avg `0.108` n `151`; fx avg `-0.0572` n `6`; index avg `0.0794` n `26`; metal avg `0.013` n `20`; unknown avg `0.6462` n `1101`
- 24h: commodity avg `-0.0167` n `13`; crypto_alt avg `-4.2168` n `235`; crypto_major avg `-2.2993` n `8`; equity avg `-2.8108` n `151`; fx avg `0.0292` n `6`; index avg `-0.3355` n `26`; metal avg `0.0194` n `20`; unknown avg `0.0294` n `973`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1826`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1647`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1636`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1422`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0748`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.073`, n `666`, weak_sample_signal
