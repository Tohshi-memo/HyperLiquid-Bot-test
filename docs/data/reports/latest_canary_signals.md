# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T04:07:25.366090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `12`; crypto_alt avg `0.3977` n `234`; crypto_major avg `0.1273` n `8`; equity avg `0.0212` n `141`; fx avg `-0.0015` n `6`; index avg `0.0003` n `26`; metal avg `-0.0057` n `20`; unknown avg `21.6021` n `953`
- 1h: commodity avg `0.0072` n `12`; crypto_alt avg `0.225` n `234`; crypto_major avg `-0.1423` n `8`; equity avg `-0.0118` n `141`; fx avg `-0.0004` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0077` n `20`; unknown avg `5.6051` n `953`
- 4h: commodity avg `0.2755` n `12`; crypto_alt avg `-0.2228` n `234`; crypto_major avg `-0.334` n `8`; equity avg `-0.1569` n `141`; fx avg `0.0025` n `6`; index avg `-0.0404` n `26`; metal avg `-0.0215` n `20`; unknown avg `17.4806` n `952`
- 24h: commodity avg `0.0264` n `12`; crypto_alt avg `3.4533` n `234`; crypto_major avg `1.127` n `8`; equity avg `-0.3059` n `141`; fx avg `-0.0976` n `6`; index avg `0.1436` n `26`; metal avg `0.2483` n `20`; unknown avg `1128.7806` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
