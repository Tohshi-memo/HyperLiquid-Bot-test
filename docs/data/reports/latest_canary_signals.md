# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T11:07:29.666496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0189` n `233`; crypto_major avg `0.0213` n `8`; equity avg `0.0202` n `136`; fx avg `-0.0036` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.0126` n `836`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.0311` n `233`; crypto_major avg `-0.0135` n `8`; equity avg `0.0008` n `136`; fx avg `-0.0041` n `6`; index avg `-0.0007` n `26`; metal avg `0.0006` n `20`; unknown avg `0.5454` n `836`
- 4h: commodity avg `0.0554` n `12`; crypto_alt avg `0.3708` n `233`; crypto_major avg `0.4807` n `8`; equity avg `0.0468` n `136`; fx avg `-0.0057` n `6`; index avg `-0.0008` n `26`; metal avg `0.0` n `20`; unknown avg `0.8673` n `830`
- 24h: commodity avg `-0.0173` n `12`; crypto_alt avg `3.2886` n `233`; crypto_major avg `2.301` n `8`; equity avg `0.2941` n `136`; fx avg `-0.0246` n `6`; index avg `0.1332` n `26`; metal avg `0.0192` n `20`; unknown avg `1.2305` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
