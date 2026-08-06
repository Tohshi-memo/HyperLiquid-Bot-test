# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T19:57:02.091025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `-0.0931` n `230`; crypto_major avg `0.0066` n `8`; equity avg `-0.2671` n `112`; fx avg `0.0081` n `6`; index avg `-0.0123` n `25`; metal avg `0.0045` n `20`; unknown avg `0.0348` n `781`
- 1h: commodity avg `0.1594` n `12`; crypto_alt avg `-0.4353` n `230`; crypto_major avg `-0.4046` n `8`; equity avg `-1.1102` n `112`; fx avg `0.0063` n `6`; index avg `-0.0976` n `25`; metal avg `-0.0549` n `20`; unknown avg `-0.1926` n `781`
- 4h: commodity avg `0.1594` n `12`; crypto_alt avg `-0.4353` n `230`; crypto_major avg `-0.4046` n `8`; equity avg `-1.1102` n `112`; fx avg `0.0063` n `6`; index avg `-0.0976` n `25`; metal avg `-0.0549` n `20`; unknown avg `-0.1926` n `781`
- 24h: commodity avg `0.5479` n `12`; crypto_alt avg `-0.0306` n `230`; crypto_major avg `-1.5644` n `8`; equity avg `-0.6488` n `109`; fx avg `0.0361` n `6`; index avg `-0.252` n `25`; metal avg `-0.0543` n `20`; unknown avg `113.2133` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1196`, n `670`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1149`, n `670`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `670`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0992`, n `670`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.092`, n `670`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.089`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0757`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `670`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `670`, weak_sample_signal
