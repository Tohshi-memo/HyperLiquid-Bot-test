# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T21:10:02.716589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1074` n `13`; crypto_alt avg `-0.1571` n `235`; crypto_major avg `-0.1086` n `8`; equity avg `-0.023` n `143`; fx avg `0.0034` n `6`; index avg `-0.0041` n `26`; metal avg `0.002` n `20`; unknown avg `-0.0208` n `1077`
- 1h: commodity avg `0.1154` n `13`; crypto_alt avg `-0.0184` n `235`; crypto_major avg `-0.2267` n `8`; equity avg `-0.0257` n `143`; fx avg `0.0099` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0015` n `20`; unknown avg `-0.2205` n `1077`
- 4h: commodity avg `0.0313` n `13`; crypto_alt avg `0.1207` n `235`; crypto_major avg `-0.0804` n `8`; equity avg `0.0439` n `143`; fx avg `0.0051` n `6`; index avg `0.0051` n `26`; metal avg `0.0006` n `20`; unknown avg `0.0825` n `1062`
- 24h: commodity avg `0.1485` n `13`; crypto_alt avg `2.9011` n `235`; crypto_major avg `1.3281` n `8`; equity avg `0.1504` n `143`; fx avg `-0.0156` n `6`; index avg `0.0318` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.4422` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
