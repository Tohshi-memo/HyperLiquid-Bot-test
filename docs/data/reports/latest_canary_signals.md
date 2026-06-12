# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T21:22:32.145390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1506` n `12`; crypto_alt avg `0.3271` n `228`; crypto_major avg `0.2154` n `8`; equity avg `0.042` n `74`; fx avg `-0.0004` n `6`; index avg `0.0186` n `23`; metal avg `-0.059` n `18`; unknown avg `51.6302` n `643`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `-0.0054` n `228`; crypto_major avg `0.0065` n `8`; equity avg `-0.0214` n `74`; fx avg `-0.0146` n `6`; index avg `-0.0012` n `23`; metal avg `-0.0616` n `18`; unknown avg `0.6243` n `643`
- 4h: commodity avg `-0.1267` n `12`; crypto_alt avg `-0.254` n `228`; crypto_major avg `-0.416` n `8`; equity avg `-0.5384` n `74`; fx avg `-0.0263` n `6`; index avg `-0.1241` n `23`; metal avg `0.1436` n `18`; unknown avg `-0.0173` n `643`
- 24h: commodity avg `-0.6511` n `12`; crypto_alt avg `-0.4907` n `228`; crypto_major avg `0.3749` n `8`; equity avg `-0.3633` n `74`; fx avg `-0.0687` n `6`; index avg `0.4724` n `23`; metal avg `0.4716` n `18`; unknown avg `40.6564` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
