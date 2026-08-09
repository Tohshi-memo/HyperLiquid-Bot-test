# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T19:22:23.644242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `0.0132` n `230`; crypto_major avg `-0.0133` n `8`; equity avg `-0.0067` n `112`; fx avg `-0.0046` n `6`; index avg `0.0004` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0138` n `785`
- 1h: commodity avg `0.0815` n `12`; crypto_alt avg `0.029` n `230`; crypto_major avg `-0.0202` n `8`; equity avg `-0.0075` n `112`; fx avg `-0.0026` n `6`; index avg `0.0097` n `25`; metal avg `0.011` n `20`; unknown avg `-0.2206` n `785`
- 4h: commodity avg `0.0724` n `12`; crypto_alt avg `0.5838` n `230`; crypto_major avg `0.011` n `8`; equity avg `0.0839` n `112`; fx avg `0.0043` n `6`; index avg `0.032` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.3511` n `785`
- 24h: commodity avg `0.1206` n `12`; crypto_alt avg `1.3508` n `230`; crypto_major avg `0.2187` n `8`; equity avg `0.233` n `112`; fx avg `0.006` n `6`; index avg `0.052` n `25`; metal avg `0.0848` n `20`; unknown avg `-0.2089` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
