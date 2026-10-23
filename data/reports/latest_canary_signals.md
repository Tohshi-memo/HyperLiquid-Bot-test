# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T18:07:32.767577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0291` n `13`; crypto_alt avg `0.0801` n `237`; crypto_major avg `-0.0286` n `8`; equity avg `0.0351` n `152`; fx avg `-0.0075` n `6`; index avg `0.0158` n `26`; metal avg `0.0358` n `20`; unknown avg `0.4559` n `1227`
- 1h: commodity avg `0.0719` n `13`; crypto_alt avg `-0.043` n `237`; crypto_major avg `-0.2892` n `8`; equity avg `-0.1341` n `152`; fx avg `-0.0071` n `6`; index avg `-0.001` n `26`; metal avg `-0.0063` n `20`; unknown avg `-0.2899` n `1229`
- 4h: commodity avg `0.1073` n `13`; crypto_alt avg `-0.1031` n `237`; crypto_major avg `-0.4047` n `8`; equity avg `0.1415` n `152`; fx avg `-0.0164` n `6`; index avg `0.0562` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.4464` n `1195`
- 24h: commodity avg `0.2879` n `13`; crypto_alt avg `1.4283` n `237`; crypto_major avg `1.076` n `8`; equity avg `1.6074` n `152`; fx avg `-0.114` n `6`; index avg `0.0919` n `26`; metal avg `-0.1703` n `20`; unknown avg `-0.5013` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
