# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T20:15:26.288545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.1059` n `230`; crypto_major avg `-0.0967` n `8`; equity avg `-0.0208` n `112`; fx avg `0.0043` n `6`; index avg `-0.0016` n `25`; metal avg `-0.004` n `20`; unknown avg `0.0775` n `785`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `0.0508` n `230`; crypto_major avg `-0.0931` n `8`; equity avg `0.0226` n `112`; fx avg `0.0045` n `6`; index avg `-0.0096` n `25`; metal avg `0.0186` n `20`; unknown avg `-0.0024` n `785`
- 4h: commodity avg `0.0951` n `12`; crypto_alt avg `0.2959` n `230`; crypto_major avg `-0.2006` n `8`; equity avg `0.1148` n `112`; fx avg `0.0063` n `6`; index avg `0.0207` n `25`; metal avg `0.0257` n `20`; unknown avg `-0.3156` n `785`
- 24h: commodity avg `0.109` n `12`; crypto_alt avg `1.3244` n `230`; crypto_major avg `0.0192` n `8`; equity avg `0.2388` n `112`; fx avg `0.0108` n `6`; index avg `0.0319` n `25`; metal avg `0.1023` n `20`; unknown avg `-0.2728` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
