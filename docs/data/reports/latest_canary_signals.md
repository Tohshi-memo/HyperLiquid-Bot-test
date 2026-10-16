# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T10:52:27.472004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0544` n `13`; crypto_alt avg `-0.0513` n `236`; crypto_major avg `0.1265` n `8`; equity avg `0.0008` n `151`; fx avg `0.0082` n `6`; index avg `-0.0183` n `26`; metal avg `-0.0315` n `20`; unknown avg `-0.0661` n `1136`
- 1h: commodity avg `0.1106` n `13`; crypto_alt avg `0.0703` n `236`; crypto_major avg `0.1826` n `8`; equity avg `-0.1388` n `151`; fx avg `0.0353` n `6`; index avg `0.0038` n `26`; metal avg `0.0199` n `20`; unknown avg `0.9172` n `1134`
- 4h: commodity avg `-0.0205` n `13`; crypto_alt avg `-0.277` n `236`; crypto_major avg `0.062` n `8`; equity avg `-0.1894` n `151`; fx avg `0.069` n `6`; index avg `-0.0173` n `26`; metal avg `0.0179` n `20`; unknown avg `0.3023` n `1066`
- 24h: commodity avg `0.0219` n `13`; crypto_alt avg `4.6027` n `236`; crypto_major avg `2.5917` n `8`; equity avg `2.7252` n `151`; fx avg `0.046` n `6`; index avg `0.3424` n `26`; metal avg `0.2748` n `20`; unknown avg `25.3979` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0983`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
