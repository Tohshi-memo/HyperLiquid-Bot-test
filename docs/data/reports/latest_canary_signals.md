# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T20:22:25.517411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `12`; crypto_alt avg `-0.2263` n `230`; crypto_major avg `0.0283` n `8`; equity avg `0.0359` n `121`; fx avg `0.0079` n `6`; index avg `0.0002` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0152` n `794`
- 1h: commodity avg `0.0657` n `12`; crypto_alt avg `0.1054` n `230`; crypto_major avg `0.5726` n `8`; equity avg `0.0914` n `121`; fx avg `0.0096` n `6`; index avg `-0.001` n `25`; metal avg `0.007` n `20`; unknown avg `0.0777` n `794`
- 4h: commodity avg `0.0689` n `12`; crypto_alt avg `0.2088` n `230`; crypto_major avg `1.3104` n `8`; equity avg `0.1494` n `121`; fx avg `0.019` n `6`; index avg `-0.0113` n `25`; metal avg `0.0003` n `20`; unknown avg `1.2792` n `794`
- 24h: commodity avg `0.0486` n `12`; crypto_alt avg `0.9162` n `230`; crypto_major avg `3.9989` n `8`; equity avg `-0.3402` n `121`; fx avg `0.0694` n `6`; index avg `-0.0451` n `25`; metal avg `-0.0852` n `20`; unknown avg `3.1347` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
