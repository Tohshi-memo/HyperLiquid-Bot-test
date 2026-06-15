# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T10:52:32.208892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `0.0245` n `228`; crypto_major avg `0.0957` n `8`; equity avg `-0.0038` n `74`; fx avg `-0.0079` n `6`; index avg `0.0367` n `23`; metal avg `0.0041` n `18`; unknown avg `0.1732` n `689`
- 1h: commodity avg `0.2006` n `12`; crypto_alt avg `0.2613` n `228`; crypto_major avg `0.5062` n `8`; equity avg `-0.001` n `74`; fx avg `0.0038` n `6`; index avg `0.06` n `23`; metal avg `0.0233` n `18`; unknown avg `0.1274` n `689`
- 4h: commodity avg `-0.2159` n `12`; crypto_alt avg `0.135` n `228`; crypto_major avg `0.5022` n `8`; equity avg `-0.0254` n `74`; fx avg `0.0098` n `6`; index avg `0.0751` n `23`; metal avg `0.7112` n `18`; unknown avg `1.3018` n `689`
- 24h: commodity avg `-1.0158` n `12`; crypto_alt avg `3.1154` n `228`; crypto_major avg `3.2892` n `8`; equity avg `1.4375` n `74`; fx avg `0.0552` n `6`; index avg `0.944` n `23`; metal avg `2.3831` n `18`; unknown avg `1.4652` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
