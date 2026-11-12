# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T21:37:40.057591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0601` n `13`; crypto_alt avg `0.2446` n `239`; crypto_major avg `0.1935` n `8`; equity avg `0.2987` n `162`; fx avg `-0.002` n `6`; index avg `0.0245` n `27`; metal avg `0.0004` n `20`; unknown avg `0.1539` n `1259`
- 1h: commodity avg `0.015` n `13`; crypto_alt avg `0.5468` n `239`; crypto_major avg `0.4229` n `8`; equity avg `0.6884` n `162`; fx avg `-0.0069` n `6`; index avg `0.0604` n `27`; metal avg `-0.032` n `20`; unknown avg `185.8379` n `1235`
- 4h: commodity avg `0.4132` n `13`; crypto_alt avg `1.0335` n `239`; crypto_major avg `0.5055` n `8`; equity avg `-0.1247` n `162`; fx avg `0.0091` n `6`; index avg `-0.0208` n `27`; metal avg `-0.0505` n `20`; unknown avg `0.9984` n `1223`
- 24h: commodity avg `0.8822` n `13`; crypto_alt avg `-1.7787` n `239`; crypto_major avg `-2.6936` n `8`; equity avg `-2.208` n `162`; fx avg `-0.1325` n `6`; index avg `-0.0995` n `27`; metal avg `-0.7382` n `20`; unknown avg `31.553` n `1149`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
