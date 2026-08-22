# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T17:07:26.323252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `-0.0484` n `230`; crypto_major avg `-0.0786` n `8`; equity avg `0.0189` n `121`; fx avg `0.0031` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0468` n `794`
- 1h: commodity avg `0.0084` n `12`; crypto_alt avg `0.7617` n `230`; crypto_major avg `0.7895` n `8`; equity avg `0.044` n `121`; fx avg `0.0101` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.1959` n `794`
- 4h: commodity avg `-0.0633` n `12`; crypto_alt avg `0.269` n `230`; crypto_major avg `-0.0419` n `8`; equity avg `-0.0439` n `121`; fx avg `0.0048` n `6`; index avg `-0.0039` n `25`; metal avg `0.0058` n `20`; unknown avg `0.2749` n `794`
- 24h: commodity avg `-0.0808` n `12`; crypto_alt avg `0.3998` n `230`; crypto_major avg `2.479` n `8`; equity avg `-0.5511` n `121`; fx avg `0.0554` n `6`; index avg `-0.0892` n `25`; metal avg `-0.1983` n `20`; unknown avg `1.6036` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
