# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T15:37:31.541777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.1108` n `230`; crypto_major avg `-0.0283` n `8`; equity avg `-0.0566` n `112`; fx avg `0.0018` n `6`; index avg `0.0166` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0042` n `784`
- 1h: commodity avg `-0.053` n `12`; crypto_alt avg `0.1656` n `230`; crypto_major avg `-0.0888` n `8`; equity avg `0.0143` n `112`; fx avg `0.004` n `6`; index avg `0.0239` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.2702` n `784`
- 4h: commodity avg `-0.0245` n `12`; crypto_alt avg `0.7325` n `230`; crypto_major avg `0.6238` n `8`; equity avg `0.1802` n `112`; fx avg `0.0015` n `6`; index avg `0.0417` n `25`; metal avg `-0.0228` n `20`; unknown avg `-0.2118` n `784`
- 24h: commodity avg `-0.2174` n `12`; crypto_alt avg `1.0` n `230`; crypto_major avg `0.8674` n `8`; equity avg `0.466` n `112`; fx avg `0.0016` n `6`; index avg `0.0393` n `25`; metal avg `0.0681` n `20`; unknown avg `-0.0984` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
