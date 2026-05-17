# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T11:37:17.562949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.012` n `228`; crypto_major avg `0.0205` n `8`; equity avg `0.02` n `65`; fx avg `-0.0001` n `5`; index avg `-0.0005` n `23`; metal avg `-0.0023` n `18`; unknown avg `-0.0246` n `383`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.3738` n `228`; crypto_major avg `-0.2336` n `8`; equity avg `0.0348` n `65`; fx avg `0.0018` n `5`; index avg `0.0037` n `23`; metal avg `-0.0336` n `18`; unknown avg `-0.1627` n `383`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `-0.1858` n `228`; crypto_major avg `0.2424` n `8`; equity avg `0.2726` n `65`; fx avg `-0.0005` n `5`; index avg `0.1441` n `23`; metal avg `-0.0628` n `18`; unknown avg `-0.0614` n `383`
- 24h: commodity avg `1.7316` n `12`; crypto_alt avg `-8.9928` n `228`; crypto_major avg `-2.268` n `8`; equity avg `-2.6041` n `65`; fx avg `-0.167` n `5`; index avg `-1.6657` n `23`; metal avg `-5.8624` n `18`; unknown avg `550.0758` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
