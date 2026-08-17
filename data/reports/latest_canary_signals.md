# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T16:52:47.732653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `12`; crypto_alt avg `-0.0149` n `230`; crypto_major avg `-0.0731` n `8`; equity avg `-0.0156` n `114`; fx avg `-0.0114` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0274` n `20`; unknown avg `0.102` n `792`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `-0.1563` n `230`; crypto_major avg `-0.1559` n `8`; equity avg `-0.0361` n `114`; fx avg `-0.0011` n `6`; index avg `-0.0271` n `25`; metal avg `-0.0331` n `20`; unknown avg `0.2253` n `792`
- 4h: commodity avg `0.0359` n `12`; crypto_alt avg `0.1353` n `230`; crypto_major avg `0.5117` n `8`; equity avg `0.8739` n `114`; fx avg `0.0281` n `6`; index avg `0.0858` n `25`; metal avg `0.1875` n `20`; unknown avg `0.166` n `792`
- 24h: commodity avg `0.0554` n `12`; crypto_alt avg `-0.132` n `230`; crypto_major avg `0.7701` n `8`; equity avg `1.6674` n `114`; fx avg `0.014` n `6`; index avg `0.1751` n `25`; metal avg `0.269` n `20`; unknown avg `0.1014` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
