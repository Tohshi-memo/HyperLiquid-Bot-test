# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T03:07:28.140828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0095` n `230`; crypto_major avg `-0.0118` n `8`; equity avg `0.0163` n `114`; fx avg `-0.0213` n `6`; index avg `0.0066` n `25`; metal avg `0.0324` n `20`; unknown avg `-0.021` n `792`
- 1h: commodity avg `-0.1097` n `12`; crypto_alt avg `0.4558` n `230`; crypto_major avg `0.5056` n `8`; equity avg `0.4487` n `114`; fx avg `0.0135` n `6`; index avg `0.036` n `25`; metal avg `0.0177` n `20`; unknown avg `0.3786` n `792`
- 4h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.794` n `230`; crypto_major avg `1.1018` n `8`; equity avg `0.5517` n `114`; fx avg `-0.0312` n `6`; index avg `0.0363` n `25`; metal avg `0.1599` n `20`; unknown avg `0.778` n `791`
- 24h: commodity avg `-0.1498` n `12`; crypto_alt avg `0.238` n `230`; crypto_major avg `0.5698` n `8`; equity avg `0.7402` n `114`; fx avg `-0.0425` n `6`; index avg `0.0704` n `25`; metal avg `0.2362` n `20`; unknown avg `0.1208` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
