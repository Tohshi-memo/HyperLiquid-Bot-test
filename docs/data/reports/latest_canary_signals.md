# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T20:07:24.163049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0409` n `12`; crypto_alt avg `0.1621` n `228`; crypto_major avg `0.1005` n `8`; equity avg `0.0127` n `69`; fx avg `0.0042` n `6`; index avg `0.0701` n `23`; metal avg `0.021` n `18`; unknown avg `0.6317` n `422`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.3791` n `228`; crypto_major avg `0.1275` n `8`; equity avg `0.2381` n `69`; fx avg `0.0133` n `6`; index avg `0.189` n `23`; metal avg `-0.01` n `18`; unknown avg `-0.0202` n `422`
- 4h: commodity avg `0.4122` n `12`; crypto_alt avg `0.2328` n `228`; crypto_major avg `-0.5424` n `8`; equity avg `0.0324` n `69`; fx avg `-0.0236` n `6`; index avg `0.1349` n `23`; metal avg `-0.4085` n `18`; unknown avg `-0.1999` n `422`
- 24h: commodity avg `-0.0763` n `12`; crypto_alt avg `-3.8113` n `228`; crypto_major avg `-4.5269` n `8`; equity avg `0.8099` n `69`; fx avg `0.0905` n `6`; index avg `0.6232` n `23`; metal avg `0.3793` n `18`; unknown avg `-0.2995` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
