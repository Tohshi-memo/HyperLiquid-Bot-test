# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T21:22:19.325219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.1911` n `228`; crypto_major avg `0.1413` n `8`; equity avg `-0.0064` n `69`; fx avg `0.0063` n `6`; index avg `0.1438` n `23`; metal avg `0.0265` n `18`; unknown avg `-0.1006` n `421`
- 1h: commodity avg `-0.0734` n `12`; crypto_alt avg `0.3358` n `228`; crypto_major avg `0.3974` n `8`; equity avg `0.0737` n `69`; fx avg `-0.0047` n `6`; index avg `0.2117` n `23`; metal avg `0.0239` n `18`; unknown avg `0.919` n `421`
- 4h: commodity avg `-0.1108` n `12`; crypto_alt avg `1.1917` n `228`; crypto_major avg `0.674` n `8`; equity avg `0.1691` n `69`; fx avg `-0.0181` n `6`; index avg `0.2422` n `23`; metal avg `-0.0253` n `18`; unknown avg `1.3368` n `421`
- 24h: commodity avg `0.4706` n `12`; crypto_alt avg `-0.6466` n `228`; crypto_major avg `-0.2074` n `8`; equity avg `0.7523` n `69`; fx avg `-0.0354` n `6`; index avg `0.2662` n `23`; metal avg `-0.147` n `18`; unknown avg `1.7618` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2874`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1974`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
