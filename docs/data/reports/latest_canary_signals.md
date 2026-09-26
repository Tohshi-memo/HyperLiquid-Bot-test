# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T14:07:31.129279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `-0.0128` n `234`; crypto_major avg `0.0487` n `8`; equity avg `-0.0242` n `141`; fx avg `0.0055` n `6`; index avg `0.0025` n `26`; metal avg `-0.003` n `20`; unknown avg `0.0192` n `959`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `-0.1856` n `234`; crypto_major avg `-0.248` n `8`; equity avg `-0.0331` n `141`; fx avg `-0.0011` n `6`; index avg `0.0119` n `26`; metal avg `-0.0012` n `20`; unknown avg `3.1617` n `959`
- 4h: commodity avg `0.0673` n `12`; crypto_alt avg `0.2961` n `234`; crypto_major avg `0.0141` n `8`; equity avg `0.0351` n `141`; fx avg `0.0282` n `6`; index avg `-0.0047` n `26`; metal avg `0.0027` n `20`; unknown avg `1.4679` n `949`
- 24h: commodity avg `0.1852` n `12`; crypto_alt avg `3.008` n `234`; crypto_major avg `0.0745` n `8`; equity avg `0.1769` n `141`; fx avg `0.0148` n `6`; index avg `0.0991` n `26`; metal avg `0.2797` n `20`; unknown avg `-0.7419` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
