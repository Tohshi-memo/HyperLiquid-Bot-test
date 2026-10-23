# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T14:37:37.738938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `13`; crypto_alt avg `0.4181` n `237`; crypto_major avg `0.3802` n `8`; equity avg `0.2001` n `152`; fx avg `0.0053` n `6`; index avg `0.0342` n `26`; metal avg `0.0408` n `20`; unknown avg `0.287` n `1231`
- 1h: commodity avg `0.247` n `13`; crypto_alt avg `0.1383` n `237`; crypto_major avg `0.1204` n `8`; equity avg `0.9219` n `152`; fx avg `0.0476` n `6`; index avg `0.0591` n `26`; metal avg `-0.1178` n `20`; unknown avg `0.0069` n `1167`
- 4h: commodity avg `0.0755` n `13`; crypto_alt avg `-0.1777` n `237`; crypto_major avg `-0.0301` n `8`; equity avg `-0.2245` n `152`; fx avg `0.0278` n `6`; index avg `-0.0267` n `26`; metal avg `-0.0929` n `20`; unknown avg `-0.2557` n `1161`
- 24h: commodity avg `0.4875` n `13`; crypto_alt avg `0.1813` n `237`; crypto_major avg `0.2173` n `8`; equity avg `-0.4957` n `152`; fx avg `-0.0324` n `6`; index avg `-0.0736` n `26`; metal avg `-0.3855` n `20`; unknown avg `-0.7188` n `984`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2003`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
