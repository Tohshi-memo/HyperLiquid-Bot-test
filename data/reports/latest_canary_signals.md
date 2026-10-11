# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T00:37:27.858670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.1068` n `235`; crypto_major avg `-0.1062` n `8`; equity avg `-0.0121` n `150`; fx avg `-0.0005` n `6`; index avg `-0.0026` n `26`; metal avg `0.0001` n `20`; unknown avg `-0.0563` n `1117`
- 1h: commodity avg `0.05` n `13`; crypto_alt avg `-0.1792` n `235`; crypto_major avg `-0.1679` n `8`; equity avg `-0.0252` n `150`; fx avg `-0.01` n `6`; index avg `0.0032` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.1384` n `1109`
- 4h: commodity avg `0.2177` n `13`; crypto_alt avg `-0.2653` n `235`; crypto_major avg `-0.2155` n `8`; equity avg `-0.0071` n `150`; fx avg `0.0012` n `6`; index avg `-0.0016` n `26`; metal avg `0.0094` n `20`; unknown avg `2.8795` n `1079`
- 24h: commodity avg `0.0941` n `13`; crypto_alt avg `1.2493` n `235`; crypto_major avg `0.3886` n `8`; equity avg `0.0968` n `150`; fx avg `-0.0076` n `6`; index avg `-0.0043` n `26`; metal avg `-0.016` n `20`; unknown avg `0.3077` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
