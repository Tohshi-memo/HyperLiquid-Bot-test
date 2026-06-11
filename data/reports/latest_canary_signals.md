# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T12:22:27.072793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.6149` n `12`; crypto_alt avg `-0.7147` n `228`; crypto_major avg `-0.5631` n `8`; equity avg `-0.5013` n `74`; fx avg `-0.0146` n `6`; index avg `-0.1897` n `23`; metal avg `-0.3968` n `18`; unknown avg `0.097` n `556`
- 1h: commodity avg `0.6594` n `12`; crypto_alt avg `-0.6085` n `228`; crypto_major avg `-0.5083` n `8`; equity avg `-0.2311` n `74`; fx avg `-0.0131` n `6`; index avg `-0.0343` n `23`; metal avg `-0.3388` n `18`; unknown avg `0.1184` n `556`
- 4h: commodity avg `0.6025` n `12`; crypto_alt avg `-0.6364` n `228`; crypto_major avg `-0.2829` n `8`; equity avg `-0.3506` n `74`; fx avg `-0.0424` n `6`; index avg `-0.1162` n `23`; metal avg `-0.8726` n `18`; unknown avg `0.872` n `556`
- 24h: commodity avg `-0.0024` n `12`; crypto_alt avg `1.8372` n `228`; crypto_major avg `1.8185` n `8`; equity avg `1.1457` n `74`; fx avg `0.0167` n `6`; index avg `0.2843` n `23`; metal avg `-0.3934` n `18`; unknown avg `5.344` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
