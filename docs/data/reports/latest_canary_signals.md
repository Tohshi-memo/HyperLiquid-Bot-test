# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T19:07:34.122289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1636` n `12`; crypto_alt avg `0.1524` n `230`; crypto_major avg `0.2479` n `8`; equity avg `0.3687` n `112`; fx avg `-0.0013` n `6`; index avg `0.085` n `25`; metal avg `0.0651` n `20`; unknown avg `-0.0274` n `782`
- 1h: commodity avg `-0.2189` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `-0.0261` n `8`; equity avg `0.2276` n `112`; fx avg `0.0062` n `6`; index avg `0.0554` n `25`; metal avg `0.0572` n `20`; unknown avg `-0.0461` n `782`
- 4h: commodity avg `-0.2084` n `12`; crypto_alt avg `-0.0309` n `230`; crypto_major avg `-0.5638` n `8`; equity avg `0.4884` n `112`; fx avg `-0.0187` n `6`; index avg `0.0627` n `25`; metal avg `0.0102` n `20`; unknown avg `-0.1198` n `782`
- 24h: commodity avg `0.1998` n `12`; crypto_alt avg `-0.5343` n `230`; crypto_major avg `-0.6644` n `8`; equity avg `0.8277` n `112`; fx avg `-0.1354` n `6`; index avg `0.0145` n `25`; metal avg `0.3577` n `20`; unknown avg `-0.1136` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2395`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
