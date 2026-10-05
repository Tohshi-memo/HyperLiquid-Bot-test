# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T02:22:27.364437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0189` n `13`; crypto_alt avg `0.1358` n `235`; crypto_major avg `0.17` n `8`; equity avg `-0.0069` n `144`; fx avg `-0.0187` n `6`; index avg `-0.0006` n `26`; metal avg `-0.021` n `20`; unknown avg `-0.0466` n `1078`
- 1h: commodity avg `-0.048` n `13`; crypto_alt avg `0.1188` n `235`; crypto_major avg `0.1391` n `8`; equity avg `-0.1021` n `144`; fx avg `0.0333` n `6`; index avg `-0.0069` n `26`; metal avg `0.0105` n `20`; unknown avg `-0.1536` n `1072`
- 4h: commodity avg `-0.1903` n `13`; crypto_alt avg `0.532` n `235`; crypto_major avg `0.0742` n `8`; equity avg `0.2801` n `144`; fx avg `-0.0736` n `6`; index avg `0.0381` n `26`; metal avg `0.1231` n `20`; unknown avg `3.144` n `1038`
- 24h: commodity avg `-0.3602` n `13`; crypto_alt avg `1.732` n `235`; crypto_major avg `1.9457` n `8`; equity avg `0.583` n `144`; fx avg `-0.0513` n `6`; index avg `0.0379` n `26`; metal avg `0.1964` n `20`; unknown avg `0.6787` n `950`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1957`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
