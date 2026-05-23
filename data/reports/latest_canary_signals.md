# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T14:02:14.595055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1024` n `12`; crypto_alt avg `0.0414` n `228`; crypto_major avg `0.0228` n `8`; equity avg `0.0745` n `67`; fx avg `0.0044` n `6`; index avg `0.0188` n `23`; metal avg `0.007` n `18`; unknown avg `0.0068` n `396`
- 1h: commodity avg `-0.2066` n `12`; crypto_alt avg `0.2053` n `228`; crypto_major avg `0.117` n `8`; equity avg `0.1384` n `67`; fx avg `-0.0006` n `6`; index avg `0.0872` n `23`; metal avg `0.0449` n `18`; unknown avg `0.04` n `396`
- 4h: commodity avg `-0.1531` n `12`; crypto_alt avg `0.9688` n `228`; crypto_major avg `0.6125` n `8`; equity avg `0.3513` n `67`; fx avg `0.0075` n `6`; index avg `0.2788` n `23`; metal avg `0.0404` n `18`; unknown avg `-0.3617` n `396`
- 24h: commodity avg `-0.0069` n `12`; crypto_alt avg `-4.7414` n `228`; crypto_major avg `-3.7485` n `8`; equity avg `-1.365` n `67`; fx avg `0.0742` n `6`; index avg `-0.1098` n `23`; metal avg `-0.145` n `18`; unknown avg `-2.9397` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
