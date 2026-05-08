# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T14:07:12.696497+00:00`
- Correlation status: `ready`
- Asset price records: `652`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2023` n `12`; crypto_alt avg `0.1759` n `228`; crypto_major avg `0.181` n `8`; equity avg `0.3267` n `65`; fx avg `-0.0016` n `5`; index avg `-0.0153` n `23`; metal avg `-0.3314` n `18`; unknown avg `-0.0619` n `375`
- 1h: commodity avg `0.0178` n `12`; crypto_alt avg `0.1084` n `228`; crypto_major avg `0.0955` n `8`; equity avg `0.7348` n `65`; fx avg `-0.0165` n `5`; index avg `0.3607` n `23`; metal avg `0.0628` n `18`; unknown avg `0.3386` n `375`
- 4h: commodity avg `0.0243` n `12`; crypto_alt avg `0.0414` n `228`; crypto_major avg `-0.0456` n `8`; equity avg `0.9405` n `65`; fx avg `-0.0631` n `5`; index avg `0.507` n `23`; metal avg `0.0599` n `18`; unknown avg `0.0193` n `375`
- 24h: commodity avg `2.3159` n `12`; crypto_alt avg `1.2219` n `228`; crypto_major avg `-0.705` n `8`; equity avg `0.9364` n `65`; fx avg `0.2087` n `5`; index avg `0.6074` n `23`; metal avg `-0.5883` n `18`; unknown avg `-0.1181` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1232`, n `644`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1198`, n `644`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `648`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `648`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `648`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.095`, n `644`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `648`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `644`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `648`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0662`, n `648`, weak_sample_signal
