# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T03:52:25.208419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `-0.1238` n `8`; equity avg `0.0251` n `112`; fx avg `0.0081` n `6`; index avg `-0.0101` n `25`; metal avg `-0.026` n `20`; unknown avg `0.0759` n `785`
- 1h: commodity avg `0.0171` n `12`; crypto_alt avg `-0.0734` n `230`; crypto_major avg `-0.2071` n `8`; equity avg `-0.0234` n `112`; fx avg `-0.0207` n `6`; index avg `-0.0162` n `25`; metal avg `0.0361` n `20`; unknown avg `0.0013` n `785`
- 4h: commodity avg `0.0156` n `12`; crypto_alt avg `0.47` n `230`; crypto_major avg `0.3182` n `8`; equity avg `-0.2002` n `112`; fx avg `0.1048` n `6`; index avg `0.0198` n `25`; metal avg `-0.0774` n `20`; unknown avg `-0.002` n `785`
- 24h: commodity avg `0.4164` n `12`; crypto_alt avg `0.7241` n `230`; crypto_major avg `-0.0093` n `8`; equity avg `-0.1743` n `112`; fx avg `0.0932` n `6`; index avg `0.0186` n `25`; metal avg `-0.1608` n `20`; unknown avg `-0.2842` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
