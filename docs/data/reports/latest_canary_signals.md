# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T23:22:28.399342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `0.0931` n `228`; crypto_major avg `0.1007` n `8`; equity avg `-0.0912` n `78`; fx avg `-0.0068` n `6`; index avg `-0.0015` n `23`; metal avg `-0.0262` n `18`; unknown avg `-0.0536` n `702`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.1748` n `228`; crypto_major avg `-0.1275` n `8`; equity avg `-0.2589` n `78`; fx avg `0.009` n `6`; index avg `-0.0353` n `23`; metal avg `0.1001` n `18`; unknown avg `1.6417` n `702`
- 4h: commodity avg `-0.1631` n `12`; crypto_alt avg `-1.3671` n `228`; crypto_major avg `-1.0028` n `8`; equity avg `-0.518` n `78`; fx avg `-0.0527` n `6`; index avg `-0.112` n `23`; metal avg `0.0128` n `18`; unknown avg `0.5451` n `702`
- 24h: commodity avg `0.1261` n `12`; crypto_alt avg `-0.5632` n `228`; crypto_major avg `-1.4689` n `8`; equity avg `-0.4279` n `78`; fx avg `-0.1254` n `6`; index avg `-0.1367` n `23`; metal avg `-0.083` n `18`; unknown avg `0.5742` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
