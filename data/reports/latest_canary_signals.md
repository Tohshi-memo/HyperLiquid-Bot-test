# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T17:07:19.826443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2098` n `12`; crypto_alt avg `0.1309` n `228`; crypto_major avg `0.089` n `8`; equity avg `0.2388` n `66`; fx avg `0.0376` n `6`; index avg `0.1114` n `23`; metal avg `0.026` n `18`; unknown avg `0.0763` n `383`
- 1h: commodity avg `0.1536` n `12`; crypto_alt avg `0.7117` n `228`; crypto_major avg `0.5007` n `8`; equity avg `1.0392` n `66`; fx avg `-0.0289` n `6`; index avg `0.5906` n `23`; metal avg `0.2012` n `18`; unknown avg `0.0549` n `383`
- 4h: commodity avg `0.4436` n `12`; crypto_alt avg `0.1743` n `228`; crypto_major avg `0.3286` n `8`; equity avg `1.4606` n `66`; fx avg `-0.0633` n `6`; index avg `0.3803` n `23`; metal avg `-0.4149` n `18`; unknown avg `-0.2556` n `383`
- 24h: commodity avg `0.8028` n `12`; crypto_alt avg `0.8848` n `228`; crypto_major avg `0.8652` n `8`; equity avg `0.7136` n `66`; fx avg `-0.017` n `6`; index avg `-0.189` n `23`; metal avg `-1.9453` n `18`; unknown avg `-0.1601` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
