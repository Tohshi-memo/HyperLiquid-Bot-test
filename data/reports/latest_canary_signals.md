# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T03:52:29.048648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.1241` n `230`; crypto_major avg `0.1907` n `8`; equity avg `0.2036` n `121`; fx avg `-0.0135` n `6`; index avg `0.0388` n `25`; metal avg `0.034` n `20`; unknown avg `0.0124` n `792`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.1784` n `230`; crypto_major avg `-0.2303` n `8`; equity avg `0.1321` n `121`; fx avg `0.0055` n `6`; index avg `0.025` n `25`; metal avg `0.0553` n `20`; unknown avg `-0.1843` n `792`
- 4h: commodity avg `0.0611` n `12`; crypto_alt avg `0.1206` n `230`; crypto_major avg `-0.0183` n `8`; equity avg `0.1276` n `121`; fx avg `0.0915` n `6`; index avg `0.0973` n `25`; metal avg `-0.0907` n `20`; unknown avg `0.0534` n `792`
- 24h: commodity avg `-0.0596` n `12`; crypto_alt avg `5.033` n `230`; crypto_major avg `9.3545` n `8`; equity avg `1.1223` n `120`; fx avg `0.0483` n `6`; index avg `0.2937` n `25`; metal avg `1.0382` n `20`; unknown avg `1.6468` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
