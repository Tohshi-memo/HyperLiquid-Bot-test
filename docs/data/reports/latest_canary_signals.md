# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T16:37:54.505861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0786` n `12`; crypto_alt avg `-0.3159` n `228`; crypto_major avg `-0.3787` n `8`; equity avg `-0.0539` n `78`; fx avg `-0.0143` n `6`; index avg `0.0202` n `23`; metal avg `0.0018` n `18`; unknown avg `-0.4233` n `702`
- 1h: commodity avg `0.0968` n `12`; crypto_alt avg `-0.2089` n `228`; crypto_major avg `-0.4098` n `8`; equity avg `-0.0845` n `78`; fx avg `-0.0048` n `6`; index avg `0.0048` n `23`; metal avg `-0.0084` n `18`; unknown avg `-0.6702` n `702`
- 4h: commodity avg `0.0652` n `12`; crypto_alt avg `0.3477` n `228`; crypto_major avg `0.2616` n `8`; equity avg `-0.0063` n `78`; fx avg `-0.0164` n `6`; index avg `0.0003` n `23`; metal avg `0.0118` n `18`; unknown avg `-0.4675` n `702`
- 24h: commodity avg `0.1441` n `12`; crypto_alt avg `1.5532` n `228`; crypto_major avg `-0.0281` n `8`; equity avg `0.3252` n `78`; fx avg `0.0254` n `6`; index avg `0.0411` n `23`; metal avg `-0.0743` n `18`; unknown avg `-0.0615` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
