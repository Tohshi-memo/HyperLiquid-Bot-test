# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T11:22:50.168600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `-0.3681` n `228`; crypto_major avg `-0.2124` n `8`; equity avg `-0.038` n `88`; fx avg `-0.0064` n `6`; index avg `-0.0067` n `23`; metal avg `-0.004` n `20`; unknown avg `-0.055` n `765`
- 1h: commodity avg `-0.0546` n `12`; crypto_alt avg `-0.3366` n `228`; crypto_major avg `-0.0834` n `8`; equity avg `0.1594` n `88`; fx avg `-0.0078` n `6`; index avg `0.0481` n `23`; metal avg `0.0952` n `20`; unknown avg `-0.3046` n `765`
- 4h: commodity avg `0.1458` n `12`; crypto_alt avg `-0.7217` n `228`; crypto_major avg `-0.2938` n `8`; equity avg `0.0084` n `88`; fx avg `-0.0055` n `6`; index avg `-0.002` n `23`; metal avg `0.1064` n `20`; unknown avg `0.3694` n `765`
- 24h: commodity avg `0.029` n `12`; crypto_alt avg `-0.9118` n `228`; crypto_major avg `0.4446` n `8`; equity avg `1.581` n `88`; fx avg `0.1208` n `6`; index avg `0.1575` n `23`; metal avg `0.4052` n `20`; unknown avg `9.0868` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
