# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T12:52:27.418075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `0.1245` n `228`; crypto_major avg `0.0735` n `8`; equity avg `-0.1926` n `74`; fx avg `-0.0014` n `6`; index avg `-0.0452` n `23`; metal avg `0.0235` n `18`; unknown avg `0.115` n `643`
- 1h: commodity avg `0.3706` n `12`; crypto_alt avg `0.2217` n `228`; crypto_major avg `0.1337` n `8`; equity avg `-0.6756` n `74`; fx avg `-0.0167` n `6`; index avg `-0.2511` n `23`; metal avg `-0.5428` n `18`; unknown avg `0.4029` n `643`
- 4h: commodity avg `0.868` n `12`; crypto_alt avg `0.602` n `228`; crypto_major avg `0.539` n `8`; equity avg `-0.1996` n `74`; fx avg `-0.0026` n `6`; index avg `0.0459` n `23`; metal avg `-0.5079` n `18`; unknown avg `1.4889` n `643`
- 24h: commodity avg `-2.2059` n `12`; crypto_alt avg `2.2947` n `228`; crypto_major avg `2.248` n `8`; equity avg `2.6383` n `74`; fx avg `-0.0214` n `6`; index avg `1.5621` n `23`; metal avg `2.8982` n `18`; unknown avg `1.7076` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
