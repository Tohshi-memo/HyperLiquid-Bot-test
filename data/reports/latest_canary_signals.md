# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T15:07:34.842756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1542` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.147` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0831` n `13`; crypto_alt avg `-0.0265` n `237`; crypto_major avg `0.0588` n `8`; equity avg `-0.0849` n `151`; fx avg `0.003` n `6`; index avg `0.0023` n `26`; metal avg `-0.0156` n `20`; unknown avg `2.3927` n `1197`
- 1h: commodity avg `-0.3147` n `13`; crypto_alt avg `0.8` n `237`; crypto_major avg `0.4058` n `8`; equity avg `0.9268` n `151`; fx avg `-0.0125` n `6`; index avg `0.1593` n `26`; metal avg `0.1632` n `20`; unknown avg `1.8824` n `1194`
- 4h: commodity avg `-0.7483` n `13`; crypto_alt avg `3.0722` n `237`; crypto_major avg `2.4059` n `8`; equity avg `2.3683` n `151`; fx avg `0.06` n `6`; index avg `0.4002` n `26`; metal avg `0.2589` n `20`; unknown avg `3.475` n `1100`
- 24h: commodity avg `-0.2931` n `13`; crypto_alt avg `3.092` n `237`; crypto_major avg `1.9813` n `8`; equity avg `-0.0634` n `151`; fx avg `0.0252` n `6`; index avg `0.022` n `26`; metal avg `0.1441` n `20`; unknown avg `3.9031` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
