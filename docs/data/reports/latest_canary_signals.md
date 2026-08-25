# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T08:37:52.773302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1316` n `12`; crypto_alt avg `0.0986` n `231`; crypto_major avg `0.0517` n `8`; equity avg `0.1173` n `122`; fx avg `-0.0193` n `6`; index avg `0.0237` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.1366` n `794`
- 1h: commodity avg `-0.1089` n `12`; crypto_alt avg `-0.4959` n `231`; crypto_major avg `-0.434` n `8`; equity avg `0.1651` n `122`; fx avg `-0.0143` n `6`; index avg `0.0281` n `25`; metal avg `-0.0727` n `20`; unknown avg `-0.0966` n `794`
- 4h: commodity avg `-0.2863` n `12`; crypto_alt avg `-0.5914` n `231`; crypto_major avg `-0.3653` n `8`; equity avg `0.544` n `122`; fx avg `0.0357` n `6`; index avg `0.0982` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.1718` n `778`
- 24h: commodity avg `-0.3743` n `12`; crypto_alt avg `1.8203` n `231`; crypto_major avg `2.9898` n `8`; equity avg `0.424` n `122`; fx avg `0.0118` n `6`; index avg `0.0543` n `25`; metal avg `-0.1764` n `20`; unknown avg `0.734` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
