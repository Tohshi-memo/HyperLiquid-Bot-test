# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T18:07:16.012895+00:00`
- Correlation status: `ready`
- Asset price records: `668`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2805` n `12`; crypto_alt avg `0.094` n `228`; crypto_major avg `0.0681` n `8`; equity avg `0.2072` n `65`; fx avg `0.0073` n `5`; index avg `0.141` n `23`; metal avg `0.2276` n `18`; unknown avg `0.327` n `375`
- 1h: commodity avg `-0.321` n `12`; crypto_alt avg `0.6622` n `228`; crypto_major avg `0.8233` n `8`; equity avg `0.4247` n `65`; fx avg `0.0099` n `5`; index avg `0.2778` n `23`; metal avg `0.357` n `18`; unknown avg `0.2949` n `375`
- 4h: commodity avg `-0.0997` n `12`; crypto_alt avg `2.0622` n `228`; crypto_major avg `1.3634` n `8`; equity avg `0.5914` n `65`; fx avg `0.0084` n `5`; index avg `0.3913` n `23`; metal avg `0.175` n `18`; unknown avg `0.2471` n `375`
- 24h: commodity avg `0.3698` n `12`; crypto_alt avg `2.8248` n `228`; crypto_major avg `0.8346` n `8`; equity avg `2.6359` n `65`; fx avg `0.1842` n `5`; index avg `1.3777` n `23`; metal avg `0.5941` n `18`; unknown avg `0.4952` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1213`, n `660`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.117`, n `660`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `664`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `660`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.096`, n `664`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0943`, n `660`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `664`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `664`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `664`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `660`, weak_sample_signal
