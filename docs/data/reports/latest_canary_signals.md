# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T17:22:26.881376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0013` n `230`; crypto_major avg `-0.0353` n `8`; equity avg `0.0293` n `112`; fx avg `-0.0023` n `6`; index avg `0.0029` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0202` n `785`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `0.1817` n `230`; crypto_major avg `0.0352` n `8`; equity avg `0.0688` n `112`; fx avg `0.0006` n `6`; index avg `0.0054` n `25`; metal avg `-0.0068` n `20`; unknown avg `-0.1226` n `785`
- 4h: commodity avg `-0.0474` n `12`; crypto_alt avg `0.7294` n `230`; crypto_major avg `0.3769` n `8`; equity avg `0.087` n `112`; fx avg `0.0206` n `6`; index avg `0.0233` n `25`; metal avg `0.0223` n `20`; unknown avg `0.0257` n `785`
- 24h: commodity avg `0.0232` n `12`; crypto_alt avg `1.1911` n `230`; crypto_major avg `0.0973` n `8`; equity avg `0.3042` n `112`; fx avg `0.003` n `6`; index avg `0.035` n `25`; metal avg `0.0714` n `20`; unknown avg `0.3889` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
