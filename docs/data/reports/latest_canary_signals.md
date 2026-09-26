# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T05:10:30.220815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.1237` n `234`; crypto_major avg `-0.0809` n `8`; equity avg `0.0551` n `141`; fx avg `-0.0001` n `6`; index avg `0.0092` n `26`; metal avg `0.0023` n `20`; unknown avg `1.9911` n `959`
- 1h: commodity avg `0.0008` n `12`; crypto_alt avg `-0.1765` n `234`; crypto_major avg `-0.1586` n `8`; equity avg `0.0594` n `141`; fx avg `0.0011` n `6`; index avg `0.0012` n `26`; metal avg `-0.0003` n `20`; unknown avg `1.5844` n `959`
- 4h: commodity avg `-0.0869` n `12`; crypto_alt avg `-0.0051` n `234`; crypto_major avg `-0.3478` n `8`; equity avg `0.1074` n `141`; fx avg `0.0062` n `6`; index avg `0.0245` n `26`; metal avg `-0.002` n `20`; unknown avg `14.6159` n `952`
- 24h: commodity avg `0.0203` n `12`; crypto_alt avg `3.2353` n `234`; crypto_major avg `1.0876` n `8`; equity avg `-0.3411` n `141`; fx avg `-0.1169` n `6`; index avg `0.1307` n `26`; metal avg `0.2945` n `20`; unknown avg `1129.0478` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
