# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T18:44:17.381745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.0346` n `230`; crypto_major avg `0.0344` n `8`; equity avg `0.0138` n `114`; fx avg `0.0006` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0066` n `20`; unknown avg `0.4145` n `791`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.132` n `230`; crypto_major avg `-0.0689` n `8`; equity avg `0.0239` n `114`; fx avg `0.0023` n `6`; index avg `-0.0022` n `25`; metal avg `0.0064` n `20`; unknown avg `0.3997` n `791`
- 4h: commodity avg `0.051` n `12`; crypto_alt avg `0.2176` n `230`; crypto_major avg `0.1523` n `8`; equity avg `0.0511` n `114`; fx avg `-0.0006` n `6`; index avg `0.0119` n `25`; metal avg `-0.0021` n `20`; unknown avg `5.1104` n `791`
- 24h: commodity avg `-0.1116` n `12`; crypto_alt avg `0.8761` n `230`; crypto_major avg `0.5231` n `8`; equity avg `0.3918` n `114`; fx avg `0.0271` n `6`; index avg `0.0384` n `25`; metal avg `0.0407` n `20`; unknown avg `0.0194` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
