# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T10:37:27.458987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.0776` n `230`; crypto_major avg `-0.0048` n `8`; equity avg `0.1467` n `102`; fx avg `-0.0151` n `6`; index avg `0.0115` n `25`; metal avg `0.0147` n `20`; unknown avg `0.008` n `779`
- 1h: commodity avg `-0.028` n `12`; crypto_alt avg `-0.0868` n `230`; crypto_major avg `0.002` n `8`; equity avg `0.3489` n `102`; fx avg `-0.0605` n `6`; index avg `0.0575` n `25`; metal avg `0.0752` n `20`; unknown avg `0.0142` n `779`
- 4h: commodity avg `-0.3474` n `12`; crypto_alt avg `0.1129` n `230`; crypto_major avg `0.6726` n `8`; equity avg `0.968` n `102`; fx avg `-0.0164` n `6`; index avg `0.1603` n `25`; metal avg `0.4889` n `20`; unknown avg `0.0002` n `771`
- 24h: commodity avg `0.4033` n `12`; crypto_alt avg `-0.2968` n `230`; crypto_major avg `-0.0929` n `8`; equity avg `-2.5591` n `102`; fx avg `-0.0555` n `6`; index avg `-0.3687` n `25`; metal avg `0.4637` n `20`; unknown avg `-0.1251` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
