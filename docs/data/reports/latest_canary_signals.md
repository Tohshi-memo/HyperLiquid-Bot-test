# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T18:22:32.427792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `-0.0074` n `230`; crypto_major avg `0.0792` n `8`; equity avg `-0.0031` n `112`; fx avg `0.0047` n `6`; index avg `-0.022` n `25`; metal avg `-0.0337` n `20`; unknown avg `0.0126` n `782`
- 1h: commodity avg `0.0294` n `12`; crypto_alt avg `0.0906` n `230`; crypto_major avg `0.2767` n `8`; equity avg `-0.0925` n `112`; fx avg `0.0112` n `6`; index avg `-0.0319` n `25`; metal avg `0.0272` n `20`; unknown avg `0.0904` n `782`
- 4h: commodity avg `0.1311` n `12`; crypto_alt avg `-0.2648` n `230`; crypto_major avg `-0.6634` n `8`; equity avg `0.471` n `112`; fx avg `-0.0259` n `6`; index avg `0.0205` n `25`; metal avg `-0.0725` n `20`; unknown avg `-0.0983` n `782`
- 24h: commodity avg `0.3921` n `12`; crypto_alt avg `-0.5045` n `230`; crypto_major avg `-0.5612` n `8`; equity avg `0.5999` n `112`; fx avg `-0.1371` n `6`; index avg `-0.0617` n `25`; metal avg `0.2656` n `20`; unknown avg `-0.0929` n `765`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.2569`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
