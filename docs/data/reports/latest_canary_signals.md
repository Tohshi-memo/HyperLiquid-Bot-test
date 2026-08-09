# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T18:22:27.746154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `12`; crypto_alt avg `-0.062` n `230`; crypto_major avg `-0.0569` n `8`; equity avg `0.0081` n `112`; fx avg `0.0043` n `6`; index avg `0.0058` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.064` n `785`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.0338` n `230`; crypto_major avg `-0.1225` n `8`; equity avg `0.0318` n `112`; fx avg `0.0038` n `6`; index avg `0.0152` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0422` n `785`
- 4h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.6889` n `230`; crypto_major avg `0.1221` n `8`; equity avg `0.1013` n `112`; fx avg `0.0162` n `6`; index avg `0.0298` n `25`; metal avg `0.0313` n `20`; unknown avg `-0.116` n `785`
- 24h: commodity avg `0.0905` n `12`; crypto_alt avg `1.2669` n `230`; crypto_major avg `0.1159` n `8`; equity avg `0.2931` n `112`; fx avg `0.0075` n `6`; index avg `0.0412` n `25`; metal avg `0.0696` n `20`; unknown avg `0.3774` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
