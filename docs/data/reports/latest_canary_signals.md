# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T00:38:03.887070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.1523` n `230`; crypto_major avg `-0.1895` n `8`; equity avg `-0.2052` n `112`; fx avg `0.0091` n `6`; index avg `-0.0179` n `25`; metal avg `-0.0418` n `20`; unknown avg `0.1013` n `785`
- 1h: commodity avg `-0.0196` n `12`; crypto_alt avg `0.2909` n `230`; crypto_major avg `0.0678` n `8`; equity avg `-0.0997` n `112`; fx avg `0.0699` n `6`; index avg `0.0123` n `25`; metal avg `-0.0522` n `20`; unknown avg `0.0689` n `785`
- 4h: commodity avg `0.3566` n `12`; crypto_alt avg `-0.8172` n `230`; crypto_major avg `-0.7784` n `8`; equity avg `-0.3136` n `112`; fx avg `0.0583` n `6`; index avg `-0.0341` n `25`; metal avg `-0.2336` n `20`; unknown avg `0.4376` n `785`
- 24h: commodity avg `0.478` n `12`; crypto_alt avg `0.6503` n `230`; crypto_major avg `-0.448` n `8`; equity avg `-0.1316` n `112`; fx avg `0.0617` n `6`; index avg `-0.0138` n `25`; metal avg `-0.143` n `20`; unknown avg `-0.3851` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
