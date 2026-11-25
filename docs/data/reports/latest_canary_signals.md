# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T10:37:26.036520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1197` n `13`; crypto_alt avg `-0.0321` n `239`; crypto_major avg `0.0817` n `8`; equity avg `-0.0161` n `168`; fx avg `0.0039` n `6`; index avg `0.0017` n `27`; metal avg `-0.0116` n `20`; unknown avg `-0.0328` n `1265`
- 1h: commodity avg `-0.0912` n `13`; crypto_alt avg `-0.2011` n `239`; crypto_major avg `0.0488` n `8`; equity avg `-0.2035` n `168`; fx avg `-0.0074` n `6`; index avg `-0.0532` n `27`; metal avg `-0.0359` n `20`; unknown avg `53.8706` n `1261`
- 4h: commodity avg `0.1317` n `13`; crypto_alt avg `-1.1331` n `239`; crypto_major avg `-0.9115` n `8`; equity avg `-1.5297` n `168`; fx avg `-0.0047` n `6`; index avg `-0.1807` n `27`; metal avg `-0.0009` n `20`; unknown avg `4.1127` n `1235`
- 24h: commodity avg `0.2447` n `13`; crypto_alt avg `-1.983` n `239`; crypto_major avg `-2.5778` n `8`; equity avg `-4.7671` n `167`; fx avg `0.0086` n `6`; index avg `-0.4286` n `27`; metal avg `-0.9018` n `20`; unknown avg `485.5786` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
