# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T18:22:31.032492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `0.186` n `230`; crypto_major avg `0.3441` n `8`; equity avg `-0.0027` n `121`; fx avg `0.0007` n `6`; index avg `0.0021` n `25`; metal avg `0.0024` n `20`; unknown avg `0.5241` n `794`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `0.2134` n `230`; crypto_major avg `0.5982` n `8`; equity avg `0.0334` n `121`; fx avg `-0.0049` n `6`; index avg `0.0035` n `25`; metal avg `0.0063` n `20`; unknown avg `1.2117` n `794`
- 4h: commodity avg `0.0302` n `12`; crypto_alt avg `0.959` n `230`; crypto_major avg `1.0653` n `8`; equity avg `0.0059` n `121`; fx avg `0.0283` n `6`; index avg `0.0044` n `25`; metal avg `0.021` n `20`; unknown avg `1.5683` n `794`
- 24h: commodity avg `-0.1081` n `12`; crypto_alt avg `0.7462` n `230`; crypto_major avg `3.5573` n `8`; equity avg `-0.4065` n `121`; fx avg `0.0384` n `6`; index avg `-0.0406` n `25`; metal avg `-0.1309` n `20`; unknown avg `3.1277` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
