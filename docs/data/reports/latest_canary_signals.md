# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T03:37:16.686308+00:00`
- Correlation status: `ready`
- Asset price records: `514`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1005` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0812` n `12`; crypto_alt avg `-0.0125` n `228`; crypto_major avg `0.0874` n `8`; equity avg `0.1281` n `65`; fx avg `-0.0043` n `4`; index avg `0.0072` n `23`; metal avg `-0.1023` n `18`; unknown avg `0.01` n `358`
- 1h: commodity avg `0.0115` n `12`; crypto_alt avg `-0.0221` n `228`; crypto_major avg `-0.1108` n `8`; equity avg `0.0961` n `65`; fx avg `0.0479` n `4`; index avg `0.067` n `23`; metal avg `0.0043` n `18`; unknown avg `-0.1272` n `358`
- 4h: commodity avg `-0.1577` n `12`; crypto_alt avg `-1.0295` n `228`; crypto_major avg `-0.9692` n `8`; equity avg `-0.0764` n `65`; fx avg `0.0996` n `4`; index avg `0.1313` n `23`; metal avg `0.2096` n `18`; unknown avg `-0.525` n `356`
- 24h: commodity avg `-1.8607` n `7`; crypto_alt avg `-0.1099` n `223`; crypto_major avg `-1.4621` n `7`; equity avg `1.4654` n `47`; fx avg `-0.2644` n `4`; index avg `1.3073` n `6`; metal avg `1.6501` n `7`; unknown avg `1.6509` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.129`, n `510`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1156`, n `510`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `510`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `510`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0759`, n `506`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0725`, n `506`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0696`, n `506`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0691`, n `506`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `510`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0667`, n `506`, weak_sample_signal
