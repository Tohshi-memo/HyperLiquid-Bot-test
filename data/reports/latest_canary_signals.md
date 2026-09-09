# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T02:52:30.175880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0201` n `12`; crypto_alt avg `0.1083` n `233`; crypto_major avg `0.053` n `8`; equity avg `0.0926` n `134`; fx avg `-0.0259` n `6`; index avg `0.008` n `26`; metal avg `0.1184` n `20`; unknown avg `-0.162` n `793`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `-0.0192` n `233`; crypto_major avg `0.0657` n `8`; equity avg `0.2591` n `134`; fx avg `0.0121` n `6`; index avg `0.0393` n `26`; metal avg `0.101` n `20`; unknown avg `-0.2536` n `791`
- 4h: commodity avg `0.014` n `12`; crypto_alt avg `-0.2126` n `233`; crypto_major avg `0.289` n `8`; equity avg `0.5839` n `134`; fx avg `-0.0103` n `6`; index avg `0.1183` n `26`; metal avg `0.2073` n `20`; unknown avg `0.3499` n `785`
- 24h: commodity avg `0.1514` n `12`; crypto_alt avg `-0.5051` n `232`; crypto_major avg `0.7018` n `8`; equity avg `0.6299` n `134`; fx avg `0.0677` n `6`; index avg `-0.1326` n `26`; metal avg `-0.2152` n `20`; unknown avg `0.2267` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
