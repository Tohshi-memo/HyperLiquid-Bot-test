# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T11:37:31.183041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `0.072` n `234`; crypto_major avg `0.0097` n `8`; equity avg `-0.0097` n `141`; fx avg `0.0004` n `6`; index avg `-0.0131` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.5087` n `962`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.115` n `234`; crypto_major avg `-0.0534` n `8`; equity avg `-0.0116` n `141`; fx avg `-0.0009` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0059` n `20`; unknown avg `0.9435` n `960`
- 4h: commodity avg `0.0561` n `12`; crypto_alt avg `0.0796` n `234`; crypto_major avg `0.4102` n `8`; equity avg `0.0871` n `141`; fx avg `-0.018` n `6`; index avg `0.0086` n `26`; metal avg `-0.0102` n `20`; unknown avg `2.0312` n `943`
- 24h: commodity avg `0.0973` n `12`; crypto_alt avg `0.6063` n `234`; crypto_major avg `0.56` n `8`; equity avg `0.3368` n `141`; fx avg `-0.0454` n `6`; index avg `0.0219` n `26`; metal avg `-0.0073` n `20`; unknown avg `6.8493` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
