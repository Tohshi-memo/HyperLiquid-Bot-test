# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T12:52:28.351676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1964` n `12`; crypto_alt avg `0.2307` n `228`; crypto_major avg `0.0969` n `8`; equity avg `0.0701` n `69`; fx avg `-0.0019` n `6`; index avg `0.0396` n `23`; metal avg `-0.0745` n `18`; unknown avg `0.9722` n `422`
- 1h: commodity avg `-0.3415` n `12`; crypto_alt avg `0.0616` n `228`; crypto_major avg `-0.0955` n `8`; equity avg `-0.0455` n `69`; fx avg `-0.0113` n `6`; index avg `0.0158` n `23`; metal avg `-0.0496` n `18`; unknown avg `0.1658` n `422`
- 4h: commodity avg `-0.0955` n `12`; crypto_alt avg `0.4066` n `228`; crypto_major avg `-0.0038` n `8`; equity avg `-0.0367` n `69`; fx avg `0.0048` n `6`; index avg `0.0441` n `23`; metal avg `-0.154` n `18`; unknown avg `0.9342` n `422`
- 24h: commodity avg `-0.2759` n `12`; crypto_alt avg `0.3142` n `228`; crypto_major avg `-1.828` n `8`; equity avg `0.8694` n `69`; fx avg `0.1318` n `6`; index avg `0.1943` n `23`; metal avg `0.6088` n `18`; unknown avg `0.8774` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
