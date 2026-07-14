# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T18:22:32.099284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.1772` n `230`; crypto_major avg `-0.0696` n `8`; equity avg `0.0475` n `92`; fx avg `0.0016` n `6`; index avg `0.0136` n `25`; metal avg `-0.0175` n `20`; unknown avg `0.0164` n `768`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.1357` n `230`; crypto_major avg `0.216` n `8`; equity avg `0.2496` n `92`; fx avg `0.0069` n `6`; index avg `0.0158` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.1176` n `766`
- 4h: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.0974` n `230`; crypto_major avg `0.3539` n `8`; equity avg `0.5789` n `92`; fx avg `-0.0284` n `6`; index avg `0.1419` n `25`; metal avg `-0.197` n `20`; unknown avg `-0.2994` n `758`
- 24h: commodity avg `0.0546` n `12`; crypto_alt avg `1.9278` n `230`; crypto_major avg `3.5839` n `8`; equity avg `1.402` n `92`; fx avg `-0.0122` n `6`; index avg `0.3957` n `25`; metal avg `0.6795` n `20`; unknown avg `-0.0613` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
