# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T07:37:26.535263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0431` n `13`; crypto_alt avg `0.0054` n `238`; crypto_major avg `-0.1203` n `8`; equity avg `-0.1266` n `155`; fx avg `0.0217` n `6`; index avg `-0.0322` n `27`; metal avg `-0.0319` n `20`; unknown avg `161.5353` n `1238`
- 1h: commodity avg `0.0347` n `13`; crypto_alt avg `-0.5752` n `238`; crypto_major avg `-0.36` n `8`; equity avg `-0.2843` n `155`; fx avg `0.0247` n `6`; index avg `-0.0368` n `27`; metal avg `-0.0118` n `20`; unknown avg `8.1315` n `1230`
- 4h: commodity avg `0.0465` n `13`; crypto_alt avg `-0.2312` n `238`; crypto_major avg `0.1834` n `8`; equity avg `0.0447` n `155`; fx avg `0.0263` n `6`; index avg `0.0934` n `27`; metal avg `-0.1168` n `20`; unknown avg `0.1975` n `1188`
- 24h: commodity avg `-0.1613` n `13`; crypto_alt avg `-2.6194` n `238`; crypto_major avg `-1.5994` n `8`; equity avg `-1.539` n `154`; fx avg `0.0792` n `6`; index avg `-0.0817` n `27`; metal avg `-0.3247` n `20`; unknown avg `30.438` n `968`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
