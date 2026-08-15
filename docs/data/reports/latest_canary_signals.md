# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T18:37:26.173931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `0.0574` n `230`; crypto_major avg `0.0077` n `8`; equity avg `0.0068` n `114`; fx avg `0.0018` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0084` n `20`; unknown avg `0.0552` n `791`
- 1h: commodity avg `0.0171` n `12`; crypto_alt avg `-0.1092` n `230`; crypto_major avg `-0.0956` n `8`; equity avg `0.0169` n `114`; fx avg `0.0035` n `6`; index avg `-0.002` n `25`; metal avg `0.0046` n `20`; unknown avg `0.0375` n `791`
- 4h: commodity avg `0.0524` n `12`; crypto_alt avg `0.2421` n `230`; crypto_major avg `0.1254` n `8`; equity avg `0.0441` n `114`; fx avg `0.0006` n `6`; index avg `0.0122` n `25`; metal avg `-0.0039` n `20`; unknown avg `5.0791` n `791`
- 24h: commodity avg `-0.1102` n `12`; crypto_alt avg `0.9024` n `230`; crypto_major avg `0.4959` n `8`; equity avg `0.3848` n `114`; fx avg `0.0284` n `6`; index avg `0.0387` n `25`; metal avg `0.0389` n `20`; unknown avg `0.0691` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
