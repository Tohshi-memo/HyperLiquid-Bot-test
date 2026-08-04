# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T11:52:27.347334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.5739` n `12`; crypto_alt avg `0.1372` n `230`; crypto_major avg `0.2896` n `8`; equity avg `0.2907` n `107`; fx avg `-0.0076` n `6`; index avg `0.0702` n `25`; metal avg `0.0934` n `20`; unknown avg `0.0127` n `781`
- 1h: commodity avg `-0.7826` n `12`; crypto_alt avg `-0.0646` n `230`; crypto_major avg `0.227` n `8`; equity avg `0.5575` n `107`; fx avg `-0.0538` n `6`; index avg `0.1389` n `25`; metal avg `0.2875` n `20`; unknown avg `0.0321` n `781`
- 4h: commodity avg `-0.9097` n `12`; crypto_alt avg `-0.0935` n `230`; crypto_major avg `0.35` n `8`; equity avg `0.9303` n `107`; fx avg `-0.0575` n `6`; index avg `0.1469` n `25`; metal avg `0.3313` n `20`; unknown avg `0.1721` n `781`
- 24h: commodity avg `-0.5884` n `12`; crypto_alt avg `1.0279` n `230`; crypto_major avg `1.7337` n `8`; equity avg `5.4692` n `107`; fx avg `0.0667` n `6`; index avg `0.6751` n `25`; metal avg `0.586` n `20`; unknown avg `0.8945` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
