# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T22:22:20.088533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.0775` n `228`; crypto_major avg `-0.1326` n `8`; equity avg `-0.0235` n `67`; fx avg `0.0091` n `6`; index avg `-0.0366` n `23`; metal avg `0.0226` n `18`; unknown avg `0.1609` n `419`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `-1.6082` n `228`; crypto_major avg `-0.9167` n `8`; equity avg `-0.1232` n `67`; fx avg `0.006` n `6`; index avg `-0.0402` n `23`; metal avg `0.1175` n `18`; unknown avg `0.6342` n `419`
- 4h: commodity avg `0.0828` n `12`; crypto_alt avg `-0.9603` n `228`; crypto_major avg `-0.4757` n `8`; equity avg `0.0568` n `67`; fx avg `0.0047` n `6`; index avg `0.1208` n `23`; metal avg `0.0994` n `18`; unknown avg `-0.0178` n `418`
- 24h: commodity avg `-1.2109` n `12`; crypto_alt avg `-1.7472` n `228`; crypto_major avg `-0.9012` n `8`; equity avg `-0.2833` n `67`; fx avg `-0.1002` n `6`; index avg `-0.3708` n `23`; metal avg `-1.2134` n `18`; unknown avg `-0.3242` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
