# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T10:37:25.778157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `12`; crypto_alt avg `-0.163` n `230`; crypto_major avg `-0.1206` n `8`; equity avg `-0.1225` n `107`; fx avg `-0.0073` n `6`; index avg `-0.0134` n `25`; metal avg `0.0322` n `20`; unknown avg `-0.0183` n `781`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `-0.0931` n `230`; crypto_major avg `0.024` n `8`; equity avg `0.4219` n `107`; fx avg `-0.0255` n `6`; index avg `0.0333` n `25`; metal avg `0.0626` n `20`; unknown avg `0.0062` n `781`
- 4h: commodity avg `0.0382` n `12`; crypto_alt avg `-0.3068` n `230`; crypto_major avg `-0.0988` n `8`; equity avg `0.4725` n `107`; fx avg `0.0246` n `6`; index avg `0.0291` n `25`; metal avg `0.0851` n `20`; unknown avg `0.8675` n `781`
- 24h: commodity avg `0.358` n `12`; crypto_alt avg `0.723` n `230`; crypto_major avg `1.0209` n `8`; equity avg `4.1155` n `107`; fx avg `0.0957` n `6`; index avg `0.4085` n `25`; metal avg `0.2439` n `20`; unknown avg `1.0424` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
