# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T11:07:32.881676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.1334` n `228`; crypto_major avg `-0.056` n `8`; equity avg `-0.0059` n `88`; fx avg `-0.0097` n `6`; index avg `-0.0049` n `23`; metal avg `0.0156` n `20`; unknown avg `-0.013` n `764`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0971` n `228`; crypto_major avg `-0.0114` n `8`; equity avg `0.0558` n `88`; fx avg `0.0213` n `6`; index avg `-0.0051` n `23`; metal avg `0.007` n `20`; unknown avg `-0.029` n `764`
- 4h: commodity avg `0.0908` n `12`; crypto_alt avg `-0.2248` n `228`; crypto_major avg `-0.2107` n `8`; equity avg `0.0674` n `88`; fx avg `0.0069` n `6`; index avg `-0.0166` n `23`; metal avg `-0.0307` n `20`; unknown avg `-0.2459` n `748`
- 24h: commodity avg `0.0896` n `12`; crypto_alt avg `1.7341` n `228`; crypto_major avg `1.6728` n `8`; equity avg `1.8014` n `87`; fx avg `0.0323` n `6`; index avg `0.0632` n `23`; metal avg `0.2988` n `20`; unknown avg `0.0061` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
