# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T05:37:33.412221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.1126` n `230`; crypto_major avg `-0.1606` n `8`; equity avg `0.0484` n `114`; fx avg `0.011` n `6`; index avg `0.0095` n `25`; metal avg `0.0208` n `20`; unknown avg `-0.1402` n `792`
- 1h: commodity avg `-0.0565` n `12`; crypto_alt avg `-0.0872` n `230`; crypto_major avg `-0.0365` n `8`; equity avg `0.1112` n `114`; fx avg `0.019` n `6`; index avg `0.0162` n `25`; metal avg `0.0595` n `20`; unknown avg `-0.0388` n `792`
- 4h: commodity avg `-0.0883` n `12`; crypto_alt avg `0.3197` n `230`; crypto_major avg `0.307` n `8`; equity avg `0.6608` n `114`; fx avg `0.0499` n `6`; index avg `0.0796` n `25`; metal avg `0.0215` n `20`; unknown avg `0.3279` n `792`
- 24h: commodity avg `-0.1809` n `12`; crypto_alt avg `0.4052` n `230`; crypto_major avg `0.688` n `8`; equity avg `0.9068` n `114`; fx avg `-0.0159` n `6`; index avg `0.1006` n `25`; metal avg `0.2231` n `20`; unknown avg `0.0133` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
