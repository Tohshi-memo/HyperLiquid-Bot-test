# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T04:07:24.969109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.0659` n `230`; crypto_major avg `-0.1039` n `8`; equity avg `-0.1747` n `96`; fx avg `0.0015` n `6`; index avg `-0.0303` n `25`; metal avg `-0.0648` n `20`; unknown avg `-0.0718` n `768`
- 1h: commodity avg `-0.0206` n `12`; crypto_alt avg `0.0496` n `230`; crypto_major avg `-0.1751` n `8`; equity avg `-0.2221` n `94`; fx avg `0.0028` n `6`; index avg `-0.0529` n `25`; metal avg `-0.0455` n `20`; unknown avg `0.0149` n `768`
- 4h: commodity avg `-0.0657` n `12`; crypto_alt avg `0.0473` n `230`; crypto_major avg `-0.2877` n `8`; equity avg `-1.3645` n `94`; fx avg `-0.0261` n `6`; index avg `-0.2241` n `25`; metal avg `-0.143` n `20`; unknown avg `-0.0107` n `768`
- 24h: commodity avg `-0.117` n `12`; crypto_alt avg `-1.8518` n `230`; crypto_major avg `-2.8074` n `8`; equity avg `-5.4253` n `94`; fx avg `-0.1262` n `6`; index avg `-0.7525` n `25`; metal avg `-0.8436` n `20`; unknown avg `-0.3276` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
