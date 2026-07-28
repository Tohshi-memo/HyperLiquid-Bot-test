# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T12:07:51.094721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `0.0221` n `230`; crypto_major avg `0.0604` n `8`; equity avg `0.2056` n `102`; fx avg `0.0128` n `6`; index avg `0.0678` n `25`; metal avg `0.0814` n `20`; unknown avg `0.0675` n `774`
- 1h: commodity avg `0.0419` n `12`; crypto_alt avg `0.1649` n `230`; crypto_major avg `0.1238` n `8`; equity avg `0.1755` n `102`; fx avg `0.015` n `6`; index avg `0.097` n `25`; metal avg `0.0556` n `20`; unknown avg `0.0244` n `774`
- 4h: commodity avg `0.1259` n `12`; crypto_alt avg `-0.1835` n `230`; crypto_major avg `-0.3203` n `8`; equity avg `-0.3718` n `102`; fx avg `-0.0232` n `6`; index avg `0.0323` n `25`; metal avg `-0.2172` n `20`; unknown avg `-0.0669` n `774`
- 24h: commodity avg `-0.5811` n `12`; crypto_alt avg `-3.7388` n `230`; crypto_major avg `-3.8608` n `8`; equity avg `-4.4318` n `102`; fx avg `-0.1705` n `6`; index avg `-0.8424` n `25`; metal avg `-0.58` n `20`; unknown avg `1225.2483` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
