# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T03:52:27.191926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.0473` n `229`; crypto_major avg `-0.0422` n `8`; equity avg `-0.0237` n `88`; fx avg `0.0108` n `6`; index avg `-0.0052` n `25`; metal avg `-0.025` n `20`; unknown avg `0.1893` n `765`
- 1h: commodity avg `0.0329` n `12`; crypto_alt avg `0.0085` n `229`; crypto_major avg `0.0511` n `8`; equity avg `0.0229` n `88`; fx avg `0.0516` n `6`; index avg `0.0029` n `25`; metal avg `-0.0789` n `20`; unknown avg `-0.2684` n `765`
- 4h: commodity avg `0.1683` n `12`; crypto_alt avg `0.489` n `229`; crypto_major avg `0.1189` n `8`; equity avg `0.9988` n `88`; fx avg `0.0888` n `6`; index avg `0.1438` n `25`; metal avg `0.5712` n `20`; unknown avg `0.2068` n `761`
- 24h: commodity avg `0.3732` n `12`; crypto_alt avg `1.4946` n `228`; crypto_major avg `2.0446` n `8`; equity avg `-1.1083` n `88`; fx avg `-0.0278` n `6`; index avg `-0.198` n `25`; metal avg `1.0644` n `20`; unknown avg `6.2369` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
