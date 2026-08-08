# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T18:22:26.912255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.0006` n `230`; crypto_major avg `-0.0717` n `8`; equity avg `-0.0016` n `112`; fx avg `0.0029` n `6`; index avg `0.0034` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0139` n `784`
- 1h: commodity avg `-0.0319` n `12`; crypto_alt avg `-0.0427` n `230`; crypto_major avg `-0.1406` n `8`; equity avg `0.0416` n `112`; fx avg `-0.0008` n `6`; index avg `0.0091` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.0175` n `784`
- 4h: commodity avg `-0.0064` n `12`; crypto_alt avg `0.6594` n `230`; crypto_major avg `0.2916` n `8`; equity avg `0.1661` n `112`; fx avg `-0.0022` n `6`; index avg `0.0157` n `25`; metal avg `0.0144` n `20`; unknown avg `0.127` n `784`
- 24h: commodity avg `-0.1968` n `12`; crypto_alt avg `1.5525` n `230`; crypto_major avg `1.4477` n `8`; equity avg `0.9293` n `112`; fx avg `0.0079` n `6`; index avg `0.0987` n `25`; metal avg `0.1336` n `20`; unknown avg `0.1301` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
