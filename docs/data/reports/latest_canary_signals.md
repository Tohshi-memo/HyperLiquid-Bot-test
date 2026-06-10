# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T00:37:23.740445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0929` n `12`; crypto_alt avg `-0.2877` n `228`; crypto_major avg `-0.3542` n `8`; equity avg `-0.2738` n `74`; fx avg `0.0392` n `6`; index avg `-0.1738` n `23`; metal avg `-0.5739` n `18`; unknown avg `-0.1867` n `547`
- 1h: commodity avg `0.318` n `12`; crypto_alt avg `-0.0586` n `228`; crypto_major avg `-0.071` n `8`; equity avg `0.3413` n `74`; fx avg `-0.0601` n `6`; index avg `0.0193` n `23`; metal avg `-0.4383` n `18`; unknown avg `-0.1192` n `547`
- 4h: commodity avg `0.536` n `12`; crypto_alt avg `-0.8844` n `228`; crypto_major avg `-1.1526` n `8`; equity avg `-0.4338` n `74`; fx avg `-0.0688` n `6`; index avg `-0.234` n `23`; metal avg `-1.0699` n `18`; unknown avg `-0.4078` n `547`
- 24h: commodity avg `-0.2126` n `12`; crypto_alt avg `0.098` n `228`; crypto_major avg `-2.0799` n `8`; equity avg `-1.5657` n `74`; fx avg `0.0526` n `6`; index avg `-0.6662` n `23`; metal avg `-2.0654` n `18`; unknown avg `-0.146` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0387`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0352`, n `668`, weak_sample_signal
