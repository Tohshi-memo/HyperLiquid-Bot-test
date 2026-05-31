# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T03:52:20.890314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `0.046` n `228`; crypto_major avg `0.0109` n `8`; equity avg `-0.013` n `69`; fx avg `0.0037` n `6`; index avg `-0.0262` n `23`; metal avg `0.0005` n `18`; unknown avg `-0.1188` n `421`
- 1h: commodity avg `-0.1104` n `12`; crypto_alt avg `0.3126` n `228`; crypto_major avg `0.2013` n `8`; equity avg `0.0744` n `69`; fx avg `0.0029` n `6`; index avg `0.0262` n `23`; metal avg `0.0019` n `18`; unknown avg `-0.3254` n `421`
- 4h: commodity avg `0.0374` n `12`; crypto_alt avg `0.8086` n `228`; crypto_major avg `0.8451` n `8`; equity avg `0.1942` n `69`; fx avg `0.0422` n `6`; index avg `-0.0352` n `23`; metal avg `-0.0429` n `18`; unknown avg `0.7267` n `419`
- 24h: commodity avg `-0.1684` n `12`; crypto_alt avg `0.5427` n `228`; crypto_major avg `2.452` n `8`; equity avg `1.0299` n `69`; fx avg `0.0474` n `6`; index avg `0.0955` n `23`; metal avg `-0.0492` n `18`; unknown avg `1.5439` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
