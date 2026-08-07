# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T02:22:32.415501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `-0.0124` n `230`; crypto_major avg `-0.1248` n `8`; equity avg `0.0425` n `112`; fx avg `-0.0136` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0544` n `20`; unknown avg `0.2786` n `782`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `0.0406` n `230`; crypto_major avg `-0.0802` n `8`; equity avg `0.637` n `112`; fx avg `-0.0234` n `6`; index avg `0.0373` n `25`; metal avg `0.118` n `20`; unknown avg `0.1323` n `782`
- 4h: commodity avg `-0.01` n `12`; crypto_alt avg `0.2764` n `230`; crypto_major avg `-0.0763` n `8`; equity avg `-0.0486` n `112`; fx avg `-0.0635` n `6`; index avg `-0.1451` n `25`; metal avg `0.1613` n `20`; unknown avg `-0.0608` n `782`
- 24h: commodity avg `0.5013` n `12`; crypto_alt avg `0.8596` n `230`; crypto_major avg `-0.5296` n `8`; equity avg `0.6387` n `109`; fx avg `0.0299` n `6`; index avg `-0.14` n `25`; metal avg `-0.2395` n `20`; unknown avg `113.1721` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
