# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T00:37:31.891973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.5907` n `12`; crypto_alt avg `-0.7112` n `234`; crypto_major avg `-0.5345` n `8`; equity avg `-0.2352` n `141`; fx avg `-0.0072` n `6`; index avg `-0.0948` n `26`; metal avg `-0.0449` n `20`; unknown avg `4.3904` n `960`
- 1h: commodity avg `0.5891` n `12`; crypto_alt avg `-0.4148` n `234`; crypto_major avg `-0.5345` n `8`; equity avg `-0.2302` n `141`; fx avg `-0.0072` n `6`; index avg `-0.0934` n `26`; metal avg `-0.0379` n `20`; unknown avg `4.6663` n `952`
- 4h: commodity avg `0.5916` n `12`; crypto_alt avg `-0.2797` n `234`; crypto_major avg `-0.4276` n `8`; equity avg `-0.1962` n `141`; fx avg `-0.0182` n `6`; index avg `-0.0776` n `26`; metal avg `-0.0346` n `20`; unknown avg `5.2714` n `926`
- 24h: commodity avg `0.2853` n `12`; crypto_alt avg `2.4146` n `234`; crypto_major avg `0.5005` n `8`; equity avg `-0.187` n `141`; fx avg `-0.244` n `6`; index avg `0.1666` n `26`; metal avg `0.1898` n `20`; unknown avg `1129.5324` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
