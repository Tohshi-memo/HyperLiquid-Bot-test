# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T12:46:11.310870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `-0.0024` n `230`; crypto_major avg `0.0352` n `8`; equity avg `-0.0021` n `92`; fx avg `0.0029` n `6`; index avg `0.0037` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.002` n `765`
- 1h: commodity avg `-0.0773` n `12`; crypto_alt avg `0.0282` n `230`; crypto_major avg `0.0768` n `8`; equity avg `0.0063` n `92`; fx avg `0.0003` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0124` n `20`; unknown avg `-0.0326` n `765`
- 4h: commodity avg `-0.0659` n `12`; crypto_alt avg `0.0675` n `230`; crypto_major avg `0.3414` n `8`; equity avg `0.048` n `92`; fx avg `-0.0014` n `6`; index avg `-0.0132` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.0662` n `763`
- 24h: commodity avg `0.4135` n `12`; crypto_alt avg `-0.9756` n `230`; crypto_major avg `-0.4107` n `8`; equity avg `-0.0725` n `92`; fx avg `0.0129` n `6`; index avg `-0.1102` n `25`; metal avg `-0.0968` n `20`; unknown avg `0.0938` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
