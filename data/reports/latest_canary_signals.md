# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T20:52:21.649111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.0983` n `228`; crypto_major avg `-0.1171` n `8`; equity avg `-0.0033` n `65`; fx avg `0.0031` n `5`; index avg `-0.0484` n `23`; metal avg `-0.0232` n `18`; unknown avg `0.2138` n `375`
- 1h: commodity avg `-0.0847` n `12`; crypto_alt avg `-0.0424` n `228`; crypto_major avg `-0.1657` n `8`; equity avg `0.4487` n `65`; fx avg `0.021` n `5`; index avg `0.0079` n `23`; metal avg `-0.1959` n `18`; unknown avg `0.1108` n `375`
- 4h: commodity avg `-0.5892` n `12`; crypto_alt avg `1.0483` n `228`; crypto_major avg `1.0787` n `8`; equity avg `1.2929` n `65`; fx avg `0.0481` n `5`; index avg `0.2274` n `23`; metal avg `0.153` n `18`; unknown avg `0.1452` n `375`
- 24h: commodity avg `-0.6312` n `12`; crypto_alt avg `3.2052` n `228`; crypto_major avg `1.3121` n `8`; equity avg `3.6166` n `65`; fx avg `0.2081` n `5`; index avg `1.5167` n `23`; metal avg `0.7541` n `18`; unknown avg `0.891` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
