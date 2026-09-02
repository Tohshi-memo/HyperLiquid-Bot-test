# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T16:22:28.687486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `0.2251` n `232`; crypto_major avg `0.1794` n `8`; equity avg `0.0256` n `133`; fx avg `-0.0202` n `6`; index avg `-0.0105` n `26`; metal avg `-0.009` n `20`; unknown avg `0.2483` n `792`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.766` n `232`; crypto_major avg `0.6096` n `8`; equity avg `0.2052` n `133`; fx avg `0.0079` n `6`; index avg `0.0187` n `26`; metal avg `-0.0023` n `20`; unknown avg `16.8623` n `790`
- 4h: commodity avg `0.3387` n `12`; crypto_alt avg `0.3824` n `232`; crypto_major avg `0.672` n `8`; equity avg `0.3327` n `133`; fx avg `-0.1004` n `6`; index avg `0.0961` n `26`; metal avg `0.2306` n `20`; unknown avg `0.2828` n `789`
- 24h: commodity avg `0.4428` n `12`; crypto_alt avg `-0.2891` n `232`; crypto_major avg `-0.5646` n `8`; equity avg `-0.194` n `133`; fx avg `-0.3605` n `6`; index avg `-0.008` n `26`; metal avg `0.1148` n `20`; unknown avg `-0.0718` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
