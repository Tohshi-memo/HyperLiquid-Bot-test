# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T21:52:28.452600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.85` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.0656` n `228`; crypto_major avg `0.1648` n `8`; equity avg `0.0357` n `88`; fx avg `0.0076` n `6`; index avg `-0.0376` n `23`; metal avg `0.0185` n `20`; unknown avg `-0.1165` n `765`
- 1h: commodity avg `0.0214` n `12`; crypto_alt avg `0.189` n `228`; crypto_major avg `0.3273` n `8`; equity avg `0.0709` n `88`; fx avg `0.0241` n `6`; index avg `-0.0193` n `23`; metal avg `0.0386` n `20`; unknown avg `0.2157` n `765`
- 4h: commodity avg `-0.109` n `12`; crypto_alt avg `-0.4255` n `228`; crypto_major avg `0.1129` n `8`; equity avg `0.4657` n `88`; fx avg `0.0239` n `6`; index avg `0.0463` n `23`; metal avg `0.0623` n `20`; unknown avg `0.3806` n `765`
- 24h: commodity avg `-0.389` n `12`; crypto_alt avg `2.4158` n `228`; crypto_major avg `3.755` n `8`; equity avg `1.7818` n `88`; fx avg `0.2282` n `6`; index avg `0.1254` n `23`; metal avg `-0.4277` n `20`; unknown avg `1.8599` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
