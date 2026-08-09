# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T04:07:23.880848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `0.0719` n `230`; crypto_major avg `-0.0108` n `8`; equity avg `0.0028` n `112`; fx avg `0.007` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0093` n `784`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.1279` n `230`; crypto_major avg `0.0122` n `8`; equity avg `-0.0829` n `112`; fx avg `0.0012` n `6`; index avg `-0.0032` n `25`; metal avg `0.0041` n `20`; unknown avg `0.4469` n `784`
- 4h: commodity avg `0.0752` n `12`; crypto_alt avg `0.1034` n `230`; crypto_major avg `-0.2565` n `8`; equity avg `-0.0246` n `112`; fx avg `0.0124` n `6`; index avg `-0.0105` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0974` n `784`
- 24h: commodity avg `0.2146` n `12`; crypto_alt avg `1.5034` n `230`; crypto_major avg `0.4056` n `8`; equity avg `0.4734` n `112`; fx avg `0.0051` n `6`; index avg `0.0208` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.0148` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
