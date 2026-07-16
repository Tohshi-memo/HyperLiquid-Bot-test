# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T03:22:27.544128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `12`; crypto_alt avg `-0.1417` n `230`; crypto_major avg `-0.0721` n `8`; equity avg `-0.0093` n `94`; fx avg `-0.0019` n `6`; index avg `-0.0429` n `25`; metal avg `-0.0224` n `20`; unknown avg `-0.1623` n `768`
- 1h: commodity avg `-0.0711` n `12`; crypto_alt avg `-0.0095` n `230`; crypto_major avg `0.081` n `8`; equity avg `0.2211` n `94`; fx avg `-0.0039` n `6`; index avg `0.0611` n `25`; metal avg `0.0052` n `20`; unknown avg `-0.2334` n `768`
- 4h: commodity avg `-0.114` n `12`; crypto_alt avg `-0.0876` n `230`; crypto_major avg `-0.3152` n `8`; equity avg `-0.2112` n `94`; fx avg `-0.0108` n `6`; index avg `-0.1296` n `25`; metal avg `-0.2033` n `20`; unknown avg `-0.3474` n `766`
- 24h: commodity avg `-0.1288` n `12`; crypto_alt avg `0.3042` n `230`; crypto_major avg `0.2833` n `8`; equity avg `-2.0646` n `93`; fx avg `0.134` n `6`; index avg `-0.4412` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0123` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
