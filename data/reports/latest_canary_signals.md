# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T18:07:37.957700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6964` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5279` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.0851` n `228`; crypto_major avg `-0.0615` n `8`; equity avg `-0.0895` n `88`; fx avg `0.0003` n `6`; index avg `-0.0113` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.4888` n `763`
- 1h: commodity avg `-0.0169` n `12`; crypto_alt avg `0.2085` n `228`; crypto_major avg `0.5132` n `8`; equity avg `-0.0273` n `88`; fx avg `-0.0007` n `6`; index avg `-0.015` n `25`; metal avg `-0.0263` n `20`; unknown avg `0.5422` n `763`
- 4h: commodity avg `-0.151` n `12`; crypto_alt avg `0.7418` n `228`; crypto_major avg `1.2281` n `8`; equity avg `-0.4683` n `88`; fx avg `-0.031` n `6`; index avg `-0.1887` n `25`; metal avg `-0.2998` n `20`; unknown avg `0.9135` n `763`
- 24h: commodity avg `-0.5857` n `12`; crypto_alt avg `2.1074` n `228`; crypto_major avg `2.2444` n `8`; equity avg `-0.5959` n `88`; fx avg `-0.0147` n `6`; index avg `-0.4723` n `25`; metal avg `0.2217` n `20`; unknown avg `0.7449` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
