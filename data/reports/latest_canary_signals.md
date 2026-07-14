# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T18:37:32.643310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0712` n `12`; crypto_alt avg `0.0308` n `230`; crypto_major avg `0.1408` n `8`; equity avg `-0.0415` n `92`; fx avg `-0.0034` n `6`; index avg `-0.006` n `25`; metal avg `-0.0504` n `20`; unknown avg `-0.0771` n `768`
- 1h: commodity avg `0.1043` n `12`; crypto_alt avg `-0.0764` n `230`; crypto_major avg `0.2522` n `8`; equity avg `0.1271` n `92`; fx avg `-0.0045` n `6`; index avg `0.0106` n `25`; metal avg `-0.0647` n `20`; unknown avg `-0.1909` n `767`
- 4h: commodity avg `0.0581` n `12`; crypto_alt avg `-0.1549` n `230`; crypto_major avg `0.4675` n `8`; equity avg `0.4085` n `92`; fx avg `-0.0324` n `6`; index avg `0.0923` n `25`; metal avg `-0.2132` n `20`; unknown avg `-0.3256` n `758`
- 24h: commodity avg `0.2696` n `12`; crypto_alt avg `1.8527` n `230`; crypto_major avg `3.5318` n `8`; equity avg `1.366` n `92`; fx avg `-0.0231` n `6`; index avg `0.3775` n `25`; metal avg `0.5633` n `20`; unknown avg `-0.0606` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
