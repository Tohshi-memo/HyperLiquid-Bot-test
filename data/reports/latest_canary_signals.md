# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T15:32:30.403749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `0.0899` n `228`; crypto_major avg `0.0011` n `8`; equity avg `0.0082` n `65`; fx avg `0.0` n `5`; index avg `0.0208` n `23`; metal avg `-0.0024` n `18`; unknown avg `0.0074` n `384`
- 1h: commodity avg `0.0393` n `12`; crypto_alt avg `0.2023` n `228`; crypto_major avg `0.1914` n `8`; equity avg `0.0175` n `65`; fx avg `-0.0009` n `5`; index avg `0.0535` n `23`; metal avg `0.0274` n `18`; unknown avg `-0.0123` n `383`
- 4h: commodity avg `0.0087` n `12`; crypto_alt avg `-0.2776` n `228`; crypto_major avg `-0.2046` n `8`; equity avg `0.0081` n `65`; fx avg `0.0013` n `5`; index avg `0.0706` n `23`; metal avg `0.0253` n `18`; unknown avg `-0.0077` n `383`
- 24h: commodity avg `1.7472` n `12`; crypto_alt avg `-9.233` n `228`; crypto_major avg `-2.4505` n `8`; equity avg `-2.6014` n `65`; fx avg `-0.1657` n `5`; index avg `-1.5969` n `23`; metal avg `-5.8376` n `18`; unknown avg `550.0138` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
