# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T18:07:29.573340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1284` n `12`; crypto_alt avg `0.1745` n `228`; crypto_major avg `0.1627` n `8`; equity avg `-0.0161` n `73`; fx avg `0.0082` n `6`; index avg `0.0133` n `23`; metal avg `-0.0632` n `18`; unknown avg `-0.1538` n `419`
- 1h: commodity avg `-0.0356` n `12`; crypto_alt avg `1.0159` n `228`; crypto_major avg `0.8743` n `8`; equity avg `0.4672` n `73`; fx avg `0.0154` n `6`; index avg `0.0671` n `23`; metal avg `-0.2258` n `18`; unknown avg `0.2639` n `419`
- 4h: commodity avg `0.4408` n `12`; crypto_alt avg `-0.5868` n `228`; crypto_major avg `-0.5376` n `8`; equity avg `-0.416` n `73`; fx avg `0.0141` n `6`; index avg `-0.0587` n `23`; metal avg `-0.6258` n `18`; unknown avg `-0.031` n `419`
- 24h: commodity avg `0.8186` n `12`; crypto_alt avg `0.1852` n `228`; crypto_major avg `-2.4578` n `8`; equity avg `-1.6745` n `72`; fx avg `0.0493` n `6`; index avg `-0.0748` n `23`; metal avg `-1.9363` n `18`; unknown avg `0.3575` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
