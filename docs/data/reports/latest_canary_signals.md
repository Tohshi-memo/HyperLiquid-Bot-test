# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T17:52:29.227627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0783` n `233`; crypto_major avg `-0.0352` n `8`; equity avg `-0.0027` n `136`; fx avg `-0.0021` n `6`; index avg `0.0011` n `26`; metal avg `-0.0055` n `20`; unknown avg `-0.0834` n `838`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `-0.0562` n `233`; crypto_major avg `-0.0726` n `8`; equity avg `-0.0364` n `136`; fx avg `0.0005` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0113` n `20`; unknown avg `5.4322` n `796`
- 4h: commodity avg `0.0345` n `12`; crypto_alt avg `0.3327` n `233`; crypto_major avg `-0.0931` n `8`; equity avg `0.0124` n `136`; fx avg `-0.0023` n `6`; index avg `0.0072` n `26`; metal avg `0.0027` n `20`; unknown avg `2.6184` n `790`
- 24h: commodity avg `-0.1109` n `12`; crypto_alt avg `0.6552` n `233`; crypto_major avg `-0.4294` n `8`; equity avg `-0.4194` n `136`; fx avg `-0.02` n `6`; index avg `-0.0207` n `26`; metal avg `-0.0567` n `20`; unknown avg `1.0879` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
