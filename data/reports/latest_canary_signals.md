# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T05:59:43.176270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.139` n `230`; crypto_major avg `0.0575` n `8`; equity avg `-0.0229` n `114`; fx avg `-0.0016` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0103` n `20`; unknown avg `35.0336` n `785`
- 1h: commodity avg `0.0176` n `12`; crypto_alt avg `0.1213` n `230`; crypto_major avg `-0.1388` n `8`; equity avg `-0.0763` n `114`; fx avg `-0.0007` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0075` n `20`; unknown avg `28.0944` n `785`
- 4h: commodity avg `0.0573` n `12`; crypto_alt avg `0.3739` n `230`; crypto_major avg `0.0559` n `8`; equity avg `-0.0183` n `114`; fx avg `0.0536` n `6`; index avg `-0.0249` n `25`; metal avg `-0.0267` n `20`; unknown avg `23.2532` n `785`
- 24h: commodity avg `0.1164` n `12`; crypto_alt avg `0.6771` n `230`; crypto_major avg `-0.3186` n `8`; equity avg `-0.1444` n `114`; fx avg `0.1683` n `6`; index avg `-0.0802` n `25`; metal avg `0.3459` n `20`; unknown avg `-0.1307` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
