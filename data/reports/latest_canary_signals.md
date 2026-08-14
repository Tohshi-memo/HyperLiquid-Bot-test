# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T10:22:29.602490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.0104` n `230`; crypto_major avg `-0.0424` n `8`; equity avg `-0.0176` n `113`; fx avg `0.0067` n `6`; index avg `-0.0072` n `25`; metal avg `-0.0166` n `20`; unknown avg `0.0284` n `787`
- 1h: commodity avg `-0.0701` n `12`; crypto_alt avg `-0.2174` n `230`; crypto_major avg `-0.2034` n `8`; equity avg `0.169` n `113`; fx avg `0.0219` n `6`; index avg `0.0254` n `25`; metal avg `0.0052` n `20`; unknown avg `0.0681` n `787`
- 4h: commodity avg `-0.1036` n `12`; crypto_alt avg `-0.3515` n `230`; crypto_major avg `-0.3027` n `8`; equity avg `0.569` n `113`; fx avg `0.0046` n `6`; index avg `0.0713` n `25`; metal avg `0.1196` n `20`; unknown avg `0.0801` n `787`
- 24h: commodity avg `-0.0986` n `12`; crypto_alt avg `-0.8579` n `230`; crypto_major avg `-0.8029` n `8`; equity avg `1.7787` n `113`; fx avg `-0.0609` n `6`; index avg `0.3505` n `25`; metal avg `-0.1708` n `20`; unknown avg `0.991` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
