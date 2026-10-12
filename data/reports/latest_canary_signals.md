# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T05:37:32.914258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `13`; crypto_alt avg `-0.4097` n `235`; crypto_major avg `-0.3292` n `8`; equity avg `-0.0664` n `151`; fx avg `0.0082` n `6`; index avg `-0.0138` n `26`; metal avg `0.0197` n `20`; unknown avg `1.428` n `1133`
- 1h: commodity avg `0.0664` n `13`; crypto_alt avg `-0.1352` n `235`; crypto_major avg `-0.0603` n `8`; equity avg `-0.1663` n `151`; fx avg `0.0192` n `6`; index avg `-0.0474` n `26`; metal avg `-0.0743` n `20`; unknown avg `1.5277` n `1103`
- 4h: commodity avg `0.0413` n `13`; crypto_alt avg `0.9271` n `235`; crypto_major avg `0.5387` n `8`; equity avg `-0.6619` n `151`; fx avg `-0.0143` n `6`; index avg `-0.0357` n `26`; metal avg `-0.0776` n `20`; unknown avg `0.7072` n `1051`
- 24h: commodity avg `-0.3532` n `13`; crypto_alt avg `2.976` n `235`; crypto_major avg `1.6319` n `8`; equity avg `-0.3283` n `151`; fx avg `-0.0427` n `6`; index avg `-0.0187` n `26`; metal avg `0.0704` n `20`; unknown avg `0.7658` n `874`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
