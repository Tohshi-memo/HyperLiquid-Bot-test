# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T23:52:28.908028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `0.0032` n `230`; crypto_major avg `-0.0784` n `8`; equity avg `-0.0075` n `112`; fx avg `-0.0024` n `6`; index avg `0.0131` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.0485` n `785`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `-0.6665` n `230`; crypto_major avg `-0.5049` n `8`; equity avg `-0.0148` n `112`; fx avg `-0.0089` n `6`; index avg `0.0162` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.011` n `785`
- 4h: commodity avg `0.3597` n `12`; crypto_alt avg `-1.0777` n `230`; crypto_major avg `-0.9614` n `8`; equity avg `-0.2153` n `112`; fx avg `-0.001` n `6`; index avg `-0.0382` n `25`; metal avg `-0.1624` n `20`; unknown avg `0.3522` n `785`
- 24h: commodity avg `0.4652` n `12`; crypto_alt avg `0.3417` n `230`; crypto_major avg `-0.5545` n `8`; equity avg `-0.0123` n `112`; fx avg `-0.008` n `6`; index avg `-0.0158` n `25`; metal avg `-0.0961` n `20`; unknown avg `-0.337` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
