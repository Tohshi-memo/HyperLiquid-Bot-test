# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T00:26:44.175786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0397` n `12`; crypto_alt avg `0.2296` n `230`; crypto_major avg `0.5049` n `8`; equity avg `0.1489` n `121`; fx avg `-0.0349` n `6`; index avg `0.0107` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.1291` n `793`
- 1h: commodity avg `-0.0429` n `12`; crypto_alt avg `0.4751` n `230`; crypto_major avg `0.6613` n `8`; equity avg `0.1622` n `121`; fx avg `-0.0818` n `6`; index avg `0.0204` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.1351` n `793`
- 4h: commodity avg `-0.0722` n `12`; crypto_alt avg `1.306` n `230`; crypto_major avg `1.2759` n `8`; equity avg `0.2696` n `121`; fx avg `-0.0706` n `6`; index avg `0.0391` n `25`; metal avg `0.0406` n `20`; unknown avg `-0.2798` n `792`
- 24h: commodity avg `0.2776` n `12`; crypto_alt avg `4.7343` n `230`; crypto_major avg `5.7784` n `8`; equity avg `-0.9637` n `121`; fx avg `0.1523` n `6`; index avg `-0.118` n `25`; metal avg `0.1534` n `20`; unknown avg `2.5495` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
