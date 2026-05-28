# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T10:37:27.812847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0829` n `12`; crypto_alt avg `0.1042` n `228`; crypto_major avg `0.1295` n `8`; equity avg `-0.0184` n `67`; fx avg `0.0104` n `6`; index avg `-0.0202` n `23`; metal avg `-0.1368` n `18`; unknown avg `0.1603` n `419`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.0601` n `228`; crypto_major avg `0.0085` n `8`; equity avg `-0.1717` n `67`; fx avg `-0.0106` n `6`; index avg `-0.1046` n `23`; metal avg `-0.1667` n `18`; unknown avg `0.1481` n `419`
- 4h: commodity avg `-0.2115` n `12`; crypto_alt avg `0.5519` n `228`; crypto_major avg `0.6502` n `8`; equity avg `0.0936` n `67`; fx avg `-0.0011` n `6`; index avg `0.021` n `23`; metal avg `0.0337` n `18`; unknown avg `0.3633` n `419`
- 24h: commodity avg `0.3446` n `12`; crypto_alt avg `-4.76` n `228`; crypto_major avg `-3.7506` n `8`; equity avg `-1.7308` n `67`; fx avg `-0.0841` n `6`; index avg `-1.1471` n `23`; metal avg `-1.7149` n `18`; unknown avg `-1.4394` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
