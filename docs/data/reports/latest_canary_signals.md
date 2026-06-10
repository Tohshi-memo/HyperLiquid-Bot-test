# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T11:22:27.466185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `0.2093` n `228`; crypto_major avg `0.2546` n `8`; equity avg `0.176` n `74`; fx avg `-0.0016` n `6`; index avg `0.0665` n `23`; metal avg `0.187` n `18`; unknown avg `0.184` n `547`
- 1h: commodity avg `0.5616` n `12`; crypto_alt avg `-0.2418` n `228`; crypto_major avg `0.157` n `8`; equity avg `0.0445` n `74`; fx avg `-0.0328` n `6`; index avg `-0.0924` n `23`; metal avg `0.1046` n `18`; unknown avg `0.2347` n `547`
- 4h: commodity avg `0.826` n `12`; crypto_alt avg `-1.1106` n `228`; crypto_major avg `-0.5644` n `8`; equity avg `-0.8373` n `74`; fx avg `-0.0603` n `6`; index avg `-0.527` n `23`; metal avg `-0.3427` n `18`; unknown avg `0.3714` n `547`
- 24h: commodity avg `0.3012` n `12`; crypto_alt avg `-1.5773` n `228`; crypto_major avg `-3.2642` n `8`; equity avg `-4.376` n `74`; fx avg `-0.0697` n `6`; index avg `-2.5213` n `23`; metal avg `-3.5077` n `18`; unknown avg `0.5852` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
