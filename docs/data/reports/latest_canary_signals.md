# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T05:22:29.417105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `-0.3381` n `230`; crypto_major avg `-0.2172` n `8`; equity avg `-0.1624` n `98`; fx avg `-0.0023` n `6`; index avg `-0.0433` n `25`; metal avg `-0.0523` n `20`; unknown avg `0.117` n `769`
- 1h: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.4425` n `230`; crypto_major avg `-0.3305` n `8`; equity avg `-0.0732` n `98`; fx avg `-0.007` n `6`; index avg `0.0091` n `25`; metal avg `-0.0641` n `20`; unknown avg `1.4712` n `769`
- 4h: commodity avg `-0.0137` n `12`; crypto_alt avg `-0.8156` n `230`; crypto_major avg `-0.5847` n `8`; equity avg `-0.3734` n `98`; fx avg `-0.034` n `6`; index avg `-0.0813` n `25`; metal avg `-0.0113` n `20`; unknown avg `-0.4721` n `769`
- 24h: commodity avg `-0.0586` n `12`; crypto_alt avg `-0.8521` n `230`; crypto_major avg `-0.5829` n `8`; equity avg `0.0617` n `97`; fx avg `-0.0252` n `6`; index avg `0.0078` n `25`; metal avg `0.0139` n `20`; unknown avg `-0.0803` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.097`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0961`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0877`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0832`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0782`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
