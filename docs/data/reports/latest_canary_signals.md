# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T19:22:37.178040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0317` n `12`; crypto_alt avg `0.0095` n `230`; crypto_major avg `-0.0061` n `8`; equity avg `-0.0768` n `114`; fx avg `-0.0101` n `6`; index avg `-0.0029` n `25`; metal avg `0.0558` n `20`; unknown avg `0.0133` n `792`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0079` n `230`; crypto_major avg `-0.1652` n `8`; equity avg `-0.2072` n `114`; fx avg `-0.0051` n `6`; index avg `-0.0319` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0386` n `792`
- 4h: commodity avg `0.4283` n `12`; crypto_alt avg `-0.0134` n `230`; crypto_major avg `-0.0367` n `8`; equity avg `-0.5566` n `114`; fx avg `0.0151` n `6`; index avg `-0.1515` n `25`; metal avg `-0.0972` n `20`; unknown avg `0.0628` n `792`
- 24h: commodity avg `0.2999` n `12`; crypto_alt avg `-0.0436` n `230`; crypto_major avg `0.6955` n `8`; equity avg `1.0103` n `114`; fx avg `0.0127` n `6`; index avg `0.0654` n `25`; metal avg `0.197` n `20`; unknown avg `0.1905` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
