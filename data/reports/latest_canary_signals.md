# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T21:52:12.013990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.0205` n `228`; crypto_major avg `-0.0087` n `8`; equity avg `-0.0081` n `65`; fx avg `0.0` n `5`; index avg `0.0138` n `23`; metal avg `0.0376` n `18`; unknown avg `0.0227` n `376`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.0` n `228`; crypto_major avg `0.0416` n `8`; equity avg `0.0249` n `65`; fx avg `-0.0289` n `5`; index avg `0.0073` n `23`; metal avg `0.0698` n `18`; unknown avg `0.26` n `376`
- 4h: commodity avg `0.0261` n `12`; crypto_alt avg `0.0461` n `228`; crypto_major avg `0.0436` n `8`; equity avg `0.2519` n `65`; fx avg `-0.0117` n `5`; index avg `0.0806` n `23`; metal avg `0.1845` n `18`; unknown avg `0.2035` n `376`
- 24h: commodity avg `0.3753` n `12`; crypto_alt avg `0.148` n `228`; crypto_major avg `0.3158` n `8`; equity avg `0.6998` n `65`; fx avg `-0.0242` n `5`; index avg `0.38` n `23`; metal avg `0.1313` n `18`; unknown avg `0.4367` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
