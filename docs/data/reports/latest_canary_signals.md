# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T10:52:36.672117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.04` n `12`; crypto_alt avg `-0.0655` n `228`; crypto_major avg `0.0907` n `8`; equity avg `-0.0441` n `74`; fx avg `0.0186` n `6`; index avg `-0.0069` n `23`; metal avg `0.1824` n `18`; unknown avg `-0.0366` n `644`
- 1h: commodity avg `0.0311` n `12`; crypto_alt avg `-0.068` n `228`; crypto_major avg `0.1656` n `8`; equity avg `0.0194` n `74`; fx avg `0.0012` n `6`; index avg `-0.0484` n `23`; metal avg `-0.0086` n `18`; unknown avg `-0.076` n `643`
- 4h: commodity avg `-0.0476` n `12`; crypto_alt avg `0.4837` n `228`; crypto_major avg `0.2502` n `8`; equity avg `0.095` n `74`; fx avg `0.0009` n `6`; index avg `-0.0495` n `23`; metal avg `0.1484` n `18`; unknown avg `0.4428` n `635`
- 24h: commodity avg `-0.0758` n `12`; crypto_alt avg `0.5804` n `228`; crypto_major avg `0.0702` n `8`; equity avg `-0.6295` n `74`; fx avg `0.0037` n `6`; index avg `0.6258` n `23`; metal avg `0.363` n `18`; unknown avg `30.4078` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
