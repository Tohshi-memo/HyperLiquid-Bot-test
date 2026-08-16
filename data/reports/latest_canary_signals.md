# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T18:51:05.364683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `0.0425` n `8`; equity avg `0.0099` n `114`; fx avg `0.0032` n `6`; index avg `0.0125` n `25`; metal avg `0.0053` n `20`; unknown avg `-0.0065` n `791`
- 1h: commodity avg `0.0498` n `12`; crypto_alt avg `-0.1137` n `230`; crypto_major avg `-0.0844` n `8`; equity avg `-0.0033` n `114`; fx avg `0.0019` n `6`; index avg `0.0096` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0042` n `791`
- 4h: commodity avg `0.0883` n `12`; crypto_alt avg `-0.1326` n `230`; crypto_major avg `0.0534` n `8`; equity avg `0.0787` n `114`; fx avg `0.0107` n `6`; index avg `0.0041` n `25`; metal avg `0.0181` n `20`; unknown avg `-0.0283` n `791`
- 24h: commodity avg `0.0692` n `12`; crypto_alt avg `-0.2956` n `230`; crypto_major avg `0.0539` n `8`; equity avg `0.2935` n `114`; fx avg `-0.0021` n `6`; index avg `0.0281` n `25`; metal avg `0.053` n `20`; unknown avg `0.1052` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2151`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
