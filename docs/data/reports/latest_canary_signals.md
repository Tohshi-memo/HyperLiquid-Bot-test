# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T19:16:29.618103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `13`; crypto_alt avg `0.0704` n `237`; crypto_major avg `0.0875` n `8`; equity avg `0.0325` n `152`; fx avg `0.002` n `6`; index avg `0.0066` n `26`; metal avg `-0.0035` n `20`; unknown avg `1.3693` n `1240`
- 1h: commodity avg `-0.0122` n `13`; crypto_alt avg `-0.101` n `237`; crypto_major avg `-0.0516` n `8`; equity avg `0.0311` n `152`; fx avg `-0.0123` n `6`; index avg `0.0112` n `26`; metal avg `-0.0001` n `20`; unknown avg `8.4258` n `1240`
- 4h: commodity avg `-0.0743` n `13`; crypto_alt avg `0.5614` n `237`; crypto_major avg `0.3234` n `8`; equity avg `0.3373` n `152`; fx avg `-0.0043` n `6`; index avg `0.0489` n `26`; metal avg `0.0468` n `20`; unknown avg `4.3044` n `1194`
- 24h: commodity avg `-0.2534` n `13`; crypto_alt avg `0.3924` n `237`; crypto_major avg `0.7605` n `8`; equity avg `0.7104` n `152`; fx avg `0.0294` n `6`; index avg `0.1388` n `26`; metal avg `0.1449` n `20`; unknown avg `9.862` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2254`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
