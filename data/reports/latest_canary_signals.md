# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T11:52:28.224105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0683` n `12`; crypto_alt avg `0.0447` n `228`; crypto_major avg `0.1652` n `8`; equity avg `0.1114` n `88`; fx avg `0.0037` n `6`; index avg `0.0342` n `23`; metal avg `0.03` n `20`; unknown avg `-0.097` n `765`
- 1h: commodity avg `0.1231` n `12`; crypto_alt avg `-0.5368` n `228`; crypto_major avg `-0.089` n `8`; equity avg `0.1418` n `88`; fx avg `-0.0225` n `6`; index avg `0.0672` n `23`; metal avg `0.021` n `20`; unknown avg `-0.0675` n `765`
- 4h: commodity avg `0.255` n `12`; crypto_alt avg `-0.7989` n `228`; crypto_major avg `-0.3033` n `8`; equity avg `0.0814` n `88`; fx avg `-0.0463` n `6`; index avg `0.0553` n `23`; metal avg `0.1175` n `20`; unknown avg `-0.2001` n `765`
- 24h: commodity avg `0.303` n `12`; crypto_alt avg `-1.1096` n `228`; crypto_major avg `0.467` n `8`; equity avg `1.451` n `88`; fx avg `0.1135` n `6`; index avg `0.1853` n `23`; metal avg `0.297` n `20`; unknown avg `9.1931` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
