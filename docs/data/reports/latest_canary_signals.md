# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T21:31:38.798915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `13`; crypto_alt avg `0.1396` n `235`; crypto_major avg `0.0324` n `8`; equity avg `0.028` n `151`; fx avg `-0.0016` n `6`; index avg `-0.001` n `26`; metal avg `0.005` n `20`; unknown avg `4.1306` n `1135`
- 1h: commodity avg `-0.0448` n `13`; crypto_alt avg `-0.0783` n `235`; crypto_major avg `-0.0458` n `8`; equity avg `0.0441` n `151`; fx avg `-0.0155` n `6`; index avg `0.0189` n `26`; metal avg `0.0394` n `20`; unknown avg `3.8308` n `1127`
- 4h: commodity avg `0.1849` n `13`; crypto_alt avg `0.4929` n `235`; crypto_major avg `0.1358` n `8`; equity avg `0.4484` n `151`; fx avg `-0.0064` n `6`; index avg `0.0577` n `26`; metal avg `0.0173` n `20`; unknown avg `5.2381` n `1075`
- 24h: commodity avg `0.8493` n `13`; crypto_alt avg `-1.0606` n `235`; crypto_major avg `-0.4101` n `8`; equity avg `-0.6273` n `151`; fx avg `0.1642` n `6`; index avg `-0.1282` n `26`; metal avg `-0.2794` n `20`; unknown avg `2.5374` n `1003`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1577`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1428`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0913`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
