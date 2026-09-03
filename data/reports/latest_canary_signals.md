# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T11:22:25.245673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0371` n `12`; crypto_alt avg `0.1308` n `232`; crypto_major avg `0.1991` n `8`; equity avg `0.0484` n `133`; fx avg `-0.035` n `6`; index avg `0.0063` n `26`; metal avg `0.0382` n `20`; unknown avg `0.1216` n `792`
- 1h: commodity avg `-0.0652` n `12`; crypto_alt avg `-0.006` n `232`; crypto_major avg `0.1371` n `8`; equity avg `0.2127` n `133`; fx avg `-0.0449` n `6`; index avg `0.0355` n `26`; metal avg `0.0561` n `20`; unknown avg `0.0427` n `790`
- 4h: commodity avg `0.3548` n `12`; crypto_alt avg `-0.0184` n `232`; crypto_major avg `-0.1016` n `8`; equity avg `-0.0978` n `133`; fx avg `-0.0625` n `6`; index avg `-0.018` n `26`; metal avg `0.0035` n `20`; unknown avg `1.4315` n `790`
- 24h: commodity avg `0.6391` n `12`; crypto_alt avg `2.3037` n `232`; crypto_major avg `2.249` n `8`; equity avg `1.6596` n `133`; fx avg `-0.4043` n `6`; index avg `0.1178` n `26`; metal avg `0.6628` n `20`; unknown avg `-0.1077` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
