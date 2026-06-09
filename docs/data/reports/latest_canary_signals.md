# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T04:52:24.495474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.0216` n `228`; crypto_major avg `-0.0393` n `8`; equity avg `-0.1067` n `74`; fx avg `0.0077` n `6`; index avg `-0.0645` n `23`; metal avg `0.0383` n `18`; unknown avg `192.8842` n `517`
- 1h: commodity avg `0.0687` n `12`; crypto_alt avg `1.2885` n `228`; crypto_major avg `0.9783` n `8`; equity avg `0.3481` n `74`; fx avg `0.0066` n `6`; index avg `0.1517` n `23`; metal avg `-0.0363` n `18`; unknown avg `193.2981` n `517`
- 4h: commodity avg `-0.2476` n `12`; crypto_alt avg `1.2542` n `228`; crypto_major avg `1.1962` n `8`; equity avg `1.3028` n `74`; fx avg `-0.0028` n `6`; index avg `0.6824` n `23`; metal avg `0.3048` n `18`; unknown avg `-0.0277` n `517`
- 24h: commodity avg `-1.2559` n `12`; crypto_alt avg `0.7373` n `228`; crypto_major avg `1.229` n `8`; equity avg `2.3014` n `74`; fx avg `-0.3021` n `6`; index avg `1.0334` n `23`; metal avg `0.133` n `18`; unknown avg `-3.1099` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
