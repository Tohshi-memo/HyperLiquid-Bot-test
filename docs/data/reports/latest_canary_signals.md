# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T08:52:41.726825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `0.0038` n `228`; crypto_major avg `-0.0912` n `8`; equity avg `0.0276` n `74`; fx avg `-0.0024` n `6`; index avg `-0.013` n `23`; metal avg `-0.0189` n `18`; unknown avg `0.0126` n `689`
- 1h: commodity avg `-0.0229` n `12`; crypto_alt avg `0.2322` n `228`; crypto_major avg `0.1881` n `8`; equity avg `0.1704` n `74`; fx avg `-0.0294` n `6`; index avg `0.0566` n `23`; metal avg `0.4056` n `18`; unknown avg `0.7296` n `689`
- 4h: commodity avg `-0.2938` n `12`; crypto_alt avg `0.2855` n `228`; crypto_major avg `0.2074` n `8`; equity avg `0.2259` n `74`; fx avg `-0.0044` n `6`; index avg `0.228` n `23`; metal avg `0.2169` n `18`; unknown avg `0.8673` n `529`
- 24h: commodity avg `-0.9461` n `12`; crypto_alt avg `2.9612` n `228`; crypto_major avg `3.0023` n `8`; equity avg `1.9496` n `74`; fx avg `0.0294` n `6`; index avg `1.0197` n `23`; metal avg `2.2656` n `18`; unknown avg `1.5767` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
