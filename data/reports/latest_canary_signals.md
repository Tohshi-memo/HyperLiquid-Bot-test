# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T20:57:15.715929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0533` n `12`; crypto_alt avg `0.0007` n `230`; crypto_major avg `0.0123` n `8`; equity avg `0.0312` n `112`; fx avg `-0.0019` n `6`; index avg `0.0004` n `25`; metal avg `-0.0092` n `20`; unknown avg `-0.0765` n `785`
- 1h: commodity avg `0.0497` n `12`; crypto_alt avg `0.0232` n `230`; crypto_major avg `-0.0263` n `8`; equity avg `0.0374` n `112`; fx avg `0.0111` n `6`; index avg `-0.0044` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.1108` n `785`
- 4h: commodity avg `0.1662` n `12`; crypto_alt avg `0.2752` n `230`; crypto_major avg `-0.1638` n `8`; equity avg `0.129` n `112`; fx avg `0.0047` n `6`; index avg `0.017` n `25`; metal avg `0.0199` n `20`; unknown avg `-0.3584` n `785`
- 24h: commodity avg `0.1475` n `12`; crypto_alt avg `1.4419` n `230`; crypto_major avg `0.1246` n `8`; equity avg `0.2492` n `112`; fx avg `0.0068` n `6`; index avg `0.0275` n `25`; metal avg `0.0985` n `20`; unknown avg `-0.3159` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
