# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T11:07:47.403920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2481` n `12`; crypto_alt avg `0.1019` n `230`; crypto_major avg `0.1572` n `8`; equity avg `0.2903` n `113`; fx avg `-0.0376` n `6`; index avg `0.0573` n `25`; metal avg `0.0549` n `20`; unknown avg `-0.0187` n `785`
- 1h: commodity avg `-0.4601` n `12`; crypto_alt avg `0.0477` n `230`; crypto_major avg `0.153` n `8`; equity avg `0.5724` n `113`; fx avg `-0.0645` n `6`; index avg `0.1125` n `25`; metal avg `0.0936` n `20`; unknown avg `0.0459` n `785`
- 4h: commodity avg `-0.3621` n `12`; crypto_alt avg `0.0921` n `230`; crypto_major avg `0.5956` n `8`; equity avg `0.5726` n `113`; fx avg `-0.0798` n `6`; index avg `0.1409` n `25`; metal avg `0.2857` n `20`; unknown avg `0.0638` n `785`
- 24h: commodity avg `0.4774` n `12`; crypto_alt avg `-0.9942` n `230`; crypto_major avg `-0.2759` n `8`; equity avg `-0.4777` n `113`; fx avg `-0.0459` n `6`; index avg `0.1357` n `25`; metal avg `0.5008` n `20`; unknown avg `0.1654` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
