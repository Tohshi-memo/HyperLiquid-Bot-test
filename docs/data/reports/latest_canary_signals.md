# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T09:37:29.805110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `13`; crypto_alt avg `0.0533` n `236`; crypto_major avg `-0.0307` n `8`; equity avg `0.0812` n `151`; fx avg `-0.0008` n `6`; index avg `0.0103` n `26`; metal avg `-0.0347` n `20`; unknown avg `0.1301` n `1136`
- 1h: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.0489` n `236`; crypto_major avg `-0.092` n `8`; equity avg `0.0473` n `151`; fx avg `0.0266` n `6`; index avg `0.0243` n `26`; metal avg `-0.0229` n `20`; unknown avg `-0.1602` n `1134`
- 4h: commodity avg `-0.0465` n `13`; crypto_alt avg `0.3998` n `236`; crypto_major avg `0.2875` n `8`; equity avg `-0.1837` n `151`; fx avg `-0.0076` n `6`; index avg `-0.0295` n `26`; metal avg `0.0091` n `20`; unknown avg `0.0833` n `1048`
- 24h: commodity avg `-0.1198` n `13`; crypto_alt avg `4.0361` n `236`; crypto_major avg `1.9193` n `8`; equity avg `2.6508` n `151`; fx avg `-0.0068` n `6`; index avg `0.3536` n `26`; metal avg `0.2409` n `20`; unknown avg `27.3588` n `864`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0963`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0926`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
