# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T08:52:15.588456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0994` n `12`; crypto_alt avg `0.0951` n `228`; crypto_major avg `-0.0626` n `8`; equity avg `0.1133` n `67`; fx avg `-0.0067` n `6`; index avg `0.0292` n `23`; metal avg `0.0504` n `18`; unknown avg `0.0706` n `417`
- 1h: commodity avg `0.2892` n `12`; crypto_alt avg `0.1068` n `228`; crypto_major avg `-0.1036` n `8`; equity avg `0.262` n `67`; fx avg `0.0161` n `6`; index avg `0.0372` n `23`; metal avg `-0.1177` n `18`; unknown avg `-0.0289` n `417`
- 4h: commodity avg `0.7874` n `12`; crypto_alt avg `0.1882` n `228`; crypto_major avg `-0.0745` n `8`; equity avg `0.0405` n `67`; fx avg `-0.0147` n `6`; index avg `-0.0386` n `23`; metal avg `-0.1429` n `18`; unknown avg `0.363` n `397`
- 24h: commodity avg `1.0073` n `12`; crypto_alt avg `-0.809` n `228`; crypto_major avg `-1.6124` n `8`; equity avg `-0.4926` n `67`; fx avg `-0.1023` n `6`; index avg `-0.0697` n `23`; metal avg `-0.6002` n `18`; unknown avg `0.0247` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
