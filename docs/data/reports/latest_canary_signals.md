# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T19:52:30.163016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `0.0011` n `230`; crypto_major avg `0.0316` n `8`; equity avg `0.1385` n `112`; fx avg `-0.0063` n `6`; index avg `0.0162` n `25`; metal avg `-0.0286` n `20`; unknown avg `-0.0162` n `782`
- 1h: commodity avg `-0.2748` n `12`; crypto_alt avg `0.3085` n `230`; crypto_major avg `0.5765` n `8`; equity avg `0.3725` n `112`; fx avg `-0.0232` n `6`; index avg `0.0853` n `25`; metal avg `0.0505` n `20`; unknown avg `-0.009` n `782`
- 4h: commodity avg `-0.3015` n `12`; crypto_alt avg `-0.125` n `230`; crypto_major avg `-0.321` n `8`; equity avg `-0.0778` n `112`; fx avg `-0.0257` n `6`; index avg `0.0069` n `25`; metal avg `0.0884` n `20`; unknown avg `-0.2001` n `782`
- 24h: commodity avg `-0.0704` n `12`; crypto_alt avg `0.0643` n `230`; crypto_major avg `0.0671` n `8`; equity avg `1.964` n `112`; fx avg `-0.1634` n `6`; index avg `0.1129` n `25`; metal avg `0.3991` n `20`; unknown avg `0.0078` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
