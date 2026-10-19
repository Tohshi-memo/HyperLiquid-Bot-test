# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T14:52:29.694736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `0.6465` n `237`; crypto_major avg `0.5086` n `8`; equity avg `0.2381` n `151`; fx avg `0.002` n `6`; index avg `0.0108` n `26`; metal avg `0.0139` n `20`; unknown avg `0.714` n `1195`
- 1h: commodity avg `-0.0193` n `13`; crypto_alt avg `0.1524` n `237`; crypto_major avg `0.0891` n `8`; equity avg `0.0458` n `151`; fx avg `-0.0037` n `6`; index avg `0.0295` n `26`; metal avg `-0.0405` n `20`; unknown avg `1.0264` n `1139`
- 4h: commodity avg `-0.1927` n `13`; crypto_alt avg `0.2386` n `237`; crypto_major avg `-0.0802` n `8`; equity avg `-0.1967` n `151`; fx avg `0.0308` n `6`; index avg `-0.0363` n `26`; metal avg `-0.1724` n `20`; unknown avg `0.6919` n `1103`
- 24h: commodity avg `-0.3572` n `13`; crypto_alt avg `1.1621` n `237`; crypto_major avg `1.7174` n `8`; equity avg `3.1229` n `151`; fx avg `-0.0259` n `6`; index avg `0.5585` n `26`; metal avg `0.0869` n `20`; unknown avg `3.5483` n `915`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
