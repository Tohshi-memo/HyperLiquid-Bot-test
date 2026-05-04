# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T06:15:19.228459+00:00`
- Correlation status: `ready`
- Asset price records: `240`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `7`; crypto_alt avg `-0.2325` n `223`; crypto_major avg `-0.2708` n `7`; equity avg `-0.0205` n `42`; fx avg `0.0114` n `4`; index avg `0.0017` n `9`; metal avg `-0.1047` n `7`; unknown avg `-0.1099` n `314`
- 1h: commodity avg `-0.1357` n `7`; crypto_alt avg `-0.0766` n `223`; crypto_major avg `-0.4779` n `7`; equity avg `-0.1827` n `42`; fx avg `0.0271` n `4`; index avg `0.1075` n `9`; metal avg `-0.2456` n `7`; unknown avg `-0.3771` n `312`
- 4h: commodity avg `-0.1267` n `7`; crypto_alt avg `0.7067` n `223`; crypto_major avg `0.3636` n `7`; equity avg `-0.0504` n `42`; fx avg `-0.0328` n `4`; index avg `0.3943` n `9`; metal avg `-0.3177` n `7`; unknown avg `-0.3504` n `312`
- 24h: commodity avg `-0.082` n `7`; crypto_alt avg `2.6138` n `223`; crypto_major avg `2.5947` n `7`; equity avg `0.8833` n `42`; fx avg `-0.0262` n `4`; index avg `0.931` n `9`; metal avg `-0.0916` n `7`; unknown avg `0.2162` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4092`, n `232`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3993`, n `232`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3606`, n `236`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3464`, n `236`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1961`, n `232`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1889`, n `232`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1862`, n `236`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1791`, n `236`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1736`, n `236`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1519`, n `232`, weak_sample_signal
