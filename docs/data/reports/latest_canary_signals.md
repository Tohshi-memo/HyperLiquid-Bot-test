# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T17:52:26.988824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.27` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2689` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0648` n `12`; crypto_alt avg `-0.2105` n `233`; crypto_major avg `-0.1079` n `8`; equity avg `0.0192` n `136`; fx avg `0.003` n `6`; index avg `-0.0013` n `26`; metal avg `-0.017` n `20`; unknown avg `0.1428` n `806`
- 1h: commodity avg `-0.0386` n `12`; crypto_alt avg `-0.6059` n `233`; crypto_major avg `-0.3857` n `8`; equity avg `0.2284` n `136`; fx avg `-0.0038` n `6`; index avg `0.0353` n `26`; metal avg `0.02` n `20`; unknown avg `-0.0334` n `758`
- 4h: commodity avg `0.0449` n `12`; crypto_alt avg `-0.6292` n `233`; crypto_major avg `-1.1933` n `8`; equity avg `0.2366` n `136`; fx avg `0.0319` n `6`; index avg `0.0756` n `26`; metal avg `-0.1976` n `20`; unknown avg `0.6632` n `736`
- 24h: commodity avg `-0.4423` n `12`; crypto_alt avg `0.5775` n `233`; crypto_major avg `1.4059` n `8`; equity avg `0.6028` n `136`; fx avg `-0.1506` n `6`; index avg `0.3476` n `26`; metal avg `0.1435` n `20`; unknown avg `1.8376` n `666`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
