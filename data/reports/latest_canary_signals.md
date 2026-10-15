# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T01:52:30.250419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1018` n `13`; crypto_alt avg `-0.2941` n `236`; crypto_major avg `-0.1757` n `8`; equity avg `-0.2733` n `151`; fx avg `-0.0444` n `6`; index avg `-0.0558` n `26`; metal avg `-0.0333` n `20`; unknown avg `1.4877` n `1136`
- 1h: commodity avg `-0.1417` n `13`; crypto_alt avg `-0.194` n `236`; crypto_major avg `-0.0774` n `8`; equity avg `-0.1697` n `151`; fx avg `0.02` n `6`; index avg `-0.0716` n `26`; metal avg `0.0366` n `20`; unknown avg `2.2625` n `1134`
- 4h: commodity avg `-0.3302` n `13`; crypto_alt avg `-0.68` n `236`; crypto_major avg `-0.2953` n `8`; equity avg `-1.3588` n `151`; fx avg `0.2038` n `6`; index avg `-0.3869` n `26`; metal avg `0.2178` n `20`; unknown avg `2.298` n `1072`
- 24h: commodity avg `-0.5438` n `13`; crypto_alt avg `-3.174` n `236`; crypto_major avg `-2.4742` n `8`; equity avg `-5.9298` n `151`; fx avg `0.0539` n `6`; index avg `-0.9965` n `26`; metal avg `-0.5569` n `20`; unknown avg `1395.8631` n `890`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1182`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1035`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0947`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
