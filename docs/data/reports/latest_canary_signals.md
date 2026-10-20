# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T14:07:32.496301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3824` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.0775` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8905` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.7099` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0374` n `13`; crypto_alt avg `1.474` n `237`; crypto_major avg `1.4595` n `8`; equity avg `1.2274` n `151`; fx avg `0.0173` n `6`; index avg `0.1496` n `26`; metal avg `0.0282` n `20`; unknown avg `0.4999` n `1142`
- 1h: commodity avg `-0.2376` n `13`; crypto_alt avg `2.0738` n `237`; crypto_major avg `1.8399` n `8`; equity avg `1.1466` n `151`; fx avg `0.0551` n `6`; index avg `0.172` n `26`; metal avg `0.13` n `20`; unknown avg `4.2979` n `1108`
- 4h: commodity avg `-0.3732` n `13`; crypto_alt avg `2.3626` n `237`; crypto_major avg `2.0092` n `8`; equity avg `1.1052` n `151`; fx avg `0.0597` n `6`; index avg `0.1933` n `26`; metal avg `0.1187` n `20`; unknown avg `2.4141` n `1102`
- 24h: commodity avg `-0.0128` n `13`; crypto_alt avg `2.8151` n `237`; crypto_major avg `2.054` n `8`; equity avg `-0.2538` n `151`; fx avg `0.0359` n `6`; index avg `-0.0403` n `26`; metal avg `-0.0006` n `20`; unknown avg `6.8316` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
