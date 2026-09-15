# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T14:07:32.805866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.1571` n `233`; crypto_major avg `0.1737` n `8`; equity avg `-0.1728` n `136`; fx avg `-0.0058` n `6`; index avg `-0.0388` n `27`; metal avg `-0.0072` n `20`; unknown avg `2.9124` n `904`
- 1h: commodity avg `0.2212` n `12`; crypto_alt avg `-0.7235` n `233`; crypto_major avg `-0.9391` n `8`; equity avg `-0.3223` n `136`; fx avg `0.0123` n `6`; index avg `-0.0947` n `27`; metal avg `0.0672` n `20`; unknown avg `3.3398` n `888`
- 4h: commodity avg `0.077` n `12`; crypto_alt avg `-0.3789` n `233`; crypto_major avg `-0.3184` n `8`; equity avg `-0.0245` n `136`; fx avg `0.0142` n `6`; index avg `0.0134` n `27`; metal avg `0.235` n `20`; unknown avg `5.3168` n `882`
- 24h: commodity avg `-0.0525` n `12`; crypto_alt avg `-1.3659` n `233`; crypto_major avg `-1.2585` n `8`; equity avg `-0.2105` n `136`; fx avg `0.1687` n `6`; index avg `-0.0159` n `27`; metal avg `0.294` n `20`; unknown avg `1.0626` n `814`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
