# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T13:37:28.956507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `13`; crypto_alt avg `-0.1557` n `235`; crypto_major avg `-0.0657` n `8`; equity avg `-0.1286` n `144`; fx avg `-0.0313` n `6`; index avg `0.0321` n `26`; metal avg `-0.0696` n `20`; unknown avg `14.8248` n `1079`
- 1h: commodity avg `-0.1944` n `13`; crypto_alt avg `-0.2403` n `235`; crypto_major avg `0.0047` n `8`; equity avg `-0.0888` n `144`; fx avg `-0.048` n `6`; index avg `0.0309` n `26`; metal avg `-0.1031` n `20`; unknown avg `9.5606` n `1077`
- 4h: commodity avg `-0.2319` n `13`; crypto_alt avg `-0.1381` n `235`; crypto_major avg `-0.1036` n `8`; equity avg `-0.0858` n `144`; fx avg `-0.0402` n `6`; index avg `0.0731` n `26`; metal avg `-0.0821` n `20`; unknown avg `3.8704` n `1071`
- 24h: commodity avg `-0.4408` n `13`; crypto_alt avg `0.782` n `235`; crypto_major avg `0.7104` n `8`; equity avg `-0.0095` n `144`; fx avg `-0.0899` n `6`; index avg `-0.0109` n `26`; metal avg `0.1996` n `20`; unknown avg `-0.2672` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2118`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1938`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
