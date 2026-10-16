# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T07:37:27.553225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `13`; crypto_alt avg `-0.3609` n `236`; crypto_major avg `-0.1904` n `8`; equity avg `-0.1495` n `151`; fx avg `-0.01` n `6`; index avg `-0.0115` n `26`; metal avg `-0.0093` n `20`; unknown avg `-0.0556` n `1136`
- 1h: commodity avg `0.1273` n `13`; crypto_alt avg `0.007` n `236`; crypto_major avg `-0.045` n `8`; equity avg `0.1035` n `151`; fx avg `0.0106` n `6`; index avg `0.0241` n `26`; metal avg `0.0824` n `20`; unknown avg `-0.0928` n `1134`
- 4h: commodity avg `0.148` n `13`; crypto_alt avg `1.4159` n `236`; crypto_major avg `0.7789` n `8`; equity avg `0.249` n `151`; fx avg `-0.0744` n `6`; index avg `0.0384` n `26`; metal avg `0.1153` n `20`; unknown avg `0.5373` n `1102`
- 24h: commodity avg `0.0948` n `13`; crypto_alt avg `4.5546` n `236`; crypto_major avg `2.0398` n `8`; equity avg `2.4849` n `151`; fx avg `-0.0215` n `6`; index avg `0.3336` n `26`; metal avg `0.4554` n `20`; unknown avg `26.3617` n `904`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0975`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0953`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0929`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
