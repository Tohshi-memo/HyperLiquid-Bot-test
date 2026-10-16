# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T17:37:30.979526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2369` n `13`; crypto_alt avg `0.8263` n `236`; crypto_major avg `0.7961` n `8`; equity avg `0.3532` n `151`; fx avg `0.0051` n `6`; index avg `0.0773` n `26`; metal avg `0.0155` n `20`; unknown avg `10.4174` n `1177`
- 1h: commodity avg `0.1902` n `13`; crypto_alt avg `-0.8206` n `236`; crypto_major avg `-0.3848` n `8`; equity avg `-0.5107` n `151`; fx avg `0.0076` n `6`; index avg `-0.1121` n `26`; metal avg `-0.0377` n `20`; unknown avg `0.2021` n `1172`
- 4h: commodity avg `0.6699` n `13`; crypto_alt avg `-1.8265` n `236`; crypto_major avg `-1.1587` n `8`; equity avg `-1.7244` n `151`; fx avg `-0.0098` n `6`; index avg `-0.3301` n `26`; metal avg `-0.2171` n `20`; unknown avg `1.0149` n `996`
- 24h: commodity avg `0.2479` n `13`; crypto_alt avg `-1.5266` n `236`; crypto_major avg `-1.5742` n `8`; equity avg `-2.2326` n `151`; fx avg `-0.0063` n `6`; index avg `-0.4455` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.2487` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1392`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0846`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0757`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
