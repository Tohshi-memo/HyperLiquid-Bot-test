# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T03:07:31.325749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0254` n `12`; crypto_alt avg `-0.0183` n `234`; crypto_major avg `-0.0541` n `8`; equity avg `-0.0136` n `141`; fx avg `0.0191` n `6`; index avg `0.0263` n `26`; metal avg `0.0028` n `20`; unknown avg `-0.0043` n `959`
- 1h: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.1863` n `234`; crypto_major avg `-0.2807` n `8`; equity avg `-0.0031` n `141`; fx avg `0.0025` n `6`; index avg `0.0328` n `26`; metal avg `-0.0024` n `20`; unknown avg `-0.0621` n `958`
- 4h: commodity avg `0.2566` n `12`; crypto_alt avg `-0.3623` n `234`; crypto_major avg `-0.3111` n `8`; equity avg `-0.1586` n `141`; fx avg `-0.0033` n `6`; index avg `-0.0151` n `26`; metal avg `-0.0082` n `20`; unknown avg `17.1004` n `952`
- 24h: commodity avg `0.12` n `12`; crypto_alt avg `3.2709` n `234`; crypto_major avg `1.2298` n `8`; equity avg `-0.3687` n `141`; fx avg `-0.1168` n `6`; index avg `0.1532` n `26`; metal avg `0.144` n `20`; unknown avg `1126.5116` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
