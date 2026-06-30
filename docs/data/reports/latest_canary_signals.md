# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T09:37:34.839975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.0126` n `228`; crypto_major avg `0.0465` n `8`; equity avg `-0.0649` n `88`; fx avg `0.0018` n `6`; index avg `-0.0311` n `23`; metal avg `-0.0599` n `20`; unknown avg `-0.016` n `765`
- 1h: commodity avg `0.0039` n `12`; crypto_alt avg `0.0814` n `228`; crypto_major avg `0.1256` n `8`; equity avg `-0.0902` n `88`; fx avg `-0.0148` n `6`; index avg `-0.0283` n `23`; metal avg `-0.0362` n `20`; unknown avg `-0.0172` n `765`
- 4h: commodity avg `0.2397` n `12`; crypto_alt avg `-0.3063` n `228`; crypto_major avg `-0.2128` n `8`; equity avg `-0.3174` n `88`; fx avg `0.0454` n `6`; index avg `-0.0996` n `23`; metal avg `0.4283` n `20`; unknown avg `-0.5237` n `739`
- 24h: commodity avg `0.014` n `12`; crypto_alt avg `-0.7226` n `228`; crypto_major avg `0.5112` n `8`; equity avg `1.2925` n `88`; fx avg `0.1457` n `6`; index avg `0.0967` n `23`; metal avg `-0.0224` n `20`; unknown avg `8.9252` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
