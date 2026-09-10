# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T10:37:28.266826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.046` n `12`; crypto_alt avg `-0.0586` n `233`; crypto_major avg `-0.0047` n `8`; equity avg `-0.0113` n `134`; fx avg `0.0059` n `6`; index avg `-0.0079` n `26`; metal avg `-0.199` n `20`; unknown avg `1.4909` n `797`
- 1h: commodity avg `-0.1058` n `12`; crypto_alt avg `-0.0889` n `233`; crypto_major avg `-0.0173` n `8`; equity avg `0.0305` n `134`; fx avg `-0.0047` n `6`; index avg `0.0201` n `26`; metal avg `-0.2667` n `20`; unknown avg `0.6805` n `795`
- 4h: commodity avg `0.2436` n `12`; crypto_alt avg `-0.6187` n `233`; crypto_major avg `-0.355` n `8`; equity avg `-0.3733` n `134`; fx avg `0.0644` n `6`; index avg `-0.0822` n `26`; metal avg `-0.5074` n `20`; unknown avg `-0.0315` n `787`
- 24h: commodity avg `-0.0802` n `12`; crypto_alt avg `-4.199` n `233`; crypto_major avg `-2.7904` n `8`; equity avg `-0.9143` n `134`; fx avg `0.1016` n `6`; index avg `-0.0372` n `26`; metal avg `-0.2347` n `20`; unknown avg `-0.2985` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
