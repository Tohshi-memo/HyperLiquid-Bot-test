# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T06:22:15.861303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.078` n `12`; crypto_alt avg `-0.4316` n `228`; crypto_major avg `-0.3243` n `8`; equity avg `-0.053` n `67`; fx avg `0.0026` n `6`; index avg `-0.0113` n `23`; metal avg `0.0059` n `18`; unknown avg `0.7599` n `397`
- 1h: commodity avg `0.3197` n `12`; crypto_alt avg `-0.131` n `228`; crypto_major avg `-0.201` n `8`; equity avg `-0.1294` n `67`; fx avg `0.0253` n `6`; index avg `-0.0078` n `23`; metal avg `-0.1831` n `18`; unknown avg `0.8419` n `387`
- 4h: commodity avg `-0.3464` n `12`; crypto_alt avg `0.6134` n `228`; crypto_major avg `0.2613` n `8`; equity avg `0.2711` n `67`; fx avg `0.012` n `6`; index avg `0.1221` n `23`; metal avg `-0.2612` n `18`; unknown avg `1.0778` n `386`
- 24h: commodity avg `0.2637` n `12`; crypto_alt avg `0.0039` n `228`; crypto_major avg `0.3193` n `8`; equity avg `0.587` n `67`; fx avg `-0.0448` n `6`; index avg `-0.0474` n `23`; metal avg `0.2165` n `18`; unknown avg `-0.1424` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
