# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T11:22:27.269860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4515` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0306` n `12`; crypto_alt avg `-0.6977` n `234`; crypto_major avg `-0.4611` n `8`; equity avg `-0.1822` n `140`; fx avg `0.0082` n `6`; index avg `-0.0201` n `26`; metal avg `-0.0599` n `20`; unknown avg `15.8432` n `946`
- 1h: commodity avg `0.1324` n `12`; crypto_alt avg `-0.5518` n `234`; crypto_major avg `-0.2001` n `8`; equity avg `-0.3435` n `140`; fx avg `0.0249` n `6`; index avg `-0.0446` n `26`; metal avg `-0.0858` n `20`; unknown avg `18.3895` n `944`
- 4h: commodity avg `0.1527` n `12`; crypto_alt avg `-1.3354` n `234`; crypto_major avg `-1.5208` n `8`; equity avg `-0.4286` n `140`; fx avg `0.004` n `6`; index avg `-0.0693` n `26`; metal avg `-0.2133` n `20`; unknown avg `17.3738` n `937`
- 24h: commodity avg `0.6257` n `12`; crypto_alt avg `2.9285` n `234`; crypto_major avg `0.2049` n `8`; equity avg `0.5396` n `140`; fx avg `0.0374` n `6`; index avg `0.0378` n `26`; metal avg `-0.1419` n `20`; unknown avg `25.6238` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
