# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T03:52:29.658065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `1.7657` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `1.6919` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.6372` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `0.8089` n `228`; crypto_major avg `1.0377` n `8`; equity avg `0.397` n `86`; fx avg `-0.004` n `6`; index avg `0.0234` n `23`; metal avg `0.0582` n `20`; unknown avg `1.5969` n `749`
- 1h: commodity avg `-0.07` n `12`; crypto_alt avg `1.5042` n `228`; crypto_major avg `1.8173` n `8`; equity avg `0.0516` n `86`; fx avg `0.0006` n `6`; index avg `-0.0632` n `23`; metal avg `0.1801` n `20`; unknown avg `4.0111` n `749`
- 4h: commodity avg `-0.1691` n `12`; crypto_alt avg `-0.5165` n `228`; crypto_major avg `-0.467` n `8`; equity avg `-2.1589` n `86`; fx avg `0.0296` n `6`; index avg `-0.5093` n `23`; metal avg `-0.459` n `20`; unknown avg `0.5102` n `733`
- 24h: commodity avg `0.3108` n `12`; crypto_alt avg `-1.617` n `228`; crypto_major avg `-1.3748` n `8`; equity avg `-4.0533` n `86`; fx avg `0.0386` n `6`; index avg `-0.6769` n `23`; metal avg `-0.1628` n `20`; unknown avg `0.618` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
