# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T18:32:00.445636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `-0.092` n `230`; crypto_major avg `-0.0895` n `8`; equity avg `-0.0959` n `114`; fx avg `0.011` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.2351` n `791`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.1505` n `230`; crypto_major avg `-0.3181` n `8`; equity avg `-0.1527` n `114`; fx avg `-0.0018` n `6`; index avg `0.0023` n `25`; metal avg `-0.038` n `20`; unknown avg `2.0415` n `791`
- 4h: commodity avg `0.0874` n `12`; crypto_alt avg `0.6043` n `230`; crypto_major avg `0.0794` n `8`; equity avg `-0.7245` n `114`; fx avg `0.0559` n `6`; index avg `-0.094` n `25`; metal avg `-0.0669` n `20`; unknown avg `38.0349` n `787`
- 24h: commodity avg `0.2819` n `12`; crypto_alt avg `0.5808` n `230`; crypto_major avg `-0.6577` n `8`; equity avg `-0.7031` n `114`; fx avg `0.0705` n `6`; index avg `-0.1144` n `25`; metal avg `0.1172` n `20`; unknown avg `0.4222` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
