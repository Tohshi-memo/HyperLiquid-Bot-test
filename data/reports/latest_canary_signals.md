# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T16:37:32.184931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `13`; crypto_alt avg `0.2203` n `239`; crypto_major avg `0.2441` n `8`; equity avg `-0.0555` n `156`; fx avg `0.0157` n `6`; index avg `-0.0095` n `27`; metal avg `0.0084` n `20`; unknown avg `18.9429` n `1265`
- 1h: commodity avg `-0.2224` n `13`; crypto_alt avg `-0.3483` n `239`; crypto_major avg `-0.3289` n `8`; equity avg `-1.0533` n `156`; fx avg `0.0136` n `6`; index avg `-0.0859` n `27`; metal avg `0.0849` n `20`; unknown avg `0.3529` n `1253`
- 4h: commodity avg `-0.7029` n `13`; crypto_alt avg `-0.2209` n `238`; crypto_major avg `-0.2408` n `8`; equity avg `-1.2472` n `156`; fx avg `0.0058` n `6`; index avg `0.0059` n `27`; metal avg `0.4665` n `20`; unknown avg `18.6529` n `1253`
- 24h: commodity avg `-1.0888` n `13`; crypto_alt avg `-1.9974` n `238`; crypto_major avg `-0.7328` n `8`; equity avg `-0.7874` n `156`; fx avg `0.2636` n `6`; index avg `0.2086` n `27`; metal avg `0.4276` n `20`; unknown avg `7.5417` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
