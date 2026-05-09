# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T14:52:14.466596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0754` n `12`; crypto_alt avg `0.0203` n `228`; crypto_major avg `-0.0514` n `8`; equity avg `0.0391` n `65`; fx avg `0.0021` n `5`; index avg `0.0021` n `23`; metal avg `-0.0241` n `18`; unknown avg `0.1299` n `376`
- 1h: commodity avg `0.226` n `12`; crypto_alt avg `-0.4185` n `228`; crypto_major avg `-0.359` n `8`; equity avg `-0.0368` n `65`; fx avg `0.0196` n `5`; index avg `-0.0483` n `23`; metal avg `-0.0563` n `18`; unknown avg `0.0903` n `376`
- 4h: commodity avg `0.3137` n `12`; crypto_alt avg `-0.8949` n `228`; crypto_major avg `-0.4598` n `8`; equity avg `0.0406` n `65`; fx avg `-0.0017` n `5`; index avg `-0.0171` n `23`; metal avg `-0.0582` n `18`; unknown avg `-0.4165` n `376`
- 24h: commodity avg `-0.188` n `12`; crypto_alt avg `1.4627` n `228`; crypto_major avg `1.1511` n `8`; equity avg `1.7589` n `65`; fx avg `0.0133` n `5`; index avg `0.6303` n `23`; metal avg `-0.2049` n `18`; unknown avg `0.3116` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
