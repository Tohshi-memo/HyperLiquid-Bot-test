# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T20:37:30.778647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0565` n `230`; crypto_major avg `-0.0401` n `8`; equity avg `0.0119` n `96`; fx avg `-0.0102` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.0149` n `769`
- 1h: commodity avg `0.1194` n `12`; crypto_alt avg `-0.1138` n `230`; crypto_major avg `-0.1266` n `8`; equity avg `-0.4699` n `96`; fx avg `-0.0421` n `6`; index avg `-0.0872` n `25`; metal avg `-0.0239` n `20`; unknown avg `-0.0173` n `769`
- 4h: commodity avg `0.1171` n `12`; crypto_alt avg `-0.2127` n `230`; crypto_major avg `0.206` n `8`; equity avg `-0.6813` n `96`; fx avg `-0.028` n `6`; index avg `-0.1157` n `25`; metal avg `-0.0482` n `20`; unknown avg `0.2207` n `769`
- 24h: commodity avg `0.6996` n `12`; crypto_alt avg `-1.288` n `230`; crypto_major avg `-1.2925` n `8`; equity avg `-1.4538` n `94`; fx avg `0.0703` n `6`; index avg `-0.2839` n `25`; metal avg `-0.021` n `20`; unknown avg `-0.053` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
