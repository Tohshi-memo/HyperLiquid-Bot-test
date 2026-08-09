# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T02:37:27.600239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0534` n `230`; crypto_major avg `-0.0479` n `8`; equity avg `-0.0065` n `112`; fx avg `0.0001` n `6`; index avg `-0.0009` n `25`; metal avg `0.0018` n `20`; unknown avg `1.0075` n `784`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `0.1373` n `230`; crypto_major avg `-0.0185` n `8`; equity avg `0.0357` n `112`; fx avg `0.0009` n `6`; index avg `0.0063` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.8782` n `784`
- 4h: commodity avg `0.0126` n `12`; crypto_alt avg `0.0212` n `230`; crypto_major avg `-0.2571` n `8`; equity avg `-0.0447` n `112`; fx avg `0.004` n `6`; index avg `0.0012` n `25`; metal avg `0.0112` n `20`; unknown avg `-0.1512` n `784`
- 24h: commodity avg `0.2189` n `12`; crypto_alt avg `1.6602` n `230`; crypto_major avg `0.8527` n `8`; equity avg `0.5004` n `112`; fx avg `-0.0014` n `6`; index avg `0.0279` n `25`; metal avg `0.0118` n `20`; unknown avg `0.14` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
