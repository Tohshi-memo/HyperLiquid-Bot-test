# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T06:37:24.589362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `-0.1144` n `232`; crypto_major avg `-0.3195` n `8`; equity avg `-0.1755` n `133`; fx avg `-0.0164` n `6`; index avg `-0.0218` n `26`; metal avg `-0.0544` n `20`; unknown avg `18.0619` n `791`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.409` n `232`; crypto_major avg `-0.4034` n `8`; equity avg `-0.2796` n `133`; fx avg `-0.0385` n `6`; index avg `-0.0501` n `26`; metal avg `-0.0811` n `20`; unknown avg `0.9492` n `755`
- 4h: commodity avg `-0.1089` n `12`; crypto_alt avg `-0.746` n `232`; crypto_major avg `-0.2943` n `8`; equity avg `0.0461` n `133`; fx avg `-0.0349` n `6`; index avg `0.0549` n `26`; metal avg `-0.108` n `20`; unknown avg `0.5114` n `755`
- 24h: commodity avg `-0.062` n `12`; crypto_alt avg `1.5833` n `232`; crypto_major avg `3.4619` n `8`; equity avg `1.6946` n `133`; fx avg `-0.1128` n `6`; index avg `0.3295` n `26`; metal avg `0.4114` n `20`; unknown avg `1.6933` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
