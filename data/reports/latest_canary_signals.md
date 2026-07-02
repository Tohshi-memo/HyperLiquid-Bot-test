# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T21:21:34.002388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.77` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.0534` n `229`; crypto_major avg `0.0149` n `8`; equity avg `-0.0102` n `88`; fx avg `0.0539` n `6`; index avg `0.0029` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.1036` n `765`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `0.1687` n `229`; crypto_major avg `0.077` n `8`; equity avg `-0.0973` n `88`; fx avg `-0.0` n `6`; index avg `0.0024` n `25`; metal avg `0.0198` n `20`; unknown avg `-0.3704` n `765`
- 4h: commodity avg `0.1071` n `12`; crypto_alt avg `0.0106` n `229`; crypto_major avg `-0.3421` n `8`; equity avg `0.3566` n `88`; fx avg `0.0391` n `6`; index avg `0.1259` n `25`; metal avg `0.1237` n `20`; unknown avg `0.0753` n `764`
- 24h: commodity avg `0.1008` n `12`; crypto_alt avg `1.6555` n `228`; crypto_major avg `2.4582` n `8`; equity avg `-2.4024` n `88`; fx avg `-0.1301` n `6`; index avg `-0.4682` n `25`; metal avg `1.0266` n `20`; unknown avg `1.8225` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
