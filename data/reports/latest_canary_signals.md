# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T04:07:25.089487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.1421` n `231`; crypto_major avg `-0.1418` n `8`; equity avg `-0.085` n `127`; fx avg `0.0105` n `6`; index avg `-0.0181` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.0047` n `792`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `0.1196` n `231`; crypto_major avg `0.1163` n `8`; equity avg `-0.1412` n `127`; fx avg `-0.0115` n `6`; index avg `-0.0311` n `26`; metal avg `-0.0349` n `20`; unknown avg `-0.1093` n `792`
- 4h: commodity avg `-0.0033` n `12`; crypto_alt avg `-1.2531` n `231`; crypto_major avg `-0.8878` n `8`; equity avg `0.0782` n `127`; fx avg `-0.0528` n `6`; index avg `0.0284` n `26`; metal avg `-0.0997` n `20`; unknown avg `0.0155` n `792`
- 24h: commodity avg `0.2946` n `12`; crypto_alt avg `0.2368` n `231`; crypto_major avg `1.5923` n `8`; equity avg `-0.1826` n `127`; fx avg `-0.0168` n `6`; index avg `0.0234` n `26`; metal avg `-0.1076` n `20`; unknown avg `0.5588` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
