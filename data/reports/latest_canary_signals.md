# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T22:22:28.982816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `0.4172` n `234`; crypto_major avg `0.2436` n `8`; equity avg `0.0051` n `141`; fx avg `0.0057` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0045` n `20`; unknown avg `-0.0311` n `944`
- 1h: commodity avg `0.0402` n `12`; crypto_alt avg `0.7138` n `234`; crypto_major avg `0.5006` n `8`; equity avg `0.0767` n `141`; fx avg `-0.0041` n `6`; index avg `0.0113` n `26`; metal avg `0.0025` n `20`; unknown avg `0.2164` n `932`
- 4h: commodity avg `0.0798` n `12`; crypto_alt avg `0.3277` n `234`; crypto_major avg `-0.0469` n `8`; equity avg `-0.0771` n `141`; fx avg `-0.0161` n `6`; index avg `0.0114` n `26`; metal avg `-0.0066` n `20`; unknown avg `-0.0026` n `852`
- 24h: commodity avg `-0.4522` n `12`; crypto_alt avg `2.8363` n `234`; crypto_major avg `1.3488` n `8`; equity avg `0.1534` n `141`; fx avg `-0.2349` n `6`; index avg `0.2539` n `26`; metal avg `0.1825` n `20`; unknown avg `1123.9308` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
