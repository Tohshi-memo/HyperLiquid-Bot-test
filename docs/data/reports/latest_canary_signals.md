# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T11:37:24.777522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0218` n `12`; crypto_alt avg `0.0593` n `230`; crypto_major avg `0.0445` n `8`; equity avg `-0.0069` n `93`; fx avg `0.0071` n `6`; index avg `-0.0041` n `25`; metal avg `0.0353` n `20`; unknown avg `0.0132` n `767`
- 1h: commodity avg `-0.1145` n `12`; crypto_alt avg `0.0281` n `230`; crypto_major avg `0.1286` n `8`; equity avg `0.0106` n `93`; fx avg `0.024` n `6`; index avg `0.0052` n `25`; metal avg `-0.0274` n `20`; unknown avg `0.0078` n `767`
- 4h: commodity avg `-0.1198` n `12`; crypto_alt avg `0.4087` n `230`; crypto_major avg `0.3563` n `8`; equity avg `-0.1702` n `93`; fx avg `-0.0017` n `6`; index avg `-0.0367` n `25`; metal avg `-0.0088` n `20`; unknown avg `-0.0674` n `765`
- 24h: commodity avg `-0.0202` n `12`; crypto_alt avg `1.6473` n `230`; crypto_major avg `2.9825` n `8`; equity avg `1.2929` n `92`; fx avg `0.0263` n `6`; index avg `0.3392` n `25`; metal avg `0.218` n `20`; unknown avg `0.2408` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
