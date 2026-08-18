# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T06:52:25.738736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0263` n `12`; crypto_alt avg `-0.1125` n `230`; crypto_major avg `-0.0901` n `8`; equity avg `0.0092` n `114`; fx avg `-0.0084` n `6`; index avg `0.0052` n `25`; metal avg `0.017` n `20`; unknown avg `0.0138` n `793`
- 1h: commodity avg `0.1093` n `12`; crypto_alt avg `0.3797` n `230`; crypto_major avg `0.3415` n `8`; equity avg `0.0851` n `114`; fx avg `0.0061` n `6`; index avg `0.0008` n `25`; metal avg `0.0548` n `20`; unknown avg `0.0491` n `761`
- 4h: commodity avg `0.0934` n `12`; crypto_alt avg `0.237` n `230`; crypto_major avg `0.4362` n `8`; equity avg `0.0107` n `114`; fx avg `0.0315` n `6`; index avg `-0.1032` n `25`; metal avg `0.0422` n `20`; unknown avg `0.0511` n `761`
- 24h: commodity avg `0.8144` n `12`; crypto_alt avg `-1.2469` n `230`; crypto_major avg `-0.001` n `8`; equity avg `-1.6038` n `114`; fx avg `-0.017` n `6`; index avg `-0.4369` n `25`; metal avg `-0.2082` n `20`; unknown avg `0.0089` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
