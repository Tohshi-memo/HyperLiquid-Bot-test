# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T03:52:23.531007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `-0.1676` n `230`; crypto_major avg `-0.0865` n `8`; equity avg `-0.0709` n `112`; fx avg `-0.0085` n `6`; index avg `-0.0205` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.1268` n `782`
- 1h: commodity avg `0.0122` n `12`; crypto_alt avg `-0.31` n `230`; crypto_major avg `-0.2099` n `8`; equity avg `-0.1321` n `112`; fx avg `0.0074` n `6`; index avg `-0.0143` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.4371` n `782`
- 4h: commodity avg `0.0096` n `12`; crypto_alt avg `0.0772` n `230`; crypto_major avg `-0.136` n `8`; equity avg `-0.0138` n `112`; fx avg `-0.0411` n `6`; index avg `-0.1365` n `25`; metal avg `0.0657` n `20`; unknown avg `-0.1642` n `782`
- 24h: commodity avg `0.6199` n `12`; crypto_alt avg `0.3701` n `230`; crypto_major avg `-0.6383` n `8`; equity avg `0.8413` n `109`; fx avg `0.036` n `6`; index avg `-0.131` n `25`; metal avg `-0.0289` n `20`; unknown avg `113.2293` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
