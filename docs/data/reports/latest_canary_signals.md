# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T17:15:19.823956+00:00`
- Correlation status: `ready`
- Asset price records: `377`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0452` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0481` n `7`; crypto_alt avg `0.0829` n `223`; crypto_major avg `0.0295` n `7`; equity avg `0.0777` n `47`; fx avg `0.0168` n `4`; index avg `0.0094` n `6`; metal avg `-0.1182` n `7`; unknown avg `-0.0239` n `313`
- 1h: commodity avg `0.0779` n `7`; crypto_alt avg `-0.0599` n `223`; crypto_major avg `-0.2433` n `7`; equity avg `0.0596` n `47`; fx avg `-0.0002` n `4`; index avg `0.0237` n `6`; metal avg `-0.2145` n `7`; unknown avg `-0.3171` n `313`
- 4h: commodity avg `-0.4028` n `7`; crypto_alt avg `-0.5987` n `223`; crypto_major avg `-0.4716` n `7`; equity avg `0.4161` n `47`; fx avg `-0.1412` n `4`; index avg `0.5736` n `6`; metal avg `-0.6005` n `7`; unknown avg `0.0921` n `312`
- 24h: commodity avg `-1.3692` n `7`; crypto_alt avg `1.2893` n `223`; crypto_major avg `1.3743` n `7`; equity avg `1.6146` n `47`; fx avg `-0.0423` n `4`; index avg `1.2769` n `6`; metal avg `0.7097` n `7`; unknown avg `0.727` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2071`, n `373`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2003`, n `373`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `373`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1295`, n `373`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `373`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1077`, n `369`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `373`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `373`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `373`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0994`, n `369`, weak_sample_signal
