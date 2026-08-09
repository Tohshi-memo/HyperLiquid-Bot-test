# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T19:45:03.507837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `0.0503` n `230`; crypto_major avg `0.0096` n `8`; equity avg `0.0272` n `112`; fx avg `-0.0014` n `6`; index avg `-0.0039` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.0222` n `785`
- 1h: commodity avg `-0.0129` n `12`; crypto_alt avg `0.1508` n `230`; crypto_major avg `0.0573` n `8`; equity avg `0.0407` n `112`; fx avg `-0.0058` n `6`; index avg `-0.0044` n `25`; metal avg `0.0181` n `20`; unknown avg `-0.1386` n `785`
- 4h: commodity avg `0.0482` n `12`; crypto_alt avg `0.4167` n `230`; crypto_major avg `-0.1149` n `8`; equity avg `0.1324` n `112`; fx avg `-0.0035` n `6`; index avg `0.0324` n `25`; metal avg `0.0162` n `20`; unknown avg `-0.337` n `785`
- 24h: commodity avg `0.0819` n `12`; crypto_alt avg `1.3416` n `230`; crypto_major avg `0.1726` n `8`; equity avg `0.1932` n `112`; fx avg `-0.006` n `6`; index avg `0.0414` n `25`; metal avg `0.0833` n `20`; unknown avg `-0.2201` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
