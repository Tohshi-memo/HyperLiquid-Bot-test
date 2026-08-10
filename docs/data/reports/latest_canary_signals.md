# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T03:02:19.432238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.0017` n `230`; crypto_major avg `-0.026` n `8`; equity avg `-0.0462` n `112`; fx avg `-0.0103` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0315` n `20`; unknown avg `-0.0777` n `785`
- 1h: commodity avg `-0.0352` n `12`; crypto_alt avg `0.0029` n `230`; crypto_major avg `0.0317` n `8`; equity avg `-0.0376` n `112`; fx avg `-0.0189` n `6`; index avg `0.0007` n `25`; metal avg `-0.0411` n `20`; unknown avg `-0.155` n `785`
- 4h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.0268` n `230`; crypto_major avg `0.0096` n `8`; equity avg `-0.3154` n `112`; fx avg `0.0974` n `6`; index avg `0.0204` n `25`; metal avg `-0.1758` n `20`; unknown avg `-0.1407` n `785`
- 24h: commodity avg `0.3887` n `12`; crypto_alt avg `0.8444` n `230`; crypto_major avg `0.1951` n `8`; equity avg `-0.2826` n `112`; fx avg `0.0978` n `6`; index avg `0.0275` n `25`; metal avg `-0.2217` n `20`; unknown avg `-0.2795` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
