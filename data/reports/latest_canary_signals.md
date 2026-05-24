# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T14:52:13.552424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `0.1723` n `228`; crypto_major avg `0.0609` n `8`; equity avg `0.0645` n `67`; fx avg `0.0` n `6`; index avg `0.0349` n `23`; metal avg `0.0346` n `18`; unknown avg `0.0313` n `396`
- 1h: commodity avg `0.7094` n `12`; crypto_alt avg `-0.6156` n `228`; crypto_major avg `-0.7188` n `8`; equity avg `-0.3262` n `67`; fx avg `-0.0055` n `6`; index avg `-0.1839` n `23`; metal avg `-0.3087` n `18`; unknown avg `0.7622` n `396`
- 4h: commodity avg `0.8918` n `12`; crypto_alt avg `-1.0632` n `228`; crypto_major avg `-0.6899` n `8`; equity avg `-0.2317` n `67`; fx avg `0.0176` n `6`; index avg `-0.3099` n `23`; metal avg `-0.5465` n `18`; unknown avg `1.6011` n `396`
- 24h: commodity avg `-1.0882` n `12`; crypto_alt avg `1.1151` n `228`; crypto_major avg `2.6685` n `8`; equity avg `1.7395` n `67`; fx avg `0.0805` n `6`; index avg `0.5484` n `23`; metal avg `0.6418` n `18`; unknown avg `2.3289` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
