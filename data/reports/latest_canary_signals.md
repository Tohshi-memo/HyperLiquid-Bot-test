# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T16:22:27.300305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `0.0184` n `230`; crypto_major avg `-0.1393` n `8`; equity avg `-0.0074` n `112`; fx avg `-0.0001` n `6`; index avg `0.0021` n `25`; metal avg `0.0034` n `20`; unknown avg `0.0929` n `785`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `0.3331` n `230`; crypto_major avg `0.1189` n `8`; equity avg `-0.0082` n `112`; fx avg `0.0025` n `6`; index avg `0.0017` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0131` n `785`
- 4h: commodity avg `-0.0763` n `12`; crypto_alt avg `0.8571` n `230`; crypto_major avg `0.6068` n `8`; equity avg `0.1049` n `112`; fx avg `0.0071` n `6`; index avg `0.0294` n `25`; metal avg `0.0571` n `20`; unknown avg `0.1205` n `785`
- 24h: commodity avg `0.1539` n `12`; crypto_alt avg `1.1192` n `230`; crypto_major avg `0.0856` n `8`; equity avg `0.3089` n `112`; fx avg `0.013` n `6`; index avg `0.03` n `25`; metal avg `0.0876` n `20`; unknown avg `0.4282` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
