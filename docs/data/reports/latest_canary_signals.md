# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T14:37:18.839968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0885` n `12`; crypto_alt avg `0.0523` n `228`; crypto_major avg `0.0408` n `8`; equity avg `-0.0296` n `67`; fx avg `0.0007` n `6`; index avg `-0.081` n `23`; metal avg `0.0637` n `18`; unknown avg `0.2607` n `396`
- 1h: commodity avg `0.633` n `12`; crypto_alt avg `-0.762` n `228`; crypto_major avg `-0.8463` n `8`; equity avg `-0.4054` n `67`; fx avg `-0.0012` n `6`; index avg `-0.232` n `23`; metal avg `-0.357` n `18`; unknown avg `1.0004` n `396`
- 4h: commodity avg `0.8968` n `12`; crypto_alt avg `-1.281` n `228`; crypto_major avg `-0.7529` n `8`; equity avg `-0.3566` n `67`; fx avg `0.0176` n `6`; index avg `-0.3158` n `23`; metal avg `-0.6104` n `18`; unknown avg `1.6714` n `396`
- 24h: commodity avg `-1.0054` n `12`; crypto_alt avg `1.1277` n `228`; crypto_major avg `2.8234` n `8`; equity avg `1.8804` n `67`; fx avg `0.0824` n `6`; index avg `0.5259` n `23`; metal avg `0.6023` n `18`; unknown avg `1.4397` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
