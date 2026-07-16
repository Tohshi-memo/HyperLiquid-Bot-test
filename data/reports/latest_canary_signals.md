# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T11:52:29.321121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1041` n `12`; crypto_alt avg `-0.0127` n `230`; crypto_major avg `0.0298` n `8`; equity avg `-0.2124` n `94`; fx avg `0.0024` n `6`; index avg `-0.0534` n `25`; metal avg `-0.0349` n `20`; unknown avg `-0.0483` n `768`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `-0.0623` n `230`; crypto_major avg `-0.034` n `8`; equity avg `-0.4026` n `94`; fx avg `-0.0049` n `6`; index avg `-0.1003` n `25`; metal avg `-0.0763` n `20`; unknown avg `-0.0356` n `768`
- 4h: commodity avg `0.146` n `12`; crypto_alt avg `-0.2779` n `230`; crypto_major avg `-0.2922` n `8`; equity avg `-0.7159` n `94`; fx avg `-0.0448` n `6`; index avg `-0.1347` n `25`; metal avg `-0.0418` n `20`; unknown avg `-0.2137` n `762`
- 24h: commodity avg `0.1114` n `12`; crypto_alt avg `-0.8004` n `230`; crypto_major avg `-0.9229` n `8`; equity avg `-3.2695` n `93`; fx avg `0.022` n `6`; index avg `-0.5733` n `25`; metal avg `-0.0874` n `20`; unknown avg `-0.0985` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
