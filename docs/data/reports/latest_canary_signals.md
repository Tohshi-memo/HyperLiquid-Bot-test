# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T12:37:28.239159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0453` n `12`; crypto_alt avg `0.3222` n `228`; crypto_major avg `0.4818` n `8`; equity avg `0.2507` n `86`; fx avg `0.0237` n `6`; index avg `0.0548` n `23`; metal avg `0.1705` n `20`; unknown avg `0.0692` n `765`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `0.0454` n `228`; crypto_major avg `0.2178` n `8`; equity avg `0.2473` n `86`; fx avg `0.0105` n `6`; index avg `0.0706` n `23`; metal avg `0.3142` n `20`; unknown avg `-0.059` n `765`
- 4h: commodity avg `0.0667` n `12`; crypto_alt avg `-0.8143` n `228`; crypto_major avg `-0.7454` n `8`; equity avg `0.1412` n `86`; fx avg `-0.0135` n `6`; index avg `0.0365` n `23`; metal avg `0.1725` n `20`; unknown avg `-0.1364` n `765`
- 24h: commodity avg `-0.1108` n `12`; crypto_alt avg `-1.8412` n `228`; crypto_major avg `-1.6056` n `8`; equity avg `0.4121` n `86`; fx avg `0.0156` n `6`; index avg `0.5234` n `23`; metal avg `-0.2147` n `20`; unknown avg `-0.6881` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
