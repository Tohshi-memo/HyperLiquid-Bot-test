# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T20:34:40.877337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `0.0109` n `228`; crypto_major avg `-0.1829` n `8`; equity avg `-0.1107` n `86`; fx avg `0.0026` n `6`; index avg `-0.0145` n `23`; metal avg `-0.0329` n `20`; unknown avg `-0.0664` n `765`
- 1h: commodity avg `-0.0744` n `12`; crypto_alt avg `0.7201` n `228`; crypto_major avg `0.5679` n `8`; equity avg `0.5018` n `86`; fx avg `-0.0064` n `6`; index avg `0.0943` n `23`; metal avg `-0.0551` n `20`; unknown avg `0.2089` n `765`
- 4h: commodity avg `0.0542` n `12`; crypto_alt avg `0.2527` n `228`; crypto_major avg `0.5482` n `8`; equity avg `0.2551` n `86`; fx avg `0.0116` n `6`; index avg `0.0432` n `23`; metal avg `-0.1216` n `20`; unknown avg `0.1723` n `765`
- 24h: commodity avg `0.4619` n `12`; crypto_alt avg `-1.2204` n `228`; crypto_major avg `-1.3851` n `8`; equity avg `-1.6001` n `86`; fx avg `0.0901` n `6`; index avg `-0.0014` n `23`; metal avg `0.3334` n `20`; unknown avg `0.2551` n `700`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
