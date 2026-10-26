# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T22:22:41.037420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `13`; crypto_alt avg `-0.0691` n `237`; crypto_major avg `-0.0345` n `8`; equity avg `0.0766` n `154`; fx avg `0.0139` n `6`; index avg `0.0064` n `27`; metal avg `0.0071` n `20`; unknown avg `0.7119` n `1238`
- 1h: commodity avg `-0.0212` n `13`; crypto_alt avg `0.2066` n `237`; crypto_major avg `0.0706` n `8`; equity avg `0.2295` n `154`; fx avg `0.0144` n `6`; index avg `0.0336` n `27`; metal avg `0.0091` n `20`; unknown avg `1.4452` n `1236`
- 4h: commodity avg `-0.1187` n `13`; crypto_alt avg `-0.5217` n `237`; crypto_major avg `-0.6372` n `8`; equity avg `-0.0853` n `154`; fx avg `-0.0143` n `6`; index avg `-0.0085` n `27`; metal avg `-0.046` n `20`; unknown avg `10.7632` n `1134`
- 24h: commodity avg `-0.0539` n `13`; crypto_alt avg `-0.3614` n `237`; crypto_major avg `-0.1839` n `8`; equity avg `0.8421` n `153`; fx avg `0.0082` n `6`; index avg `-0.0802` n `27`; metal avg `-0.0229` n `20`; unknown avg `706.1278` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
