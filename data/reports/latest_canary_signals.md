# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T02:07:25.803548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `0.0218` n `230`; crypto_major avg `0.1706` n `8`; equity avg `0.0887` n `94`; fx avg `-0.0048` n `6`; index avg `0.0028` n `25`; metal avg `0.0095` n `20`; unknown avg `0.0681` n `768`
- 1h: commodity avg `-0.0533` n `12`; crypto_alt avg `-0.64` n `230`; crypto_major avg `-0.7115` n `8`; equity avg `-0.775` n `94`; fx avg `-0.0057` n `6`; index avg `-0.1006` n `25`; metal avg `-0.1558` n `20`; unknown avg `0.538` n `768`
- 4h: commodity avg `0.0023` n `12`; crypto_alt avg `-1.3375` n `230`; crypto_major avg `-1.2501` n `8`; equity avg `-1.6713` n `94`; fx avg `-0.0171` n `6`; index avg `-0.2766` n `25`; metal avg `-0.1272` n `20`; unknown avg `-0.2545` n `768`
- 24h: commodity avg `-0.1052` n `12`; crypto_alt avg `-2.1409` n `230`; crypto_major avg `-2.9095` n `8`; equity avg `-4.7013` n `94`; fx avg `-0.1825` n `6`; index avg `-0.5544` n `25`; metal avg `-0.7059` n `20`; unknown avg `-0.7049` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
