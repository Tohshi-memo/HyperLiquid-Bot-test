# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T04:52:27.566907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0803` n `230`; crypto_major avg `-0.1782` n `8`; equity avg `-0.1902` n `112`; fx avg `-0.0068` n `6`; index avg `-0.03` n `25`; metal avg `-0.0201` n `20`; unknown avg `0.0107` n `782`
- 1h: commodity avg `0.0811` n `12`; crypto_alt avg `-0.2806` n `230`; crypto_major avg `-0.3188` n `8`; equity avg `-0.1805` n `112`; fx avg `-0.0135` n `6`; index avg `-0.0094` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.3447` n `782`
- 4h: commodity avg `0.1156` n `12`; crypto_alt avg `-0.5904` n `230`; crypto_major avg `-0.558` n `8`; equity avg `0.0636` n `112`; fx avg `-0.0356` n `6`; index avg `-0.1084` n `25`; metal avg `0.2233` n `20`; unknown avg `-0.4737` n `782`
- 24h: commodity avg `0.781` n `12`; crypto_alt avg `-0.1265` n `230`; crypto_major avg `-1.1862` n `8`; equity avg `0.5331` n `109`; fx avg `0.0222` n `6`; index avg `-0.1567` n `25`; metal avg `-0.0278` n `20`; unknown avg `113.1025` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
