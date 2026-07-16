# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T14:22:30.400366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.134` n `12`; crypto_alt avg `0.0961` n `230`; crypto_major avg `0.0989` n `8`; equity avg `-0.2262` n `94`; fx avg `-0.0004` n `6`; index avg `-0.0097` n `25`; metal avg `-0.0121` n `20`; unknown avg `0.0519` n `768`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `0.2758` n `230`; crypto_major avg `0.3177` n `8`; equity avg `-0.788` n `94`; fx avg `0.0209` n `6`; index avg `0.0082` n `25`; metal avg `-0.0804` n `20`; unknown avg `0.0837` n `768`
- 4h: commodity avg `0.2485` n `12`; crypto_alt avg `0.5562` n `230`; crypto_major avg `0.294` n `8`; equity avg `-1.0879` n `94`; fx avg `0.0332` n `6`; index avg `-0.0733` n `25`; metal avg `-0.3119` n `20`; unknown avg `0.143` n `768`
- 24h: commodity avg `0.3047` n `12`; crypto_alt avg `-0.6318` n `230`; crypto_major avg `-1.3038` n `8`; equity avg `-2.6606` n `94`; fx avg `0.0091` n `6`; index avg `-0.2859` n `25`; metal avg `-0.496` n `20`; unknown avg `-0.0837` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
