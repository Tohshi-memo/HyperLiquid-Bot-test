# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T07:22:19.224824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.35` n `12`; crypto_alt avg `-0.2585` n `228`; crypto_major avg `-0.2081` n `8`; equity avg `-0.0751` n `67`; fx avg `0.0232` n `6`; index avg `-0.0955` n `23`; metal avg `-0.2245` n `18`; unknown avg `-0.007` n `397`
- 1h: commodity avg `0.3696` n `12`; crypto_alt avg `0.1494` n `228`; crypto_major avg `-0.0026` n `8`; equity avg `-0.0252` n `67`; fx avg `0.0293` n `6`; index avg `-0.0166` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.1659` n `397`
- 4h: commodity avg `0.3801` n `12`; crypto_alt avg `1.0062` n `228`; crypto_major avg `0.6127` n `8`; equity avg `0.0933` n `67`; fx avg `0.0628` n `6`; index avg `0.0488` n `23`; metal avg `-0.2211` n `18`; unknown avg `0.1405` n `387`
- 24h: commodity avg `0.246` n `12`; crypto_alt avg `0.0124` n `228`; crypto_major avg `-0.0011` n `8`; equity avg `0.3395` n `67`; fx avg `-0.0093` n `6`; index avg `-0.173` n `23`; metal avg `0.2887` n `18`; unknown avg `0.0533` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
