# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T21:22:31.805907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `0.3475` n `228`; crypto_major avg `0.3379` n `8`; equity avg `0.1184` n `88`; fx avg `0.0427` n `6`; index avg `0.0304` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0973` n `763`
- 1h: commodity avg `0.0296` n `12`; crypto_alt avg `0.8152` n `228`; crypto_major avg `0.6958` n `8`; equity avg `0.3034` n `88`; fx avg `0.0461` n `6`; index avg `0.0421` n `25`; metal avg `-0.0371` n `20`; unknown avg `0.2976` n `763`
- 4h: commodity avg `-0.0333` n `12`; crypto_alt avg `-0.0428` n `228`; crypto_major avg `-0.0157` n `8`; equity avg `-0.7089` n `88`; fx avg `0.0535` n `6`; index avg `-0.1209` n `25`; metal avg `-0.3477` n `20`; unknown avg `0.5129` n `761`
- 24h: commodity avg `-0.614` n `12`; crypto_alt avg `2.487` n `228`; crypto_major avg `2.0489` n `8`; equity avg `-1.5012` n `88`; fx avg `0.064` n `6`; index avg `-0.4919` n `25`; metal avg `0.1806` n `20`; unknown avg `0.8115` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
