# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T19:46:47.511729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0063` n `230`; crypto_major avg `0.0051` n `8`; equity avg `0.0053` n `114`; fx avg `0.002` n `6`; index avg `0.0061` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.0404` n `792`
- 1h: commodity avg `0.0511` n `12`; crypto_alt avg `-0.1012` n `230`; crypto_major avg `-0.1308` n `8`; equity avg `-0.1971` n `114`; fx avg `0.0006` n `6`; index avg `-0.0203` n `25`; metal avg `0.0477` n `20`; unknown avg `0.1133` n `792`
- 4h: commodity avg `0.3573` n `12`; crypto_alt avg `-0.2267` n `230`; crypto_major avg `-0.2706` n `8`; equity avg `-0.504` n `114`; fx avg `-0.0003` n `6`; index avg `-0.1234` n `25`; metal avg `-0.0879` n `20`; unknown avg `0.2054` n `792`
- 24h: commodity avg `0.3387` n `12`; crypto_alt avg `-0.0863` n `230`; crypto_major avg `0.8154` n `8`; equity avg `1.1699` n `114`; fx avg `0.0257` n `6`; index avg `0.0729` n `25`; metal avg `0.2055` n `20`; unknown avg `0.2546` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
