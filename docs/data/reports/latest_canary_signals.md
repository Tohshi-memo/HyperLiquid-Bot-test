# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T07:07:18.898492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.057` n `12`; crypto_alt avg `-0.0578` n `228`; crypto_major avg `-0.1159` n `8`; equity avg `-0.0192` n `67`; fx avg `0.0069` n `6`; index avg `-0.0257` n `23`; metal avg `0.0234` n `18`; unknown avg `0.0326` n `386`
- 1h: commodity avg `-0.0721` n `12`; crypto_alt avg `-0.245` n `228`; crypto_major avg `-0.3631` n `8`; equity avg `-0.0378` n `67`; fx avg `0.0095` n `6`; index avg `-0.0321` n `23`; metal avg `0.0507` n `18`; unknown avg `-0.2861` n `386`
- 4h: commodity avg `0.1207` n `12`; crypto_alt avg `-0.8204` n `228`; crypto_major avg `-0.5633` n `8`; equity avg `-0.1745` n `67`; fx avg `0.0133` n `6`; index avg `-0.1293` n `23`; metal avg `0.015` n `18`; unknown avg `-0.3834` n `376`
- 24h: commodity avg `-0.2266` n `12`; crypto_alt avg `-3.8195` n `228`; crypto_major avg `-2.5584` n `8`; equity avg `-1.9232` n `67`; fx avg `0.0821` n `6`; index avg `-0.1839` n `23`; metal avg `-0.5829` n `18`; unknown avg `-2.0742` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
