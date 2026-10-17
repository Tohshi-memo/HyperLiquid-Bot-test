# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T15:55:02.264332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.05` n `13`; crypto_alt avg `-0.352` n `236`; crypto_major avg `-0.2541` n `8`; equity avg `-0.0457` n `151`; fx avg `0.0043` n `6`; index avg `-0.0213` n `26`; metal avg `-0.0067` n `20`; unknown avg `2.6124` n `1193`
- 1h: commodity avg `0.0432` n `13`; crypto_alt avg `-1.0142` n `236`; crypto_major avg `-0.7165` n `8`; equity avg `-0.2612` n `151`; fx avg `-0.0099` n `6`; index avg `-0.0358` n `26`; metal avg `-0.0144` n `20`; unknown avg `3.4224` n `1183`
- 4h: commodity avg `0.0805` n `13`; crypto_alt avg `-1.5821` n `236`; crypto_major avg `-0.8262` n `8`; equity avg `-0.3727` n `151`; fx avg `-0.0207` n `6`; index avg `-0.0816` n `26`; metal avg `-0.042` n `20`; unknown avg `5.549` n `1167`
- 24h: commodity avg `0.6193` n `13`; crypto_alt avg `-2.5111` n `236`; crypto_major avg `-0.8517` n `8`; equity avg `-1.6943` n `151`; fx avg `-0.0072` n `6`; index avg `-0.343` n `26`; metal avg `-0.1157` n `20`; unknown avg `1.423` n `1054`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1717`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1456`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.115`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0712`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
