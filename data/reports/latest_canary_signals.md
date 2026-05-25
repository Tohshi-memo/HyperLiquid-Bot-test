# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T05:07:15.495104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `12`; crypto_alt avg `0.1963` n `228`; crypto_major avg `0.0857` n `8`; equity avg `0.0199` n `67`; fx avg `-0.0144` n `6`; index avg `0.0084` n `23`; metal avg `-0.039` n `18`; unknown avg `-0.0867` n `397`
- 1h: commodity avg `-0.0416` n `12`; crypto_alt avg `1.0212` n `228`; crypto_major avg `0.8219` n `8`; equity avg `0.1129` n `67`; fx avg `-0.0188` n `6`; index avg `-0.0282` n `23`; metal avg `0.1306` n `18`; unknown avg `-0.2212` n `397`
- 4h: commodity avg `-0.5718` n `12`; crypto_alt avg `0.9641` n `228`; crypto_major avg `0.4654` n `8`; equity avg `0.393` n `67`; fx avg `-0.0571` n `6`; index avg `0.164` n `23`; metal avg `-0.0929` n `18`; unknown avg `-0.0876` n `396`
- 24h: commodity avg `-0.0325` n `12`; crypto_alt avg `0.1438` n `228`; crypto_major avg `0.5741` n `8`; equity avg `0.4903` n `67`; fx avg `-0.1043` n `6`; index avg `-0.1081` n `23`; metal avg `0.5792` n `18`; unknown avg `-0.104` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
