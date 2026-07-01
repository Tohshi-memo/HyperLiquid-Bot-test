# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T04:22:30.477325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.5` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.6529` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6315` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `0.1345` n `228`; crypto_major avg `0.0538` n `8`; equity avg `-0.0287` n `88`; fx avg `0.0091` n `6`; index avg `-0.0115` n `23`; metal avg `-0.0209` n `20`; unknown avg `0.9803` n `765`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `0.989` n `228`; crypto_major avg `0.651` n `8`; equity avg `0.0924` n `88`; fx avg `-0.0116` n `6`; index avg `0.037` n `23`; metal avg `-0.0899` n `20`; unknown avg `1.0171` n `763`
- 4h: commodity avg `-0.0326` n `12`; crypto_alt avg `1.4873` n `228`; crypto_major avg `1.3398` n `8`; equity avg `-0.2917` n `88`; fx avg `0.046` n `6`; index avg `-0.1463` n `23`; metal avg `-0.3131` n `20`; unknown avg `1.9934` n `763`
- 24h: commodity avg `0.0882` n `12`; crypto_alt avg `0.0764` n `228`; crypto_major avg `0.2595` n `8`; equity avg `0.4542` n `88`; fx avg `0.174` n `6`; index avg `-0.043` n `23`; metal avg `-0.1799` n `20`; unknown avg `-0.6338` n `733`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
