# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T23:37:25.786357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `0.0831` n `236`; crypto_major avg `0.1406` n `8`; equity avg `-0.0794` n `151`; fx avg `-0.0032` n `6`; index avg `-0.0169` n `26`; metal avg `-0.0183` n `20`; unknown avg `0.1759` n `1136`
- 1h: commodity avg `-0.0726` n `13`; crypto_alt avg `-0.426` n `236`; crypto_major avg `-0.4511` n `8`; equity avg `-0.3222` n `151`; fx avg `-0.0166` n `6`; index avg `-0.056` n `26`; metal avg `-0.0549` n `20`; unknown avg `0.3379` n `1134`
- 4h: commodity avg `-0.1081` n `13`; crypto_alt avg `-0.4872` n `236`; crypto_major avg `-0.3374` n `8`; equity avg `-0.3` n `151`; fx avg `-0.0199` n `6`; index avg `-0.0851` n `26`; metal avg `0.003` n `20`; unknown avg `-0.4758` n `1020`
- 24h: commodity avg `-0.2403` n `13`; crypto_alt avg `0.2551` n `236`; crypto_major avg `0.3479` n `8`; equity avg `1.2651` n `151`; fx avg `0.1052` n `6`; index avg `0.0621` n `26`; metal avg `0.4633` n `20`; unknown avg `24.5899` n `910`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0923`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.092`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0796`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0678`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0548`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0542`, n `666`, weak_sample_signal
