# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T12:37:38.070881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `13`; crypto_alt avg `0.2496` n `237`; crypto_major avg `0.1672` n `8`; equity avg `-0.0528` n `152`; fx avg `-0.0088` n `6`; index avg `-0.0256` n `26`; metal avg `0.0179` n `20`; unknown avg `3.1662` n `1240`
- 1h: commodity avg `-0.0461` n `13`; crypto_alt avg `0.3513` n `237`; crypto_major avg `0.273` n `8`; equity avg `0.5647` n `152`; fx avg `0.0019` n `6`; index avg `0.0676` n `26`; metal avg `0.0848` n `20`; unknown avg `12.803` n `1234`
- 4h: commodity avg `0.0808` n `13`; crypto_alt avg `0.4762` n `237`; crypto_major avg `0.4487` n `8`; equity avg `0.8306` n `152`; fx avg `0.0025` n `6`; index avg `0.0945` n `26`; metal avg `0.0671` n `20`; unknown avg `0.8829` n `1234`
- 24h: commodity avg `-0.3718` n `13`; crypto_alt avg `0.5583` n `237`; crypto_major avg `0.4903` n `8`; equity avg `0.237` n `152`; fx avg `0.033` n `6`; index avg `0.0829` n `26`; metal avg `0.2208` n `20`; unknown avg `0.2588` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2585`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
