# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T11:37:33.358940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `12`; crypto_alt avg `-0.0793` n `229`; crypto_major avg `-0.1776` n `8`; equity avg `-0.2276` n `91`; fx avg `0.009` n `6`; index avg `-0.0297` n `25`; metal avg `-0.0703` n `20`; unknown avg `-0.0133` n `766`
- 1h: commodity avg `0.158` n `12`; crypto_alt avg `-0.231` n `229`; crypto_major avg `-0.2276` n `8`; equity avg `0.1137` n `91`; fx avg `0.0207` n `6`; index avg `-0.0085` n `25`; metal avg `-0.0915` n `20`; unknown avg `-0.025` n `766`
- 4h: commodity avg `0.2434` n `12`; crypto_alt avg `0.4571` n `229`; crypto_major avg `0.5614` n `8`; equity avg `0.5107` n `91`; fx avg `0.0173` n `6`; index avg `0.072` n `25`; metal avg `-0.1635` n `20`; unknown avg `0.1008` n `765`
- 24h: commodity avg `-0.8942` n `12`; crypto_alt avg `1.3014` n `229`; crypto_major avg `1.9584` n `8`; equity avg `0.7325` n `91`; fx avg `-0.1015` n `6`; index avg `0.221` n `25`; metal avg `0.1343` n `20`; unknown avg `0.0489` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
