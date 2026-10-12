# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T03:07:24.920910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `-0.1317` n `235`; crypto_major avg `-0.0961` n `8`; equity avg `-0.0559` n `151`; fx avg `-0.0143` n `6`; index avg `-0.0155` n `26`; metal avg `-0.0231` n `20`; unknown avg `-0.0822` n `1131`
- 1h: commodity avg `-0.0254` n `13`; crypto_alt avg `0.349` n `235`; crypto_major avg `0.1267` n `8`; equity avg `-0.5281` n `151`; fx avg `-0.0361` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0296` n `20`; unknown avg `-0.3569` n `1111`
- 4h: commodity avg `-0.5723` n `13`; crypto_alt avg `0.0644` n `235`; crypto_major avg `0.1893` n `8`; equity avg `-0.6249` n `151`; fx avg `-0.0625` n `6`; index avg `-0.0288` n `26`; metal avg `0.1585` n `20`; unknown avg `0.6093` n `1097`
- 24h: commodity avg `-0.4398` n `13`; crypto_alt avg `2.1369` n `235`; crypto_major avg `1.0114` n `8`; equity avg `-0.264` n `151`; fx avg `-0.0605` n `6`; index avg `0.0083` n `26`; metal avg `0.1554` n `20`; unknown avg `0.7074` n `928`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
