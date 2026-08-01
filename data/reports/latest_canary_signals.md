# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T23:52:24.689175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1784` n `12`; crypto_alt avg `-0.04` n `230`; crypto_major avg `-0.0134` n `8`; equity avg `0.0049` n `102`; fx avg `-0.0275` n `6`; index avg `0.0111` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0365` n `782`
- 1h: commodity avg `-0.1408` n `12`; crypto_alt avg `-0.0797` n `230`; crypto_major avg `-0.0286` n `8`; equity avg `-0.014` n `102`; fx avg `-0.0816` n `6`; index avg `0.0151` n `25`; metal avg `-0.002` n `20`; unknown avg `1.8274` n `782`
- 4h: commodity avg `-0.3171` n `12`; crypto_alt avg `0.117` n `230`; crypto_major avg `0.4194` n `8`; equity avg `0.2809` n `102`; fx avg `-0.0801` n `6`; index avg `0.0357` n `25`; metal avg `0.0306` n `20`; unknown avg `0.0321` n `782`
- 24h: commodity avg `-0.3352` n `12`; crypto_alt avg `-0.5876` n `230`; crypto_major avg `-0.7861` n `8`; equity avg `-0.0794` n `102`; fx avg `-0.1062` n `6`; index avg `0.0248` n `25`; metal avg `0.0452` n `20`; unknown avg `-0.0607` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
