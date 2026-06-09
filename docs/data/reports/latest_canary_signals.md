# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T05:07:26.436847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `-0.072` n `228`; crypto_major avg `-0.2143` n `8`; equity avg `0.074` n `74`; fx avg `-0.0105` n `6`; index avg `0.0499` n `23`; metal avg `0.1585` n `18`; unknown avg `-0.3384` n `517`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `1.1826` n `228`; crypto_major avg `0.8206` n `8`; equity avg `0.3713` n `74`; fx avg `-0.0005` n `6`; index avg `0.1803` n `23`; metal avg `0.1306` n `18`; unknown avg `-0.2578` n `517`
- 4h: commodity avg `-0.1607` n `12`; crypto_alt avg `0.8939` n `228`; crypto_major avg `0.891` n `8`; equity avg `1.3607` n `74`; fx avg `0.0043` n `6`; index avg `0.7198` n `23`; metal avg `0.2406` n `18`; unknown avg `-0.3921` n `517`
- 24h: commodity avg `-1.3201` n `12`; crypto_alt avg `0.9958` n `228`; crypto_major avg `1.4985` n `8`; equity avg `2.5792` n `74`; fx avg `-0.3186` n `6`; index avg `1.202` n `23`; metal avg `0.4227` n `18`; unknown avg `-3.178` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
