# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T18:07:37.925307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `13`; crypto_alt avg `-0.0498` n `238`; crypto_major avg `-0.0299` n `8`; equity avg `-0.082` n `154`; fx avg `-0.0049` n `6`; index avg `-0.0101` n `27`; metal avg `0.0001` n `20`; unknown avg `0.1257` n `1232`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.1362` n `238`; crypto_major avg `-0.1334` n `8`; equity avg `-0.1136` n `154`; fx avg `-0.007` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0367` n `20`; unknown avg `0.0513` n `1232`
- 4h: commodity avg `-0.2227` n `13`; crypto_alt avg `0.801` n `238`; crypto_major avg `0.7732` n `8`; equity avg `0.9693` n `154`; fx avg `-0.044` n `6`; index avg `0.1856` n `27`; metal avg `0.1374` n `20`; unknown avg `8.4025` n `1196`
- 24h: commodity avg `-0.4554` n `13`; crypto_alt avg `0.1796` n `237`; crypto_major avg `0.6037` n `8`; equity avg `1.0382` n `154`; fx avg `-0.0694` n `6`; index avg `0.3362` n `27`; metal avg `0.0828` n `20`; unknown avg `34.9326` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
