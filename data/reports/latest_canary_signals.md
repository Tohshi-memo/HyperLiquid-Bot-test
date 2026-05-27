# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T21:22:20.096761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `-0.0423` n `228`; crypto_major avg `-0.0496` n `8`; equity avg `0.0217` n `67`; fx avg `-0.023` n `6`; index avg `-0.0003` n `23`; metal avg `0.0087` n `18`; unknown avg `-0.0196` n `419`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.0695` n `228`; crypto_major avg `-0.22` n `8`; equity avg `-0.033` n `67`; fx avg `-0.0192` n `6`; index avg `0.0333` n `23`; metal avg `-0.0173` n `18`; unknown avg `0.2852` n `419`
- 4h: commodity avg `-0.2912` n `12`; crypto_alt avg `0.2042` n `228`; crypto_major avg `0.2376` n `8`; equity avg `0.4199` n `67`; fx avg `-0.013` n `6`; index avg `0.251` n `23`; metal avg `0.1318` n `18`; unknown avg `0.0095` n `418`
- 24h: commodity avg `-1.4923` n `12`; crypto_alt avg `-0.2764` n `228`; crypto_major avg `-0.0149` n `8`; equity avg `-0.152` n `67`; fx avg `-0.0961` n `6`; index avg `-0.3671` n `23`; metal avg `-1.2719` n `18`; unknown avg `-0.2112` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
