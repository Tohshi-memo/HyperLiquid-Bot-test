# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T23:22:24.337777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `0.027` n `230`; crypto_major avg `-0.0042` n `8`; equity avg `0.021` n `114`; fx avg `0.001` n `6`; index avg `0.0045` n `25`; metal avg `-0.0306` n `20`; unknown avg `0.0966` n `791`
- 1h: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0253` n `230`; crypto_major avg `-0.0738` n `8`; equity avg `-0.0045` n `114`; fx avg `-0.001` n `6`; index avg `-0.0063` n `25`; metal avg `0.0604` n `20`; unknown avg `0.0363` n `791`
- 4h: commodity avg `-0.146` n `12`; crypto_alt avg `-0.7087` n `230`; crypto_major avg `-0.6484` n `8`; equity avg `-0.0076` n `114`; fx avg `-0.0052` n `6`; index avg `0.0164` n `25`; metal avg `0.0034` n `20`; unknown avg `0.8019` n `791`
- 24h: commodity avg `-0.0625` n `12`; crypto_alt avg `-0.6293` n `230`; crypto_major avg `-0.3957` n `8`; equity avg `0.2687` n `114`; fx avg `-0.0052` n `6`; index avg `0.0414` n `25`; metal avg `0.0642` n `20`; unknown avg `-0.0011` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2108`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
