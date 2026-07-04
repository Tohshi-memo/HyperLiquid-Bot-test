# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T09:07:28.105204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.1296` n `229`; crypto_major avg `-0.2168` n `8`; equity avg `-0.0148` n `88`; fx avg `0.0058` n `6`; index avg `-0.0035` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.0397` n `765`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.0788` n `229`; crypto_major avg `-0.1081` n `8`; equity avg `0.0062` n `88`; fx avg `0.0041` n `6`; index avg `0.0183` n `25`; metal avg `0.0056` n `20`; unknown avg `0.3444` n `765`
- 4h: commodity avg `0.0076` n `12`; crypto_alt avg `-0.4849` n `229`; crypto_major avg `-0.3455` n `8`; equity avg `0.0158` n `88`; fx avg `-0.0148` n `6`; index avg `-0.0077` n `25`; metal avg `0.0135` n `20`; unknown avg `0.7396` n `745`
- 24h: commodity avg `-0.0397` n `12`; crypto_alt avg `1.2078` n `229`; crypto_major avg `1.9921` n `8`; equity avg `0.3749` n `88`; fx avg `-0.0461` n `6`; index avg `0.0158` n `25`; metal avg `-0.1532` n `20`; unknown avg `5.8001` n `733`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
