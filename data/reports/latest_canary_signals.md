# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T01:22:27.512486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.0349` n `230`; crypto_major avg `0.229` n `8`; equity avg `0.013` n `121`; fx avg `-0.0103` n `6`; index avg `0.0018` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0412` n `794`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `0.4048` n `230`; crypto_major avg `0.8088` n `8`; equity avg `0.0756` n `121`; fx avg `-0.0022` n `6`; index avg `0.0108` n `25`; metal avg `0.0249` n `20`; unknown avg `0.1965` n `794`
- 4h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.204` n `230`; crypto_major avg `0.8773` n `8`; equity avg `0.1949` n `121`; fx avg `0.0194` n `6`; index avg `0.028` n `25`; metal avg `0.0229` n `20`; unknown avg `0.558` n `794`
- 24h: commodity avg `0.0747` n `12`; crypto_alt avg `-2.4265` n `230`; crypto_major avg `1.227` n `8`; equity avg `-0.2196` n `121`; fx avg `0.1077` n `6`; index avg `-0.0366` n `25`; metal avg `-0.0288` n `20`; unknown avg `2.8142` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
