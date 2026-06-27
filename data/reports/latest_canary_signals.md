# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T10:31:29.382461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.0274` n `228`; crypto_major avg `-0.0851` n `8`; equity avg `0.0151` n `88`; fx avg `-0.0187` n `6`; index avg `-0.0009` n `23`; metal avg `-0.0018` n `20`; unknown avg `-0.011` n `764`
- 1h: commodity avg `0.0481` n `12`; crypto_alt avg `0.1136` n `228`; crypto_major avg `0.0833` n `8`; equity avg `-0.009` n `88`; fx avg `-0.019` n `6`; index avg `-0.0017` n `23`; metal avg `-0.0014` n `20`; unknown avg `-0.0343` n `764`
- 4h: commodity avg `0.1219` n `12`; crypto_alt avg `-0.2175` n `228`; crypto_major avg `-0.1927` n `8`; equity avg `0.1071` n `88`; fx avg `-0.0091` n `6`; index avg `0.0005` n `23`; metal avg `-0.0324` n `20`; unknown avg `-0.2451` n `748`
- 24h: commodity avg `0.1651` n `12`; crypto_alt avg `1.5655` n `228`; crypto_major avg `1.6422` n `8`; equity avg `1.9376` n `87`; fx avg `0.0103` n `6`; index avg `0.09` n `23`; metal avg `0.3676` n `20`; unknown avg `-0.0183` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
