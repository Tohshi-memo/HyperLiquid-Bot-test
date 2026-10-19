# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T15:07:38.155617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `13`; crypto_alt avg `-0.0245` n `237`; crypto_major avg `-0.083` n `8`; equity avg `0.1169` n `151`; fx avg `0.008` n `6`; index avg `0.045` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.0891` n `1193`
- 1h: commodity avg `-0.036` n `13`; crypto_alt avg `0.5379` n `237`; crypto_major avg `0.4768` n `8`; equity avg `0.7323` n `151`; fx avg `-0.0016` n `6`; index avg `0.0968` n `26`; metal avg `0.0185` n `20`; unknown avg `0.4014` n `1139`
- 4h: commodity avg `-0.3008` n `13`; crypto_alt avg `0.354` n `237`; crypto_major avg `0.0076` n `8`; equity avg `0.2308` n `151`; fx avg `0.0185` n `6`; index avg `0.0627` n `26`; metal avg `-0.2269` n `20`; unknown avg `0.8236` n `1103`
- 24h: commodity avg `-0.4002` n `13`; crypto_alt avg `0.8932` n `237`; crypto_major avg `1.429` n `8`; equity avg `3.1852` n `151`; fx avg `-0.0192` n `6`; index avg `0.5985` n `26`; metal avg `0.0804` n `20`; unknown avg `3.8921` n `915`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
