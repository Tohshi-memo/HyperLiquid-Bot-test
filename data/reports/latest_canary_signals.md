# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T06:37:18.305005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.1682` n `228`; crypto_major avg `-0.1175` n `8`; equity avg `0.0509` n `67`; fx avg `-0.018` n `6`; index avg `-0.0433` n `23`; metal avg `-0.0155` n `18`; unknown avg `-0.0444` n `386`
- 1h: commodity avg `0.1559` n `12`; crypto_alt avg `-0.3154` n `228`; crypto_major avg `-0.2439` n `8`; equity avg `-0.0643` n `67`; fx avg `-0.0121` n `6`; index avg `-0.0444` n `23`; metal avg `-0.3532` n `18`; unknown avg `-0.2787` n `376`
- 4h: commodity avg `0.2063` n `12`; crypto_alt avg `-0.0367` n `228`; crypto_major avg `-0.3749` n `8`; equity avg `0.296` n `67`; fx avg `0.0652` n `6`; index avg `0.1483` n `23`; metal avg `0.1617` n `18`; unknown avg `-0.3651` n `376`
- 24h: commodity avg `-0.6673` n `12`; crypto_alt avg `1.7022` n `228`; crypto_major avg `0.2945` n `8`; equity avg `1.4861` n `66`; fx avg `0.0963` n `6`; index avg `0.7036` n `23`; metal avg `0.8069` n `18`; unknown avg `2.2322` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0437`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0426`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
