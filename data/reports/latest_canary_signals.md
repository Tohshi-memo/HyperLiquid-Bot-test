# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T10:37:35.677060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.1618` n `236`; crypto_major avg `0.1888` n `8`; equity avg `0.0083` n `151`; fx avg `0.0328` n `6`; index avg `0.0108` n `26`; metal avg `0.0116` n `20`; unknown avg `0.1588` n `1136`
- 1h: commodity avg `0.1173` n `13`; crypto_alt avg `0.0208` n `236`; crypto_major avg `-0.0086` n `8`; equity avg `-0.295` n `151`; fx avg `0.0196` n `6`; index avg `-0.0283` n `26`; metal avg `0.0255` n `20`; unknown avg `2.2332` n `1134`
- 4h: commodity avg `0.0765` n `13`; crypto_alt avg `0.1077` n `236`; crypto_major avg `0.08` n `8`; equity avg `-0.1244` n `151`; fx avg `0.0654` n `6`; index avg `0.0114` n `26`; metal avg `0.0592` n `20`; unknown avg `0.3396` n `1066`
- 24h: commodity avg `-0.0024` n `13`; crypto_alt avg `4.4284` n `236`; crypto_major avg `2.2507` n `8`; equity avg `2.4579` n `151`; fx avg `0.0504` n `6`; index avg `0.3253` n `26`; metal avg `0.3141` n `20`; unknown avg `25.2863` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0846`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.076`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
