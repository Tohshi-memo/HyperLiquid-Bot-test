# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T15:22:29.977642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0527` n `12`; crypto_alt avg `-0.1979` n `230`; crypto_major avg `-0.2299` n `8`; equity avg `-0.5707` n `102`; fx avg `-0.001` n `6`; index avg `-0.074` n `25`; metal avg `0.0354` n `20`; unknown avg `-0.1428` n `780`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.1131` n `230`; crypto_major avg `-0.5718` n `8`; equity avg `-0.1852` n `102`; fx avg `0.0429` n `6`; index avg `0.018` n `25`; metal avg `0.1721` n `20`; unknown avg `-0.1954` n `780`
- 4h: commodity avg `-0.0394` n `12`; crypto_alt avg `-0.3377` n `230`; crypto_major avg `-1.0847` n `8`; equity avg `-2.5581` n `102`; fx avg `-0.1082` n `6`; index avg `-0.3181` n `25`; metal avg `-0.0619` n `20`; unknown avg `0.7835` n `780`
- 24h: commodity avg `0.1181` n `12`; crypto_alt avg `-0.9571` n `230`; crypto_major avg `-1.8835` n `8`; equity avg `0.4254` n `102`; fx avg `0.0876` n `6`; index avg `0.2499` n `25`; metal avg `-0.1275` n `20`; unknown avg `0.9646` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
