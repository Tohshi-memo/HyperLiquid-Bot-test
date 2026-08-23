# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T09:22:25.528522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0291` n `12`; crypto_alt avg `0.029` n `230`; crypto_major avg `-0.1347` n `8`; equity avg `-0.0018` n `121`; fx avg `0.0` n `6`; index avg `0.0031` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.0104` n `794`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.5908` n `230`; crypto_major avg `0.1164` n `8`; equity avg `0.0304` n `121`; fx avg `0.0107` n `6`; index avg `0.0072` n `25`; metal avg `-0.0167` n `20`; unknown avg `1.0367` n `794`
- 4h: commodity avg `0.0319` n `12`; crypto_alt avg `1.9947` n `230`; crypto_major avg `0.6557` n `8`; equity avg `0.0734` n `121`; fx avg `-0.0475` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0135` n `20`; unknown avg `0.4794` n `778`
- 24h: commodity avg `-0.0097` n `12`; crypto_alt avg `-1.9748` n `230`; crypto_major avg `-0.9865` n `8`; equity avg `0.1418` n `121`; fx avg `0.0577` n `6`; index avg `0.0171` n `25`; metal avg `0.0378` n `20`; unknown avg `2.4525` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
