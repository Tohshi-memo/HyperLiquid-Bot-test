# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T20:37:31.289612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `0.0735` n `230`; crypto_major avg `0.0184` n `8`; equity avg `0.0221` n `108`; fx avg `-0.0025` n `6`; index avg `0.0049` n `25`; metal avg `0.0131` n `20`; unknown avg `-0.0339` n `782`
- 1h: commodity avg `-0.0427` n `12`; crypto_alt avg `0.0831` n `230`; crypto_major avg `-0.0998` n `8`; equity avg `-0.7923` n `108`; fx avg `0.0132` n `6`; index avg `-0.079` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.0034` n `782`
- 4h: commodity avg `-0.1901` n `12`; crypto_alt avg `0.16` n `230`; crypto_major avg `0.1528` n `8`; equity avg `-0.9946` n `108`; fx avg `-0.0055` n `6`; index avg `-0.0928` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.1302` n `782`
- 24h: commodity avg `-0.0131` n `12`; crypto_alt avg `0.7131` n `230`; crypto_major avg `0.8488` n `8`; equity avg `-0.2571` n `108`; fx avg `-0.0441` n `6`; index avg `-0.0747` n `25`; metal avg `0.8122` n `20`; unknown avg `0.7257` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
