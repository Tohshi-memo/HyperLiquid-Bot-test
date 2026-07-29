# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T15:07:36.662524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.74` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.1042` n `230`; crypto_major avg `0.0921` n `8`; equity avg `0.3694` n `102`; fx avg `-0.0055` n `6`; index avg `0.1023` n `25`; metal avg `0.0376` n `20`; unknown avg `-0.0576` n `778`
- 1h: commodity avg `0.2124` n `12`; crypto_alt avg `-0.3154` n `230`; crypto_major avg `-0.2721` n `8`; equity avg `-0.9647` n `102`; fx avg `-0.0079` n `6`; index avg `-0.1683` n `25`; metal avg `0.0219` n `20`; unknown avg `-0.1181` n `777`
- 4h: commodity avg `0.4852` n `12`; crypto_alt avg `-0.5419` n `230`; crypto_major avg `-0.4808` n `8`; equity avg `-1.8138` n `102`; fx avg `0.0065` n `6`; index avg `-0.2953` n `25`; metal avg `-0.1294` n `20`; unknown avg `0.3203` n `777`
- 24h: commodity avg `0.8659` n `12`; crypto_alt avg `-1.5969` n `230`; crypto_major avg `0.6827` n `8`; equity avg `-0.6154` n `102`; fx avg `-0.0489` n `6`; index avg `-0.2858` n `25`; metal avg `-0.1588` n `20`; unknown avg `-0.0215` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
