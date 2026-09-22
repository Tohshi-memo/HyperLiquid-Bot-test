# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T20:52:32.145571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0293` n `12`; crypto_alt avg `-0.1107` n `234`; crypto_major avg `-0.1547` n `8`; equity avg `-0.0092` n `140`; fx avg `0.0076` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0019` n `20`; unknown avg `4.1355` n `944`
- 1h: commodity avg `0.0955` n `12`; crypto_alt avg `0.2679` n `234`; crypto_major avg `-0.0647` n `8`; equity avg `-0.0993` n `140`; fx avg `-0.0232` n `6`; index avg `-0.0538` n `26`; metal avg `-0.085` n `20`; unknown avg `4.5625` n `906`
- 4h: commodity avg `-0.1367` n `12`; crypto_alt avg `0.8591` n `234`; crypto_major avg `0.1592` n `8`; equity avg `0.41` n `140`; fx avg `-0.0081` n `6`; index avg `0.0387` n `26`; metal avg `0.2659` n `20`; unknown avg `5.6096` n `906`
- 24h: commodity avg `0.1494` n `12`; crypto_alt avg `2.0457` n `234`; crypto_major avg `-0.0179` n `8`; equity avg `0.9459` n `140`; fx avg `-0.2979` n `6`; index avg `0.1177` n `26`; metal avg `0.2891` n `20`; unknown avg `1.0089` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
