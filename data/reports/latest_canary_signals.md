# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T07:07:27.933496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0591` n `13`; crypto_alt avg `0.0446` n `237`; crypto_major avg `-0.0098` n `8`; equity avg `-0.0579` n `151`; fx avg `-0.021` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.0818` n `1196`
- 1h: commodity avg `-0.0741` n `13`; crypto_alt avg `0.395` n `237`; crypto_major avg `0.1729` n `8`; equity avg `0.4152` n `151`; fx avg `-0.0089` n `6`; index avg `0.1008` n `26`; metal avg `0.1262` n `20`; unknown avg `0.1837` n `1196`
- 4h: commodity avg `0.0198` n `13`; crypto_alt avg `-0.187` n `237`; crypto_major avg `-0.255` n `8`; equity avg `-0.705` n `151`; fx avg `-0.0287` n `6`; index avg `-0.0921` n `26`; metal avg `-0.0228` n `20`; unknown avg `1.2938` n `1168`
- 24h: commodity avg `0.3945` n `13`; crypto_alt avg `-0.0644` n `237`; crypto_major avg `-0.9309` n `8`; equity avg `-1.4464` n `151`; fx avg `0.0026` n `6`; index avg `-0.202` n `26`; metal avg `-0.2333` n `20`; unknown avg `5.0058` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
