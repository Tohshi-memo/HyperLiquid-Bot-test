# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T17:07:13.393494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.2185` n `228`; crypto_major avg `-0.0531` n `8`; equity avg `-0.1734` n `65`; fx avg `0.011` n `5`; index avg `-0.0324` n `23`; metal avg `-0.0276` n `18`; unknown avg `-0.0174` n `384`
- 1h: commodity avg `-0.0321` n `12`; crypto_alt avg `-0.4517` n `228`; crypto_major avg `-0.1974` n `8`; equity avg `-0.1246` n `65`; fx avg `0.0116` n `5`; index avg `-0.0655` n `23`; metal avg `-0.0223` n `18`; unknown avg `-0.0971` n `384`
- 4h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.5176` n `228`; crypto_major avg `-0.3983` n `8`; equity avg `-0.175` n `65`; fx avg `0.0322` n `5`; index avg `0.0045` n `23`; metal avg `-0.0135` n `18`; unknown avg `-0.1425` n `383`
- 24h: commodity avg `1.777` n `12`; crypto_alt avg `-9.5519` n `228`; crypto_major avg `-2.5727` n `8`; equity avg `-2.6979` n `65`; fx avg `-0.1543` n `5`; index avg `-1.6444` n `23`; metal avg `-5.8495` n `18`; unknown avg `549.9597` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
