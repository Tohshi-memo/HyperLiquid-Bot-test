# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T12:37:31.694775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `-0.0706` n `230`; crypto_major avg `-0.1022` n `8`; equity avg `0.5325` n `112`; fx avg `-0.1037` n `6`; index avg `0.1015` n `25`; metal avg `0.2546` n `20`; unknown avg `-0.0152` n `782`
- 1h: commodity avg `0.099` n `12`; crypto_alt avg `-0.0992` n `230`; crypto_major avg `0.1779` n `8`; equity avg `0.564` n `112`; fx avg `-0.1005` n `6`; index avg `0.1096` n `25`; metal avg `0.1424` n `20`; unknown avg `-0.0163` n `782`
- 4h: commodity avg `-0.225` n `12`; crypto_alt avg `0.0325` n `230`; crypto_major avg `0.7919` n `8`; equity avg `0.6849` n `112`; fx avg `-0.1044` n `6`; index avg `0.1607` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0928` n `782`
- 24h: commodity avg `0.1707` n `12`; crypto_alt avg `0.4518` n `230`; crypto_major avg `0.577` n `8`; equity avg `2.8922` n `109`; fx avg `-0.1916` n `6`; index avg `0.2403` n `25`; metal avg `0.4144` n `20`; unknown avg `0.3257` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
