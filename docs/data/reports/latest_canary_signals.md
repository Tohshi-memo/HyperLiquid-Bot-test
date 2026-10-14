# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T10:22:27.355994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `13`; crypto_alt avg `0.0518` n `235`; crypto_major avg `0.2402` n `8`; equity avg `0.1143` n `151`; fx avg `0.0023` n `6`; index avg `0.0112` n `26`; metal avg `0.0264` n `20`; unknown avg `0.9534` n `1135`
- 1h: commodity avg `0.1435` n `13`; crypto_alt avg `-0.3792` n `235`; crypto_major avg `-0.1435` n `8`; equity avg `-0.0442` n `151`; fx avg `-0.0017` n `6`; index avg `-0.0162` n `26`; metal avg `0.042` n `20`; unknown avg `-0.0649` n `1133`
- 4h: commodity avg `0.0567` n `13`; crypto_alt avg `-0.7611` n `235`; crypto_major avg `-0.3079` n `8`; equity avg `-0.0407` n `151`; fx avg `-0.0414` n `6`; index avg `0.0377` n `26`; metal avg `-0.0858` n `20`; unknown avg `1192.671` n `1037`
- 24h: commodity avg `1.2414` n `13`; crypto_alt avg `-0.7342` n `235`; crypto_major avg `-0.2076` n `8`; equity avg `-0.4312` n `151`; fx avg `0.0352` n `6`; index avg `-0.0226` n `26`; metal avg `-0.4386` n `20`; unknown avg `1268.0601` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1516`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1309`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0743`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0731`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
