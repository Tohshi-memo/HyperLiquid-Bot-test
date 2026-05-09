# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T11:15:01.362064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `-0.044` n `228`; crypto_major avg `0.0419` n `8`; equity avg `-0.0046` n `65`; fx avg `0.0025` n `5`; index avg `0.0066` n `23`; metal avg `0.0071` n `18`; unknown avg `0.2803` n `376`
- 1h: commodity avg `0.0338` n `12`; crypto_alt avg `0.3272` n `228`; crypto_major avg `0.1679` n `8`; equity avg `0.0324` n `65`; fx avg `0.0055` n `5`; index avg `-0.0081` n `23`; metal avg `0.0016` n `18`; unknown avg `0.0565` n `376`
- 4h: commodity avg `0.0177` n `12`; crypto_alt avg `-0.4513` n `228`; crypto_major avg `-0.2303` n `8`; equity avg `0.0878` n `65`; fx avg `0.0096` n `5`; index avg `-0.0144` n `23`; metal avg `-0.0456` n `18`; unknown avg `-0.1893` n `376`
- 24h: commodity avg `-0.1493` n `12`; crypto_alt avg `3.0929` n `228`; crypto_major avg `1.919` n `8`; equity avg `2.8756` n `65`; fx avg `0.0037` n `5`; index avg `1.1481` n `23`; metal avg `-0.1995` n `18`; unknown avg `0.7744` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
