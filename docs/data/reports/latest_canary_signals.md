# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T03:22:26.283174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `12`; crypto_alt avg `-0.1444` n `228`; crypto_major avg `-0.2613` n `8`; equity avg `-0.1258` n `88`; fx avg `0.0011` n `6`; index avg `-0.0331` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.2024` n `763`
- 1h: commodity avg `-0.0671` n `12`; crypto_alt avg `0.0673` n `228`; crypto_major avg `0.0656` n `8`; equity avg `-0.2912` n `88`; fx avg `0.0044` n `6`; index avg `-0.073` n `25`; metal avg `0.1175` n `20`; unknown avg `-0.2246` n `763`
- 4h: commodity avg `-0.1414` n `12`; crypto_alt avg `0.447` n `228`; crypto_major avg `0.0703` n `8`; equity avg `-0.055` n `88`; fx avg `0.0017` n `6`; index avg `0.0217` n `25`; metal avg `0.4093` n `20`; unknown avg `-0.509` n `761`
- 24h: commodity avg `-0.6984` n `12`; crypto_alt avg `1.9463` n `228`; crypto_major avg `1.0549` n `8`; equity avg `-1.3193` n `88`; fx avg `-0.0416` n `6`; index avg `-0.3094` n `25`; metal avg `1.0075` n `20`; unknown avg `25.2338` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
