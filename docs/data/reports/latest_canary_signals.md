# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T04:37:23.596656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0569` n `12`; crypto_alt avg `-0.1146` n `228`; crypto_major avg `-0.0185` n `8`; equity avg `-0.0482` n `66`; fx avg `-0.0212` n `6`; index avg `-0.064` n `23`; metal avg `-0.0286` n `18`; unknown avg `-0.0505` n `384`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1485` n `228`; crypto_major avg `-0.0642` n `8`; equity avg `0.0255` n `66`; fx avg `-0.0062` n `6`; index avg `-0.0023` n `23`; metal avg `-0.1038` n `18`; unknown avg `-0.2975` n `384`
- 4h: commodity avg `-0.0589` n `12`; crypto_alt avg `0.2032` n `228`; crypto_major avg `0.1114` n `8`; equity avg `0.0758` n `66`; fx avg `-0.0502` n `6`; index avg `-0.2427` n `23`; metal avg `-0.6602` n `18`; unknown avg `-0.5408` n `384`
- 24h: commodity avg `0.6166` n `12`; crypto_alt avg `-1.1205` n `228`; crypto_major avg `-0.7802` n `8`; equity avg `0.1879` n `66`; fx avg `-0.1404` n `6`; index avg `-0.4805` n `23`; metal avg `-2.0202` n `18`; unknown avg `0.6097` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
