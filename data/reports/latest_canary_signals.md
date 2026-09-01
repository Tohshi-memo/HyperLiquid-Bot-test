# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T13:07:26.605477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `-0.3664` n `232`; crypto_major avg `-0.3656` n `8`; equity avg `-0.1334` n `131`; fx avg `0.0019` n `6`; index avg `-0.0257` n `26`; metal avg `-0.1193` n `20`; unknown avg `-0.0395` n `790`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.8513` n `232`; crypto_major avg `-0.6429` n `8`; equity avg `-0.2818` n `130`; fx avg `-0.0104` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0697` n `20`; unknown avg `-0.1205` n `790`
- 4h: commodity avg `-0.0895` n `12`; crypto_alt avg `0.137` n `232`; crypto_major avg `-0.1516` n `8`; equity avg `-0.4943` n `130`; fx avg `0.01` n `6`; index avg `-0.0708` n `26`; metal avg `-0.0908` n `20`; unknown avg `-0.5877` n `790`
- 24h: commodity avg `0.4153` n `12`; crypto_alt avg `0.6042` n `232`; crypto_major avg `-0.1095` n `8`; equity avg `-0.7671` n `130`; fx avg `0.07` n `6`; index avg `-0.2842` n `26`; metal avg `-0.7155` n `20`; unknown avg `-0.1878` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0396`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0309`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0305`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0286`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0285`, n `668`, weak_sample_signal
