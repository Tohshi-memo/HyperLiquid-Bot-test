# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T02:37:28.285664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0447` n `12`; crypto_alt avg `0.0188` n `228`; crypto_major avg `0.0234` n `8`; equity avg `0.0887` n `78`; fx avg `-0.0039` n `6`; index avg `0.0167` n `23`; metal avg `-0.003` n `18`; unknown avg `0.0481` n `687`
- 1h: commodity avg `0.1382` n `12`; crypto_alt avg `-0.3819` n `228`; crypto_major avg `-0.2858` n `8`; equity avg `0.0378` n `78`; fx avg `-0.003` n `6`; index avg `0.0258` n `23`; metal avg `-0.0029` n `18`; unknown avg `0.0663` n `687`
- 4h: commodity avg `-0.056` n `12`; crypto_alt avg `-0.1169` n `228`; crypto_major avg `-0.0499` n `8`; equity avg `0.2253` n `78`; fx avg `0.0362` n `6`; index avg `0.0829` n `23`; metal avg `-0.0281` n `18`; unknown avg `-0.6964` n `671`
- 24h: commodity avg `0.3989` n `12`; crypto_alt avg `-3.7822` n `228`; crypto_major avg `-4.574` n `8`; equity avg `0.95` n `78`; fx avg `-0.087` n `6`; index avg `0.2946` n `23`; metal avg `-4.1342` n `18`; unknown avg `-0.6983` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
