# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T21:07:27.578733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.0043` n `231`; crypto_major avg `-0.0396` n `8`; equity avg `-0.0037` n `127`; fx avg `0.0096` n `6`; index avg `-0.0043` n `26`; metal avg `0.0123` n `20`; unknown avg `-0.0423` n `793`
- 1h: commodity avg `0.0128` n `12`; crypto_alt avg `0.255` n `231`; crypto_major avg `0.1812` n `8`; equity avg `0.0803` n `127`; fx avg `-0.0337` n `6`; index avg `0.0101` n `26`; metal avg `0.0169` n `20`; unknown avg `-0.0862` n `793`
- 4h: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.1932` n `231`; crypto_major avg `-0.7173` n `8`; equity avg `0.0914` n `127`; fx avg `-0.0466` n `6`; index avg `0.0108` n `26`; metal avg `-0.1258` n `20`; unknown avg `-0.5698` n `793`
- 24h: commodity avg `-0.1029` n `12`; crypto_alt avg `-3.4087` n `231`; crypto_major avg `-3.7505` n `8`; equity avg `-2.239` n `127`; fx avg `-0.146` n `6`; index avg `-0.1936` n `26`; metal avg `-0.3468` n `20`; unknown avg `-0.7507` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
