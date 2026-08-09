# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T20:07:31.169793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `0.0423` n `230`; crypto_major avg `-0.0324` n `8`; equity avg `0.0125` n `112`; fx avg `0.0061` n `6`; index avg `-0.0027` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0048` n `785`
- 1h: commodity avg `-0.0197` n `12`; crypto_alt avg `0.1709` n `230`; crypto_major avg `-0.0097` n `8`; equity avg `0.0367` n `112`; fx avg `-0.0044` n `6`; index avg `-0.0076` n `25`; metal avg `0.0233` n `20`; unknown avg `-0.0947` n `785`
- 4h: commodity avg `0.0788` n `12`; crypto_alt avg `0.4245` n `230`; crypto_major avg `-0.2432` n `8`; equity avg `0.1282` n `112`; fx avg `0.0018` n `6`; index avg `0.0244` n `25`; metal avg `0.0331` n `20`; unknown avg `-0.3239` n `785`
- 24h: commodity avg `0.1017` n `12`; crypto_alt avg `1.4542` n `230`; crypto_major avg `0.1084` n `8`; equity avg `0.2267` n `112`; fx avg `0.0046` n `6`; index avg `0.0335` n `25`; metal avg `0.1092` n `20`; unknown avg `-0.2839` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
