# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T23:37:55.887880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.0636` n `234`; crypto_major avg `0.109` n `8`; equity avg `0.0047` n `141`; fx avg `0.0007` n `6`; index avg `0.0224` n `26`; metal avg `-0.0029` n `20`; unknown avg `2.9109` n `946`
- 1h: commodity avg `-0.0401` n `12`; crypto_alt avg `0.2252` n `234`; crypto_major avg `0.2898` n `8`; equity avg `0.0136` n `141`; fx avg `0.042` n `6`; index avg `0.0056` n `26`; metal avg `0.0091` n `20`; unknown avg `7.4745` n `944`
- 4h: commodity avg `-0.4882` n `12`; crypto_alt avg `-0.1011` n `234`; crypto_major avg `-0.2833` n `8`; equity avg `0.0168` n `141`; fx avg `0.0056` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0193` n `20`; unknown avg `12.0686` n `836`
- 24h: commodity avg `0.6075` n `12`; crypto_alt avg `4.0495` n `234`; crypto_major avg `1.0755` n `8`; equity avg `-0.3026` n `141`; fx avg `0.0618` n `6`; index avg `-0.1003` n `26`; metal avg `-0.0766` n `20`; unknown avg `24.6733` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
