# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T00:07:30.462794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.1736` n `230`; crypto_major avg `-0.1015` n `8`; equity avg `0.074` n `108`; fx avg `-0.0282` n `6`; index avg `0.0397` n `25`; metal avg `0.0326` n `20`; unknown avg `-0.0512` n `781`
- 1h: commodity avg `-0.0509` n `12`; crypto_alt avg `-0.4394` n `230`; crypto_major avg `-0.3738` n `8`; equity avg `0.2561` n `108`; fx avg `-0.033` n `6`; index avg `0.0355` n `25`; metal avg `0.0351` n `20`; unknown avg `0.0153` n `781`
- 4h: commodity avg `-0.1091` n `12`; crypto_alt avg `-0.2836` n `230`; crypto_major avg `-0.435` n `8`; equity avg `-0.1993` n `108`; fx avg `-0.0245` n `6`; index avg `-0.032` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.1288` n `781`
- 24h: commodity avg `-1.3909` n `12`; crypto_alt avg `-0.2593` n `230`; crypto_major avg `0.4139` n `8`; equity avg `3.1426` n `107`; fx avg `0.0396` n `6`; index avg `0.7011` n `25`; metal avg `0.807` n `20`; unknown avg `0.3852` n `764`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
