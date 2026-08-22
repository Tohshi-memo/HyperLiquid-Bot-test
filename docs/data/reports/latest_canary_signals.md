# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T19:41:46.785472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.1954` n `230`; crypto_major avg `0.2349` n `8`; equity avg `0.0174` n `121`; fx avg `0.0047` n `6`; index avg `0.0014` n `25`; metal avg `0.0063` n `20`; unknown avg `0.0312` n `794`
- 1h: commodity avg `0.0107` n `12`; crypto_alt avg `-0.146` n `230`; crypto_major avg `0.0436` n `8`; equity avg `0.0385` n `121`; fx avg `0.0124` n `6`; index avg `-0.0043` n `25`; metal avg `0.0043` n `20`; unknown avg `0.221` n `794`
- 4h: commodity avg `0.0504` n `12`; crypto_alt avg `0.9399` n `230`; crypto_major avg `1.4683` n `8`; equity avg `0.1247` n `121`; fx avg `0.0324` n `6`; index avg `-0.0049` n `25`; metal avg `0.0101` n `20`; unknown avg `1.2824` n `794`
- 24h: commodity avg `0.018` n `12`; crypto_alt avg `1.8019` n `230`; crypto_major avg `4.2337` n `8`; equity avg `-0.3868` n `121`; fx avg `0.0592` n `6`; index avg `-0.0489` n `25`; metal avg `-0.0904` n `20`; unknown avg `2.0065` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
