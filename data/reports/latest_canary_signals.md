# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T06:52:32.449519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.0575` n `228`; crypto_major avg `0.1155` n `8`; equity avg `0.0326` n `88`; fx avg `-0.0035` n `6`; index avg `-0.0018` n `23`; metal avg `0.0044` n `20`; unknown avg `-0.1082` n `764`
- 1h: commodity avg `0.0785` n `12`; crypto_alt avg `-0.1642` n `228`; crypto_major avg `0.0447` n `8`; equity avg `0.0229` n `88`; fx avg `-0.0028` n `6`; index avg `-0.0152` n `23`; metal avg `0.0283` n `20`; unknown avg `-0.3061` n `732`
- 4h: commodity avg `-0.1204` n `12`; crypto_alt avg `-0.0294` n `228`; crypto_major avg `-0.2225` n `8`; equity avg `0.0273` n `88`; fx avg `-0.0034` n `6`; index avg `0.0008` n `23`; metal avg `0.0101` n `20`; unknown avg `-0.4786` n `732`
- 24h: commodity avg `0.2818` n `12`; crypto_alt avg `-0.8091` n `228`; crypto_major avg `-1.4268` n `8`; equity avg `-0.0917` n `88`; fx avg `-0.0238` n `6`; index avg `-0.1419` n `23`; metal avg `-0.0527` n `20`; unknown avg `15.9376` n `682`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.219`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
