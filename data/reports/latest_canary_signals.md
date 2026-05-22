# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T09:07:16.502638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1344` n `12`; crypto_alt avg `0.052` n `228`; crypto_major avg `0.0534` n `8`; equity avg `-0.369` n `67`; fx avg `0.0085` n `6`; index avg `-0.1307` n `23`; metal avg `-0.1651` n `18`; unknown avg `-0.1054` n `386`
- 1h: commodity avg `0.1621` n `12`; crypto_alt avg `0.0111` n `228`; crypto_major avg `0.3589` n `8`; equity avg `-0.4892` n `67`; fx avg `0.0273` n `6`; index avg `-0.0651` n `23`; metal avg `-0.3056` n `18`; unknown avg `-0.2936` n `386`
- 4h: commodity avg `0.6176` n `12`; crypto_alt avg `-0.0511` n `228`; crypto_major avg `0.0841` n `8`; equity avg `-0.61` n `67`; fx avg `0.013` n `6`; index avg `-0.0671` n `23`; metal avg `-0.5936` n `18`; unknown avg `-0.2755` n `376`
- 24h: commodity avg `0.1926` n `12`; crypto_alt avg `1.3966` n `228`; crypto_major avg `-0.0041` n `8`; equity avg `0.7013` n `67`; fx avg `0.1515` n `6`; index avg `0.5415` n `23`; metal avg `0.0224` n `18`; unknown avg `1.0686` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0381`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0342`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0341`, n `668`, weak_sample_signal
