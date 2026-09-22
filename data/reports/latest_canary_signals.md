# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T21:22:34.583325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0253` n `234`; crypto_major avg `-0.1376` n `8`; equity avg `-0.0082` n `140`; fx avg `-0.004` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0166` n `20`; unknown avg `0.2082` n `944`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `0.1617` n `234`; crypto_major avg `-0.0707` n `8`; equity avg `0.0418` n `140`; fx avg `-0.0001` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0315` n `20`; unknown avg `0.0232` n `942`
- 4h: commodity avg `-0.0925` n `12`; crypto_alt avg `0.4193` n `234`; crypto_major avg `-0.1537` n `8`; equity avg `0.295` n `140`; fx avg `-0.0255` n `6`; index avg `0.0559` n `26`; metal avg `0.248` n `20`; unknown avg `0.783` n `906`
- 24h: commodity avg `0.158` n `12`; crypto_alt avg `2.2387` n `234`; crypto_major avg `0.4035` n `8`; equity avg `0.8839` n `140`; fx avg `-0.2989` n `6`; index avg `0.1264` n `26`; metal avg `0.2705` n `20`; unknown avg `1.4583` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
