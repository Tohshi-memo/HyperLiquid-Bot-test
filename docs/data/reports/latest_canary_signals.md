# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T05:37:25.373878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.0477` n `230`; crypto_major avg `-0.0414` n `8`; equity avg `0.0313` n `112`; fx avg `-0.0142` n `6`; index avg `-0.0235` n `25`; metal avg `0.0557` n `20`; unknown avg `0.4088` n `782`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `0.1767` n `230`; crypto_major avg `-0.2624` n `8`; equity avg `0.1818` n `112`; fx avg `-0.0047` n `6`; index avg `0.0234` n `25`; metal avg `0.0778` n `20`; unknown avg `-0.1479` n `782`
- 4h: commodity avg `0.1737` n `12`; crypto_alt avg `-0.3597` n `230`; crypto_major avg `-0.7104` n `8`; equity avg `0.6845` n `112`; fx avg `0.0022` n `6`; index avg `0.0582` n `25`; metal avg `0.201` n `20`; unknown avg `-0.541` n `782`
- 24h: commodity avg `0.7329` n `12`; crypto_alt avg `0.1533` n `230`; crypto_major avg `-1.5289` n `8`; equity avg `0.911` n `109`; fx avg `0.0582` n `6`; index avg `-0.0856` n `25`; metal avg `0.1247` n `20`; unknown avg `113.1455` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
