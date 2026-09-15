# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T09:37:26.078252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.2002` n `233`; crypto_major avg `0.1071` n `8`; equity avg `0.1355` n `136`; fx avg `-0.0011` n `6`; index avg `0.0425` n `27`; metal avg `0.0496` n `20`; unknown avg `0.0219` n `908`
- 1h: commodity avg `0.0035` n `12`; crypto_alt avg `0.2387` n `233`; crypto_major avg `0.2858` n `8`; equity avg `0.0921` n `136`; fx avg `0.009` n `6`; index avg `0.0239` n `27`; metal avg `0.0133` n `20`; unknown avg `0.1556` n `906`
- 4h: commodity avg `0.084` n `12`; crypto_alt avg `-0.2054` n `233`; crypto_major avg `-0.2243` n `8`; equity avg `-0.1787` n `136`; fx avg `0.0779` n `6`; index avg `-0.0468` n `27`; metal avg `-0.1669` n `20`; unknown avg `17.6189` n `876`
- 24h: commodity avg `0.0742` n `12`; crypto_alt avg `-0.9893` n `233`; crypto_major avg `-0.6495` n `8`; equity avg `0.1056` n `136`; fx avg `0.2388` n `6`; index avg `0.0019` n `27`; metal avg `-0.038` n `20`; unknown avg `-0.0159` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
