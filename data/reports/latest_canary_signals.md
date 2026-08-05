# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T01:07:38.340441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1184` n `12`; crypto_alt avg `0.0057` n `230`; crypto_major avg `0.0442` n `8`; equity avg `-0.0906` n `108`; fx avg `0.0099` n `6`; index avg `-0.0189` n `25`; metal avg `-0.053` n `20`; unknown avg `0.2932` n `781`
- 1h: commodity avg `0.2251` n `12`; crypto_alt avg `0.0541` n `230`; crypto_major avg `-0.0645` n `8`; equity avg `-0.0631` n `108`; fx avg `-0.0375` n `6`; index avg `-0.0062` n `25`; metal avg `-0.037` n `20`; unknown avg `0.2822` n `781`
- 4h: commodity avg `0.1542` n `12`; crypto_alt avg `-0.3561` n `230`; crypto_major avg `-0.4521` n `8`; equity avg `0.3779` n `108`; fx avg `-0.0783` n `6`; index avg `0.0659` n `25`; metal avg `-0.034` n `20`; unknown avg `0.2259` n `781`
- 24h: commodity avg `-1.2186` n `12`; crypto_alt avg `0.1718` n `230`; crypto_major avg `0.6534` n `8`; equity avg `4.1718` n `107`; fx avg `0.105` n `6`; index avg `0.9445` n `25`; metal avg `0.8856` n `20`; unknown avg `0.395` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
