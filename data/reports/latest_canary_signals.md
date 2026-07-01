# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T05:07:28.780855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1844` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8288` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `-0.0409` n `228`; crypto_major avg `-0.0403` n `8`; equity avg `-0.0777` n `88`; fx avg `0.0208` n `6`; index avg `-0.0086` n `23`; metal avg `-0.103` n `20`; unknown avg `0.1376` n `765`
- 1h: commodity avg `-0.0217` n `12`; crypto_alt avg `0.304` n `228`; crypto_major avg `0.2338` n `8`; equity avg `0.045` n `88`; fx avg `-0.0295` n `6`; index avg `0.0235` n `23`; metal avg `-0.0558` n `20`; unknown avg `0.7799` n `765`
- 4h: commodity avg `-0.0227` n `12`; crypto_alt avg `1.9102` n `228`; crypto_major avg `1.8723` n `8`; equity avg `0.0435` n `88`; fx avg `-0.0507` n `6`; index avg `-0.0224` n `23`; metal avg `-0.3121` n `20`; unknown avg `7.7083` n `763`
- 24h: commodity avg `0.1643` n `12`; crypto_alt avg `0.1252` n `228`; crypto_major avg `0.3515` n `8`; equity avg `0.3523` n `88`; fx avg `0.1532` n `6`; index avg `-0.0696` n `23`; metal avg `-0.2972` n `20`; unknown avg `-0.7661` n `733`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
