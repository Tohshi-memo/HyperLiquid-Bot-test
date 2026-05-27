# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T03:37:18.322840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1271` n `12`; crypto_alt avg `-0.0997` n `228`; crypto_major avg `-0.1558` n `8`; equity avg `-0.0253` n `67`; fx avg `-0.0023` n `6`; index avg `-0.0678` n `23`; metal avg `-0.2411` n `18`; unknown avg `-0.1889` n `418`
- 1h: commodity avg `-0.1104` n `12`; crypto_alt avg `0.1362` n `228`; crypto_major avg `0.1408` n `8`; equity avg `-0.0497` n `67`; fx avg `-0.0087` n `6`; index avg `-0.1436` n `23`; metal avg `-0.0535` n `18`; unknown avg `-0.63` n `418`
- 4h: commodity avg `-0.3252` n `12`; crypto_alt avg `-0.4071` n `228`; crypto_major avg `0.1083` n `8`; equity avg `0.1072` n `67`; fx avg `-0.0531` n `6`; index avg `0.0664` n `23`; metal avg `-0.4604` n `18`; unknown avg `-0.4188` n `418`
- 24h: commodity avg `0.0122` n `12`; crypto_alt avg `-0.3977` n `228`; crypto_major avg `-0.2211` n `8`; equity avg `0.6865` n `67`; fx avg `-0.0741` n `6`; index avg `0.9395` n `23`; metal avg `-0.4231` n `18`; unknown avg `0.5451` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
