# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T21:52:25.926234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.0557` n `231`; crypto_major avg `-0.0652` n `8`; equity avg `-0.0333` n `127`; fx avg `-0.0055` n `6`; index avg `0.004` n `26`; metal avg `0.006` n `20`; unknown avg `-0.061` n `792`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `-0.0204` n `231`; crypto_major avg `-0.1975` n `8`; equity avg `-0.2424` n `127`; fx avg `-0.0123` n `6`; index avg `0.0066` n `26`; metal avg `-0.0146` n `20`; unknown avg `0.0874` n `792`
- 4h: commodity avg `-0.0962` n `12`; crypto_alt avg `-0.5529` n `231`; crypto_major avg `-0.6119` n `8`; equity avg `-0.1826` n `127`; fx avg `-0.0074` n `6`; index avg `0.0302` n `26`; metal avg `-0.0231` n `20`; unknown avg `0.0232` n `792`
- 24h: commodity avg `0.3603` n `12`; crypto_alt avg `1.8397` n `231`; crypto_major avg `2.7508` n `8`; equity avg `-0.2043` n `127`; fx avg `-0.0464` n `6`; index avg `-0.0478` n `26`; metal avg `0.194` n `20`; unknown avg `0.864` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
