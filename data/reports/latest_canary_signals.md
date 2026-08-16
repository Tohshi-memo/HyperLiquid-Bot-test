# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T19:37:26.395018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.0674` n `230`; crypto_major avg `0.031` n `8`; equity avg `0.0057` n `114`; fx avg `-0.0055` n `6`; index avg `0.0109` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0093` n `791`
- 1h: commodity avg `0.0317` n `12`; crypto_alt avg `0.0787` n `230`; crypto_major avg `0.1589` n `8`; equity avg `0.0355` n `114`; fx avg `-0.0011` n `6`; index avg `0.0278` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.1424` n `791`
- 4h: commodity avg `0.0701` n `12`; crypto_alt avg `-0.163` n `230`; crypto_major avg `0.0848` n `8`; equity avg `0.057` n `114`; fx avg `-0.001` n `6`; index avg `0.0201` n `25`; metal avg `0.021` n `20`; unknown avg `-0.1448` n `791`
- 24h: commodity avg `0.0461` n `12`; crypto_alt avg `-0.2598` n `230`; crypto_major avg `0.0623` n `8`; equity avg `0.2759` n `114`; fx avg `-0.0063` n `6`; index avg `0.0392` n `25`; metal avg `0.0553` n `20`; unknown avg `0.1667` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
