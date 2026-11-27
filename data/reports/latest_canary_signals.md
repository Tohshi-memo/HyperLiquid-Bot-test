# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T04:22:27.256615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `0.0731` n `239`; crypto_major avg `0.2348` n `8`; equity avg `0.1256` n `168`; fx avg `-0.0044` n `6`; index avg `0.0215` n `27`; metal avg `0.0298` n `20`; unknown avg `0.0857` n `1261`
- 1h: commodity avg `0.0399` n `13`; crypto_alt avg `-0.0935` n `239`; crypto_major avg `-0.0019` n `8`; equity avg `0.2576` n `168`; fx avg `-0.0268` n `6`; index avg `0.0484` n `27`; metal avg `0.0122` n `20`; unknown avg `55.8477` n `1251`
- 4h: commodity avg `0.1901` n `13`; crypto_alt avg `1.2817` n `239`; crypto_major avg `2.164` n `8`; equity avg `2.8898` n `168`; fx avg `-0.0201` n `6`; index avg `0.309` n `27`; metal avg `0.9282` n `20`; unknown avg `15.667` n `1253`
- 24h: commodity avg `0.2228` n `13`; crypto_alt avg `1.5344` n `239`; crypto_major avg `1.7868` n `8`; equity avg `2.2518` n `168`; fx avg `0.0298` n `6`; index avg `0.2329` n `27`; metal avg `0.7115` n `20`; unknown avg `202.6966` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
