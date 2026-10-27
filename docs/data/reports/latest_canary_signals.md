# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T15:22:50.134125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `13`; crypto_alt avg `0.4893` n `238`; crypto_major avg `0.4411` n `8`; equity avg `0.1702` n `154`; fx avg `0.0018` n `6`; index avg `0.0272` n `27`; metal avg `0.0119` n `20`; unknown avg `6.2698` n `1206`
- 1h: commodity avg `-0.1497` n `13`; crypto_alt avg `0.8214` n `238`; crypto_major avg `0.7525` n `8`; equity avg `0.7643` n `154`; fx avg `-0.0308` n `6`; index avg `0.1724` n `27`; metal avg `0.1579` n `20`; unknown avg `6.9475` n `1202`
- 4h: commodity avg `-0.1883` n `13`; crypto_alt avg `1.0949` n `238`; crypto_major avg `1.1271` n `8`; equity avg `1.1307` n `154`; fx avg `-0.0024` n `6`; index avg `0.1506` n `27`; metal avg `0.3924` n `20`; unknown avg `4.9951` n `1150`
- 24h: commodity avg `-0.5142` n `13`; crypto_alt avg `-0.3406` n `237`; crypto_major avg `0.2681` n `8`; equity avg `0.7665` n `154`; fx avg `-0.0674` n `6`; index avg `0.282` n `27`; metal avg `0.0394` n `20`; unknown avg `20.1564` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
