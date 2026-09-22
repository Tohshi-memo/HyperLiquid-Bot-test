# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T21:37:30.161542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `0.2862` n `234`; crypto_major avg `0.1857` n `8`; equity avg `0.0437` n `140`; fx avg `-0.0026` n `6`; index avg `0.0047` n `26`; metal avg `0.016` n `20`; unknown avg `-0.1051` n `944`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `0.1212` n `234`; crypto_major avg `-0.0229` n `8`; equity avg `0.015` n `140`; fx avg `0.0046` n `6`; index avg `0.0008` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.3753` n `942`
- 4h: commodity avg `-0.0333` n `12`; crypto_alt avg `0.7547` n `234`; crypto_major avg `0.066` n `8`; equity avg `0.3321` n `140`; fx avg `-0.0203` n `6`; index avg `0.0541` n `26`; metal avg `0.2592` n `20`; unknown avg `0.7983` n `906`
- 24h: commodity avg `0.1962` n `12`; crypto_alt avg `2.1753` n `234`; crypto_major avg `0.0093` n `8`; equity avg `0.873` n `140`; fx avg `-0.2999` n `6`; index avg `0.144` n `26`; metal avg `0.2783` n `20`; unknown avg `1.3686` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
