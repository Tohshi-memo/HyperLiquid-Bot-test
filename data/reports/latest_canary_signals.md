# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T22:22:25.194931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0361` n `13`; crypto_alt avg `-0.0625` n `238`; crypto_major avg `-0.0668` n `8`; equity avg `-0.0631` n `155`; fx avg `-0.0034` n `6`; index avg `-0.011` n `27`; metal avg `-0.0406` n `20`; unknown avg `4.9714` n `1238`
- 1h: commodity avg `0.0061` n `13`; crypto_alt avg `-0.5872` n `238`; crypto_major avg `-0.3307` n `8`; equity avg `0.0164` n `155`; fx avg `-0.0033` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0257` n `20`; unknown avg `12.0286` n `1232`
- 4h: commodity avg `-0.3102` n `13`; crypto_alt avg `1.2598` n `238`; crypto_major avg `0.7078` n `8`; equity avg `-0.165` n `155`; fx avg `-0.0046` n `6`; index avg `-0.0426` n `27`; metal avg `0.18` n `20`; unknown avg `3.8023` n `1112`
- 24h: commodity avg `0.1992` n `13`; crypto_alt avg `0.724` n `238`; crypto_major avg `0.6009` n `8`; equity avg `0.9223` n `154`; fx avg `0.2338` n `6`; index avg `0.1431` n `27`; metal avg `-0.1385` n `20`; unknown avg `25.2737` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
