# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T22:07:31.444211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0599` n `12`; crypto_alt avg `-0.0631` n `230`; crypto_major avg `-0.0068` n `8`; equity avg `0.0705` n `112`; fx avg `0.0143` n `6`; index avg `0.0126` n `25`; metal avg `-0.0254` n `20`; unknown avg `-0.0325` n `782`
- 1h: commodity avg `0.0781` n `12`; crypto_alt avg `0.3258` n `230`; crypto_major avg `0.0237` n `8`; equity avg `0.463` n `112`; fx avg `-0.0009` n `6`; index avg `0.0217` n `25`; metal avg `-0.0653` n `20`; unknown avg `-0.1665` n `782`
- 4h: commodity avg `0.239` n `12`; crypto_alt avg `-0.1136` n `230`; crypto_major avg `-0.381` n `8`; equity avg `-0.6636` n `112`; fx avg `0.0054` n `6`; index avg `-0.0761` n `25`; metal avg `-0.1202` n `20`; unknown avg `-0.221` n `781`
- 24h: commodity avg `0.607` n `12`; crypto_alt avg `0.4267` n `230`; crypto_major avg `-1.0281` n `8`; equity avg `0.5284` n `109`; fx avg `0.035` n `6`; index avg `-0.1527` n `25`; metal avg `-0.1153` n `20`; unknown avg `113.2165` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `670`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1151`, n `670`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1061`, n `670`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0974`, n `670`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.093`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `670`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0815`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0755`, n `670`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `670`, weak_sample_signal
