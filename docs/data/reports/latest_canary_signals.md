# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T21:01:12.518021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0717` n `228`; crypto_major avg `-0.0876` n `8`; equity avg `0.0059` n `88`; fx avg `-0.0044` n `6`; index avg `0.0131` n `23`; metal avg `0.0123` n `20`; unknown avg `-0.0367` n `765`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.3568` n `228`; crypto_major avg `-0.3876` n `8`; equity avg `0.0685` n `88`; fx avg `0.0009` n `6`; index avg `0.0214` n `23`; metal avg `0.0483` n `20`; unknown avg `-0.0445` n `765`
- 4h: commodity avg `-0.0668` n `12`; crypto_alt avg `-0.046` n `228`; crypto_major avg `0.7978` n `8`; equity avg `0.6422` n `88`; fx avg `-0.0141` n `6`; index avg `0.0911` n `23`; metal avg `0.201` n `20`; unknown avg `-0.1844` n `765`
- 24h: commodity avg `-0.3591` n `12`; crypto_alt avg `1.4254` n `228`; crypto_major avg `2.7576` n `8`; equity avg `1.6673` n `88`; fx avg `0.171` n `6`; index avg `0.1633` n `23`; metal avg `-0.4844` n `20`; unknown avg `1.2841` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
