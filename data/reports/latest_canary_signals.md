# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T17:22:27.368931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.0409` n `230`; crypto_major avg `-0.0496` n `8`; equity avg `0.0016` n `114`; fx avg `-0.0005` n `6`; index avg `-0.0015` n `25`; metal avg `0.0015` n `20`; unknown avg `0.036` n `791`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `-0.1442` n `230`; crypto_major avg `0.005` n `8`; equity avg `0.0214` n `114`; fx avg `0.0007` n `6`; index avg `0.0007` n `25`; metal avg `0.0166` n `20`; unknown avg `0.2209` n `791`
- 4h: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0477` n `230`; crypto_major avg `0.2643` n `8`; equity avg `0.1409` n `114`; fx avg `0.0101` n `6`; index avg `-0.0024` n `25`; metal avg `0.0198` n `20`; unknown avg `-0.0478` n `791`
- 24h: commodity avg `0.0552` n `12`; crypto_alt avg `-0.3119` n `230`; crypto_major avg `0.1656` n `8`; equity avg `0.3737` n `114`; fx avg `0.0008` n `6`; index avg `0.0305` n `25`; metal avg `0.0623` n `20`; unknown avg `0.1935` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
