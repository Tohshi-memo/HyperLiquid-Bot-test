# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T09:07:26.627308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `0.1308` n `228`; crypto_major avg `0.1139` n `8`; equity avg `0.1664` n `88`; fx avg `-0.0178` n `6`; index avg `0.0045` n `23`; metal avg `0.0699` n `20`; unknown avg `-0.1011` n `765`
- 1h: commodity avg `0.0888` n `12`; crypto_alt avg `-0.3502` n `228`; crypto_major avg `-0.3171` n `8`; equity avg `-0.1924` n `88`; fx avg `-0.0361` n `6`; index avg `-0.043` n `23`; metal avg `-0.1317` n `20`; unknown avg `-0.1473` n `765`
- 4h: commodity avg `0.2277` n `12`; crypto_alt avg `-0.5157` n `228`; crypto_major avg `-0.3694` n `8`; equity avg `-0.4985` n `88`; fx avg `0.0595` n `6`; index avg `-0.1554` n `23`; metal avg `0.384` n `20`; unknown avg `-0.7087` n `737`
- 24h: commodity avg `0.0326` n `12`; crypto_alt avg `-0.5643` n `228`; crypto_major avg `0.6001` n `8`; equity avg `1.4695` n `88`; fx avg `0.1501` n `6`; index avg `0.1209` n `23`; metal avg `-0.0669` n `20`; unknown avg `8.9668` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
