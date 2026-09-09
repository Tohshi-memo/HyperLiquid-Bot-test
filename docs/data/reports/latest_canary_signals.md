# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T01:52:29.204883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `-0.0076` n `233`; crypto_major avg `0.0311` n `8`; equity avg `-0.1702` n `134`; fx avg `-0.0068` n `6`; index avg `-0.0325` n `26`; metal avg `-0.0594` n `20`; unknown avg `0.0356` n `797`
- 1h: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.1946` n `233`; crypto_major avg `-0.1329` n `8`; equity avg `0.1093` n `134`; fx avg `-0.0137` n `6`; index avg `0.0052` n `26`; metal avg `0.0053` n `20`; unknown avg `-0.0348` n `795`
- 4h: commodity avg `-0.0235` n `12`; crypto_alt avg `0.2081` n `233`; crypto_major avg `0.5788` n `8`; equity avg `0.3343` n `134`; fx avg `-0.0186` n `6`; index avg `0.073` n `26`; metal avg `0.0417` n `20`; unknown avg `0.8601` n `757`
- 24h: commodity avg `0.1717` n `12`; crypto_alt avg `-1.1648` n `232`; crypto_major avg `0.056` n `8`; equity avg `0.3364` n `134`; fx avg `0.0121` n `6`; index avg `-0.1795` n `26`; metal avg `-0.4742` n `20`; unknown avg `0.7288` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
