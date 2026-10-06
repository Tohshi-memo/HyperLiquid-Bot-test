# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T10:52:32.020123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `13`; crypto_alt avg `0.1216` n `235`; crypto_major avg `0.19` n `8`; equity avg `0.0472` n `150`; fx avg `-0.0` n `6`; index avg `0.0136` n `26`; metal avg `-0.015` n `20`; unknown avg `1.2781` n `1074`
- 1h: commodity avg `-0.0728` n `13`; crypto_alt avg `0.4063` n `235`; crypto_major avg `0.3254` n `8`; equity avg `0.1433` n `150`; fx avg `0.0048` n `6`; index avg `0.0279` n `26`; metal avg `0.0095` n `20`; unknown avg `1.1548` n `1072`
- 4h: commodity avg `-0.3087` n `13`; crypto_alt avg `0.816` n `235`; crypto_major avg `0.6835` n `8`; equity avg `0.2449` n `149`; fx avg `0.051` n `6`; index avg `0.0503` n `26`; metal avg `0.0898` n `20`; unknown avg `1.4362` n `992`
- 24h: commodity avg `-0.8151` n `13`; crypto_alt avg `-0.4608` n `235`; crypto_major avg `-0.1909` n `8`; equity avg `0.682` n `149`; fx avg `0.0434` n `6`; index avg `0.2474` n `26`; metal avg `-0.0857` n `20`; unknown avg `1.5471` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
