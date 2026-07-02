# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T10:07:28.581943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.0119` n `229`; crypto_major avg `0.0458` n `8`; equity avg `-0.1381` n `88`; fx avg `0.0067` n `6`; index avg `-0.0375` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.0366` n `763`
- 1h: commodity avg `-0.0255` n `12`; crypto_alt avg `0.8304` n `228`; crypto_major avg `1.0256` n `8`; equity avg `-0.0207` n `88`; fx avg `-0.0317` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0172` n `20`; unknown avg `0.5156` n `763`
- 4h: commodity avg `-0.0636` n `12`; crypto_alt avg `1.2651` n `228`; crypto_major avg `1.2655` n `8`; equity avg `0.0079` n `88`; fx avg `-0.0571` n `6`; index avg `-0.0221` n `25`; metal avg `0.0093` n `20`; unknown avg `1.6263` n `763`
- 24h: commodity avg `-0.4837` n `12`; crypto_alt avg `2.817` n `228`; crypto_major avg `2.8053` n `8`; equity avg `-2.0007` n `88`; fx avg `-0.1185` n `6`; index avg `-0.5642` n `25`; metal avg `1.0486` n `20`; unknown avg `3.3172` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
