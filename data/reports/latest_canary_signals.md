# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T13:22:32.663989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.2637` n `234`; crypto_major avg `-0.2216` n `8`; equity avg `-0.1297` n `140`; fx avg `0.0051` n `6`; index avg `0.0004` n `26`; metal avg `0.0296` n `20`; unknown avg `2.3543` n `944`
- 1h: commodity avg `-0.1044` n `12`; crypto_alt avg `0.9723` n `234`; crypto_major avg `0.337` n `8`; equity avg `-0.0991` n `140`; fx avg `0.0102` n `6`; index avg `0.0189` n `26`; metal avg `0.1019` n `20`; unknown avg `-0.0381` n `942`
- 4h: commodity avg `-0.2348` n `12`; crypto_alt avg `0.823` n `234`; crypto_major avg `0.4974` n `8`; equity avg `0.1174` n `140`; fx avg `0.034` n `6`; index avg `0.0539` n `26`; metal avg `0.2983` n `20`; unknown avg `2.6795` n `934`
- 24h: commodity avg `-0.414` n `12`; crypto_alt avg `0.966` n `234`; crypto_major avg `1.3595` n `8`; equity avg `0.6975` n `140`; fx avg `-0.2407` n `6`; index avg `0.2581` n `26`; metal avg `-0.1425` n `20`; unknown avg `1108.3941` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
