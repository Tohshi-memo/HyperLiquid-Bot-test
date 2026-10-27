# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T14:22:34.227038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0766` n `13`; crypto_alt avg `-0.0351` n `238`; crypto_major avg `-0.126` n `8`; equity avg `-0.1189` n `154`; fx avg `-0.0041` n `6`; index avg `-0.0171` n `27`; metal avg `0.0128` n `20`; unknown avg `0.2195` n `1236`
- 1h: commodity avg `-0.0515` n `13`; crypto_alt avg `-0.1054` n `238`; crypto_major avg `-0.2069` n `8`; equity avg `0.3055` n `154`; fx avg `-0.0003` n `6`; index avg `-0.0261` n `27`; metal avg `0.1453` n `20`; unknown avg `0.1058` n `1164`
- 4h: commodity avg `-0.3242` n `13`; crypto_alt avg `0.9393` n `238`; crypto_major avg `0.9755` n `8`; equity avg `1.1374` n `154`; fx avg `0.0181` n `6`; index avg `0.0989` n `27`; metal avg `0.3324` n `20`; unknown avg `1.244` n `1112`
- 24h: commodity avg `-0.1765` n `13`; crypto_alt avg `0.2079` n `237`; crypto_major avg `0.7436` n `8`; equity avg `2.104` n `154`; fx avg `-0.0053` n `6`; index avg `0.3835` n `27`; metal avg `0.1526` n `20`; unknown avg `1338.8866` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
