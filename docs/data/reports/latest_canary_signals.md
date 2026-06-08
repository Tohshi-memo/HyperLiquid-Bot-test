# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T19:22:22.106752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `0.1196` n `228`; crypto_major avg `0.1381` n `8`; equity avg `-0.3072` n `74`; fx avg `-0.0008` n `6`; index avg `-0.2625` n `23`; metal avg `-0.1107` n `18`; unknown avg `-0.0619` n `517`
- 1h: commodity avg `-0.0963` n `12`; crypto_alt avg `-0.0423` n `228`; crypto_major avg `0.159` n `8`; equity avg `-0.6164` n `74`; fx avg `-0.0298` n `6`; index avg `-0.3921` n `23`; metal avg `-0.4174` n `18`; unknown avg `-0.0027` n `517`
- 4h: commodity avg `-0.131` n `12`; crypto_alt avg `0.0795` n `228`; crypto_major avg `-0.2053` n `8`; equity avg `-0.889` n `74`; fx avg `-0.0475` n `6`; index avg `-0.6244` n `23`; metal avg `-0.3874` n `18`; unknown avg `-0.0172` n `517`
- 24h: commodity avg `-1.2897` n `12`; crypto_alt avg `4.3663` n `228`; crypto_major avg `4.6455` n `8`; equity avg `2.3751` n `74`; fx avg `-0.3172` n `6`; index avg `0.8448` n `23`; metal avg `-0.0356` n `18`; unknown avg `-1.6552` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
