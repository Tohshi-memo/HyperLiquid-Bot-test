# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T07:22:17.875710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0416` n `12`; crypto_alt avg `0.1591` n `228`; crypto_major avg `0.0595` n `8`; equity avg `0.0006` n `67`; fx avg `0.0` n `6`; index avg `-0.0161` n `23`; metal avg `0.0164` n `18`; unknown avg `0.0084` n `386`
- 1h: commodity avg `-0.104` n `12`; crypto_alt avg `-0.1613` n `228`; crypto_major avg `-0.1905` n `8`; equity avg `-0.0214` n `67`; fx avg `0.0079` n `6`; index avg `-0.055` n `23`; metal avg `0.0521` n `18`; unknown avg `-0.2548` n `386`
- 4h: commodity avg `0.0402` n `12`; crypto_alt avg `-0.8616` n `228`; crypto_major avg `-0.573` n `8`; equity avg `-0.1452` n `67`; fx avg `0.0154` n `6`; index avg `-0.1423` n `23`; metal avg `0.0116` n `18`; unknown avg `-0.3856` n `376`
- 24h: commodity avg `-0.2676` n `12`; crypto_alt avg `-4.1639` n `228`; crypto_major avg `-2.7562` n `8`; equity avg `-1.9659` n `67`; fx avg `0.0753` n `6`; index avg `-0.2203` n `23`; metal avg `-0.6325` n `18`; unknown avg `-2.0944` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
