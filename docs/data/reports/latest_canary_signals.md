# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T06:37:18.628017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `0.261` n `228`; crypto_major avg `0.1814` n `8`; equity avg `-0.0355` n `67`; fx avg `0.0081` n `6`; index avg `0.0334` n `23`; metal avg `0.0455` n `18`; unknown avg `0.0696` n `397`
- 1h: commodity avg `0.2574` n `12`; crypto_alt avg `0.0742` n `228`; crypto_major avg `0.0333` n `8`; equity avg `-0.1679` n `67`; fx avg `0.0301` n `6`; index avg `0.0479` n `23`; metal avg `-0.156` n `18`; unknown avg `0.9645` n `387`
- 4h: commodity avg `-0.2384` n `12`; crypto_alt avg `0.9999` n `228`; crypto_major avg `0.6872` n `8`; equity avg `0.2518` n `67`; fx avg `0.015` n `6`; index avg `0.1641` n `23`; metal avg `-0.2381` n `18`; unknown avg `1.2313` n `386`
- 24h: commodity avg `0.2991` n `12`; crypto_alt avg `0.285` n `228`; crypto_major avg `0.4108` n `8`; equity avg `0.4723` n `67`; fx avg `-0.0247` n `6`; index avg `-0.0611` n `23`; metal avg `0.3033` n `18`; unknown avg `-0.1514` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
