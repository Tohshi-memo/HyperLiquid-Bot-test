# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T08:37:27.629047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0913` n `13`; crypto_alt avg `0.2905` n `236`; crypto_major avg `0.2102` n `8`; equity avg `0.0411` n `151`; fx avg `-0.0034` n `6`; index avg `-0.0017` n `26`; metal avg `0.0077` n `20`; unknown avg `1.8997` n `1134`
- 1h: commodity avg `-0.1331` n `13`; crypto_alt avg `0.1265` n `236`; crypto_major avg `0.2261` n `8`; equity avg `0.0207` n `151`; fx avg `0.0086` n `6`; index avg `-0.0087` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.0809` n `1066`
- 4h: commodity avg `-0.077` n `13`; crypto_alt avg `0.6339` n `236`; crypto_major avg `0.5724` n `8`; equity avg `-0.3764` n `151`; fx avg `-0.1007` n `6`; index avg `-0.0664` n `26`; metal avg `-0.0158` n `20`; unknown avg `-0.1268` n `1048`
- 24h: commodity avg `-0.0845` n `13`; crypto_alt avg `3.9519` n `236`; crypto_major avg `1.9449` n `8`; equity avg `2.687` n `151`; fx avg `-0.0173` n `6`; index avg `0.3328` n `26`; metal avg `0.3356` n `20`; unknown avg `27.573` n `864`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0974`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0927`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0908`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0904`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
