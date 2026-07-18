# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T18:22:26.683891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0704` n `12`; crypto_alt avg `-0.0497` n `230`; crypto_major avg `-0.0098` n `8`; equity avg `0.0282` n `96`; fx avg `-0.0207` n `6`; index avg `-0.0114` n `25`; metal avg `-0.0166` n `20`; unknown avg `0.0955` n `770`
- 1h: commodity avg `0.1022` n `12`; crypto_alt avg `0.1722` n `230`; crypto_major avg `0.2918` n `8`; equity avg `0.0172` n `96`; fx avg `-0.0166` n `6`; index avg `-0.0145` n `25`; metal avg `-0.0276` n `20`; unknown avg `0.0851` n `770`
- 4h: commodity avg `0.2059` n `12`; crypto_alt avg `0.3078` n `230`; crypto_major avg `0.4337` n `8`; equity avg `-0.0058` n `96`; fx avg `-0.0803` n `6`; index avg `-0.0164` n `25`; metal avg `-0.0681` n `20`; unknown avg `0.0428` n `770`
- 24h: commodity avg `0.3749` n `12`; crypto_alt avg `-0.6008` n `230`; crypto_major avg `0.3807` n `8`; equity avg `-0.8229` n `96`; fx avg `-0.1325` n `6`; index avg `-0.0539` n `25`; metal avg `-0.0161` n `20`; unknown avg `-0.0938` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
