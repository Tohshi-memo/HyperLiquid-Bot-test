# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T09:22:26.159532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `0.0267` n `233`; crypto_major avg `-0.0466` n `8`; equity avg `-0.052` n `134`; fx avg `0.0044` n `6`; index avg `-0.0171` n `26`; metal avg `-0.0213` n `20`; unknown avg `0.7658` n `797`
- 1h: commodity avg `0.083` n `12`; crypto_alt avg `0.0561` n `233`; crypto_major avg `-0.0225` n `8`; equity avg `-0.1244` n `134`; fx avg `0.0042` n `6`; index avg `-0.0406` n `26`; metal avg `-0.1118` n `20`; unknown avg `0.1809` n `789`
- 4h: commodity avg `0.1382` n `12`; crypto_alt avg `-0.5058` n `233`; crypto_major avg `-0.3868` n `8`; equity avg `-0.3396` n `134`; fx avg `0.0656` n `6`; index avg `-0.0582` n `26`; metal avg `-0.2495` n `20`; unknown avg `-0.365` n `765`
- 24h: commodity avg `-0.0107` n `12`; crypto_alt avg `-4.4927` n `233`; crypto_major avg `-3.0693` n `8`; equity avg `-1.4451` n `134`; fx avg `0.0928` n `6`; index avg `-0.1581` n `26`; metal avg `0.0654` n `20`; unknown avg `-0.8046` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
