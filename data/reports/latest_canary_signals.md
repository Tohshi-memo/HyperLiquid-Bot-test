# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T21:37:32.155286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `0.7854` n `238`; crypto_major avg `0.6579` n `8`; equity avg `0.1107` n `154`; fx avg `-0.0089` n `6`; index avg `0.0061` n `27`; metal avg `0.0212` n `20`; unknown avg `3.9169` n `1238`
- 1h: commodity avg `-0.0218` n `13`; crypto_alt avg `0.6447` n `238`; crypto_major avg `0.5976` n `8`; equity avg `0.1705` n `154`; fx avg `-0.0062` n `6`; index avg `0.0113` n `27`; metal avg `0.0423` n `20`; unknown avg `1.9227` n `1226`
- 4h: commodity avg `0.1639` n `13`; crypto_alt avg `0.665` n `238`; crypto_major avg `0.4742` n `8`; equity avg `-0.1486` n `154`; fx avg `-0.0153` n `6`; index avg `0.0001` n `27`; metal avg `0.0378` n `20`; unknown avg `2.5558` n `1152`
- 24h: commodity avg `-0.2107` n `13`; crypto_alt avg `1.6364` n `237`; crypto_major avg `1.9188` n `8`; equity avg `1.488` n `154`; fx avg `-0.0499` n `6`; index avg `0.4094` n `27`; metal avg `0.2326` n `20`; unknown avg `29.5179` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
