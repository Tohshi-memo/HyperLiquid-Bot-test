# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T01:52:30.711815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0456` n `12`; crypto_alt avg `-0.0056` n `234`; crypto_major avg `0.0629` n `8`; equity avg `0.051` n `141`; fx avg `-0.0022` n `6`; index avg `0.0026` n `26`; metal avg `0.0162` n `20`; unknown avg `-0.0322` n `960`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.2602` n `234`; crypto_major avg `0.3675` n `8`; equity avg `0.0605` n `141`; fx avg `-0.0015` n `6`; index avg `0.0142` n `26`; metal avg `0.0169` n `20`; unknown avg `0.4393` n `958`
- 4h: commodity avg `0.3371` n `12`; crypto_alt avg `1.001` n `234`; crypto_major avg `0.6285` n `8`; equity avg `-0.1518` n `141`; fx avg `-0.0032` n `6`; index avg `-0.0567` n `26`; metal avg `-0.0291` n `20`; unknown avg `0.4909` n `926`
- 24h: commodity avg `0.0857` n `12`; crypto_alt avg `2.9465` n `234`; crypto_major avg `1.1209` n `8`; equity avg `-0.3138` n `141`; fx avg `-0.1852` n `6`; index avg `0.1241` n `26`; metal avg `0.1433` n `20`; unknown avg `1125.7916` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
