# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T07:07:26.314506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `-0.1299` n `237`; crypto_major avg `-0.011` n `8`; equity avg `0.0248` n `151`; fx avg `-0.0043` n `6`; index avg `0.0177` n `26`; metal avg `0.0039` n `20`; unknown avg `0.0268` n `1191`
- 1h: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0769` n `237`; crypto_major avg `0.059` n `8`; equity avg `0.0804` n `151`; fx avg `-0.0109` n `6`; index avg `0.025` n `26`; metal avg `0.0001` n `20`; unknown avg `0.0527` n `1191`
- 4h: commodity avg `-0.047` n `13`; crypto_alt avg `-0.5851` n `237`; crypto_major avg `-0.3345` n `8`; equity avg `0.1607` n `151`; fx avg `-0.013` n `6`; index avg `0.0513` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.1863` n `1169`
- 24h: commodity avg `0.0885` n `13`; crypto_alt avg `-2.6927` n `236`; crypto_major avg `-0.8689` n `8`; equity avg `-0.8479` n `151`; fx avg `-0.0538` n `6`; index avg `-0.0765` n `26`; metal avg `-0.0663` n `20`; unknown avg `3.9107` n `1053`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.169`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1321`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0821`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
