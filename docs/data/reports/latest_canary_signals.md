# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T05:22:16.672548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `0.2856` n `228`; crypto_major avg `0.1977` n `8`; equity avg `0.0057` n `66`; fx avg `-0.0036` n `6`; index avg `-0.0197` n `23`; metal avg `0.0438` n `18`; unknown avg `1.2058` n `384`
- 1h: commodity avg `0.1134` n `12`; crypto_alt avg `0.6411` n `228`; crypto_major avg `0.4596` n `8`; equity avg `-0.0525` n `66`; fx avg `-0.0022` n `6`; index avg `-0.0057` n `23`; metal avg `0.2123` n `18`; unknown avg `1.1878` n `384`
- 4h: commodity avg `-0.1071` n `12`; crypto_alt avg `0.7939` n `228`; crypto_major avg `0.4034` n `8`; equity avg `-0.1401` n `66`; fx avg `-0.0138` n `6`; index avg `-0.139` n `23`; metal avg `-0.3228` n `18`; unknown avg `0.7757` n `384`
- 24h: commodity avg `0.528` n `12`; crypto_alt avg `0.0514` n `228`; crypto_major avg `-0.004` n `8`; equity avg `0.3112` n `66`; fx avg `-0.1242` n `6`; index avg `-0.5056` n `23`; metal avg `-1.7166` n `18`; unknown avg `2.0568` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0431`, n `668`, weak_sample_signal
