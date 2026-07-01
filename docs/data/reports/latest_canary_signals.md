# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T23:52:25.545394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.1318` n `228`; crypto_major avg `-0.174` n `8`; equity avg `-0.0729` n `88`; fx avg `-0.0116` n `6`; index avg `-0.0602` n `25`; metal avg `-0.0482` n `20`; unknown avg `0.3916` n `763`
- 1h: commodity avg `-0.0248` n `12`; crypto_alt avg `-0.813` n `228`; crypto_major avg `-0.6747` n `8`; equity avg `-0.3978` n `88`; fx avg `-0.0097` n `6`; index avg `-0.0945` n `25`; metal avg `-0.1063` n `20`; unknown avg `141.4028` n `763`
- 4h: commodity avg `-0.0166` n `12`; crypto_alt avg `0.0419` n `228`; crypto_major avg `-0.3561` n `8`; equity avg `-0.4077` n `88`; fx avg `0.0327` n `6`; index avg `-0.1038` n `25`; metal avg `-0.0464` n `20`; unknown avg `143.1627` n `763`
- 24h: commodity avg `-0.6408` n `12`; crypto_alt avg `1.6003` n `228`; crypto_major avg `1.0554` n `8`; equity avg `-2.0137` n `88`; fx avg `0.0264` n `6`; index avg `-0.592` n `25`; metal avg `0.2642` n `20`; unknown avg `147.8842` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
