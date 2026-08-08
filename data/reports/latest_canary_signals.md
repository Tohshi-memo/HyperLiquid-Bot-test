# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T05:37:30.592194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.0532` n `230`; crypto_major avg `0.0524` n `8`; equity avg `-0.0167` n `112`; fx avg `-0.0065` n `6`; index avg `0.0084` n `25`; metal avg `-0.003` n `20`; unknown avg `0.7443` n `784`
- 1h: commodity avg `-0.0304` n `12`; crypto_alt avg `-0.0272` n `230`; crypto_major avg `-0.0108` n `8`; equity avg `-0.0437` n `112`; fx avg `-0.0018` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0188` n `20`; unknown avg `0.6801` n `783`
- 4h: commodity avg `-0.0321` n `12`; crypto_alt avg `0.3287` n `230`; crypto_major avg `0.3791` n `8`; equity avg `-0.127` n `112`; fx avg `-0.0084` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0439` n `20`; unknown avg `1.4519` n `783`
- 24h: commodity avg `-0.2708` n `12`; crypto_alt avg `0.1709` n `230`; crypto_major avg `1.0511` n `8`; equity avg `1.4434` n `112`; fx avg `-0.0732` n `6`; index avg `0.1554` n `25`; metal avg `0.2352` n `20`; unknown avg `0.0386` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
