# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T19:52:30.975982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.92` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0421` n `12`; crypto_alt avg `0.1023` n `230`; crypto_major avg `0.0964` n `8`; equity avg `0.0441` n `92`; fx avg `-0.0007` n `6`; index avg `0.0207` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0688` n `768`
- 1h: commodity avg `0.0294` n `12`; crypto_alt avg `0.0921` n `230`; crypto_major avg `0.0894` n `8`; equity avg `0.0757` n `92`; fx avg `0.0078` n `6`; index avg `0.0138` n `25`; metal avg `0.0304` n `20`; unknown avg `-0.1837` n `768`
- 4h: commodity avg `0.0155` n `12`; crypto_alt avg `-0.3869` n `230`; crypto_major avg `0.0618` n `8`; equity avg `0.2395` n `92`; fx avg `-0.0252` n `6`; index avg `0.0404` n `25`; metal avg `-0.0679` n `20`; unknown avg `-0.1776` n `766`
- 24h: commodity avg `0.3754` n `12`; crypto_alt avg `1.617` n `230`; crypto_major avg `3.2333` n `8`; equity avg `1.2093` n `92`; fx avg `-0.0187` n `6`; index avg `0.3715` n `25`; metal avg `0.5914` n `20`; unknown avg `0.0033` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
