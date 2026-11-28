# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T05:37:28.892873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.3751` n `239`; crypto_major avg `-0.0675` n `8`; equity avg `-0.0377` n `168`; fx avg `-0.0103` n `6`; index avg `-0.0057` n `27`; metal avg `-0.0088` n `20`; unknown avg `99.3358` n `1265`
- 1h: commodity avg `0.0081` n `13`; crypto_alt avg `-0.9475` n `239`; crypto_major avg `-0.5046` n `8`; equity avg `-0.2985` n `168`; fx avg `-0.0099` n `6`; index avg `-0.0266` n `27`; metal avg `-0.0315` n `20`; unknown avg `21.0822` n `1259`
- 4h: commodity avg `0.0312` n `13`; crypto_alt avg `-1.9369` n `239`; crypto_major avg `-0.9131` n `8`; equity avg `-0.1117` n `168`; fx avg `-0.001` n `6`; index avg `-0.0224` n `27`; metal avg `-0.0074` n `20`; unknown avg `0.9895` n `1235`
- 24h: commodity avg `-0.8404` n `13`; crypto_alt avg `-2.9292` n `239`; crypto_major avg `-2.587` n `8`; equity avg `-0.3694` n `168`; fx avg `-0.1451` n `6`; index avg `-0.0115` n `27`; metal avg `-0.1288` n `20`; unknown avg `215.4034` n `975`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
