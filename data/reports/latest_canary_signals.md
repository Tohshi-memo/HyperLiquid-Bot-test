# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T14:22:27.892640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0651` n `12`; crypto_alt avg `-0.2611` n `229`; crypto_major avg `-0.2114` n `8`; equity avg `-0.6257` n `91`; fx avg `-0.0008` n `6`; index avg `-0.1` n `25`; metal avg `-0.0452` n `20`; unknown avg `0.0482` n `763`
- 1h: commodity avg `0.1895` n `12`; crypto_alt avg `-0.5074` n `229`; crypto_major avg `-0.2619` n `8`; equity avg `-1.5836` n `91`; fx avg `-0.0006` n `6`; index avg `-0.202` n `25`; metal avg `-0.1047` n `20`; unknown avg `0.0844` n `763`
- 4h: commodity avg `0.1995` n `12`; crypto_alt avg `-0.8876` n `229`; crypto_major avg `-0.588` n `8`; equity avg `-1.9797` n `91`; fx avg `-0.0317` n `6`; index avg `-0.2335` n `25`; metal avg `0.0341` n `20`; unknown avg `0.0589` n `763`
- 24h: commodity avg `0.4392` n `12`; crypto_alt avg `0.3666` n `229`; crypto_major avg `0.7478` n `8`; equity avg `-3.6673` n `90`; fx avg `-0.1814` n `6`; index avg `-0.6708` n `25`; metal avg `0.0118` n `20`; unknown avg `0.1651` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
