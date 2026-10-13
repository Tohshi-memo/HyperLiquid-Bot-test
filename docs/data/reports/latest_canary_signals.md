# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T09:37:30.903932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `13`; crypto_alt avg `-0.1314` n `235`; crypto_major avg `-0.015` n `8`; equity avg `0.0235` n `151`; fx avg `0.008` n `6`; index avg `0.0` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.0742` n `1135`
- 1h: commodity avg `0.0061` n `13`; crypto_alt avg `-0.673` n `235`; crypto_major avg `-0.5954` n `8`; equity avg `-0.0396` n `151`; fx avg `-0.0111` n `6`; index avg `0.0004` n `26`; metal avg `-0.0398` n `20`; unknown avg `0.2981` n `1133`
- 4h: commodity avg `-0.1394` n `13`; crypto_alt avg `-0.7363` n `235`; crypto_major avg `-0.3321` n `8`; equity avg `0.2455` n `151`; fx avg `-0.0246` n `6`; index avg `0.0845` n `26`; metal avg `-0.0056` n `20`; unknown avg `1.1178` n `1101`
- 24h: commodity avg `-0.046` n `13`; crypto_alt avg `-3.8506` n `235`; crypto_major avg `-2.1577` n `8`; equity avg `-2.6189` n `151`; fx avg `0.0368` n `6`; index avg `-0.313` n `26`; metal avg `0.0494` n `20`; unknown avg `0.0606` n `973`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1831`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1646`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1626`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1418`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0747`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0729`, n `666`, weak_sample_signal
