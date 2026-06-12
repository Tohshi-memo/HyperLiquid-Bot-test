# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T19:52:34.605507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.4049` n `228`; crypto_major avg `-0.3886` n `8`; equity avg `-0.1013` n `74`; fx avg `-0.0153` n `6`; index avg `-0.0429` n `23`; metal avg `-0.0075` n `18`; unknown avg `0.0554` n `643`
- 1h: commodity avg `0.2401` n `12`; crypto_alt avg `-0.1513` n `228`; crypto_major avg `-0.5113` n `8`; equity avg `-0.3788` n `74`; fx avg `-0.0261` n `6`; index avg `-0.1717` n `23`; metal avg `-0.2074` n `18`; unknown avg `-0.0755` n `643`
- 4h: commodity avg `0.1161` n `12`; crypto_alt avg `-0.5569` n `228`; crypto_major avg `-0.3509` n `8`; equity avg `0.0254` n `74`; fx avg `-0.0205` n `6`; index avg `0.0105` n `23`; metal avg `0.2261` n `18`; unknown avg `-0.3517` n `643`
- 24h: commodity avg `-0.5534` n `12`; crypto_alt avg `-0.2091` n `228`; crypto_major avg `0.1722` n `8`; equity avg `-0.3417` n `74`; fx avg `0.0197` n `6`; index avg `0.4322` n `23`; metal avg `0.1896` n `18`; unknown avg `39.7394` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
