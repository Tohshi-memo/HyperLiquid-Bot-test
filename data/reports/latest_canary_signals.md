# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T15:37:25.206070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0491` n `12`; crypto_alt avg `-0.0454` n `231`; crypto_major avg `-0.043` n `8`; equity avg `-0.0151` n `128`; fx avg `0.0007` n `6`; index avg `-0.0032` n `26`; metal avg `0.0095` n `20`; unknown avg `-0.0106` n `792`
- 1h: commodity avg `-0.0748` n `12`; crypto_alt avg `0.1216` n `231`; crypto_major avg `0.2689` n `8`; equity avg `-0.01` n `128`; fx avg `-0.0016` n `6`; index avg `0.0075` n `26`; metal avg `0.0413` n `20`; unknown avg `-0.058` n `782`
- 4h: commodity avg `-0.0709` n `12`; crypto_alt avg `0.8631` n `231`; crypto_major avg `0.7401` n `8`; equity avg `-0.0411` n `128`; fx avg `-0.0023` n `6`; index avg `-0.0` n `26`; metal avg `0.0466` n `20`; unknown avg `0.4969` n `768`
- 24h: commodity avg `-0.0215` n `12`; crypto_alt avg `-1.446` n `231`; crypto_major avg `-1.4548` n `8`; equity avg `-1.0128` n `128`; fx avg `-0.0673` n `6`; index avg `-0.1975` n `26`; metal avg `-0.6172` n `20`; unknown avg `-0.3445` n `732`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2101`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
