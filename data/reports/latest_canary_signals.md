# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T16:07:25.266440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.2307` n `230`; crypto_major avg `0.2144` n `8`; equity avg `0.0049` n `121`; fx avg `-0.0026` n `6`; index avg `-0.005` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0451` n `794`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `0.1672` n `230`; crypto_major avg `0.2299` n `8`; equity avg `-0.0216` n `121`; fx avg `0.0132` n `6`; index avg `0.0055` n `25`; metal avg `0.0162` n `20`; unknown avg `0.1354` n `794`
- 4h: commodity avg `-0.0422` n `12`; crypto_alt avg `-0.9206` n `230`; crypto_major avg `-0.9322` n `8`; equity avg `-0.0914` n `121`; fx avg `-0.0075` n `6`; index avg `-0.0057` n `25`; metal avg `0.017` n `20`; unknown avg `0.0708` n `794`
- 24h: commodity avg `-0.0722` n `12`; crypto_alt avg `0.208` n `230`; crypto_major avg `2.539` n `8`; equity avg `-0.5422` n `121`; fx avg `0.0455` n `6`; index avg `-0.091` n `25`; metal avg `-0.0998` n `20`; unknown avg `1.8288` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
