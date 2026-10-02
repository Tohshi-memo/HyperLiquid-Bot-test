# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T00:52:26.670897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0562` n `13`; crypto_alt avg `0.016` n `234`; crypto_major avg `0.1897` n `8`; equity avg `-0.0093` n `142`; fx avg `-0.0113` n `6`; index avg `0.0042` n `26`; metal avg `-0.0127` n `20`; unknown avg `0.0559` n `985`
- 1h: commodity avg `-0.0538` n `13`; crypto_alt avg `0.2331` n `234`; crypto_major avg `0.1425` n `8`; equity avg `0.098` n `142`; fx avg `0.0497` n `6`; index avg `0.0387` n `26`; metal avg `-0.1613` n `20`; unknown avg `0.1205` n `977`
- 4h: commodity avg `-0.0421` n `13`; crypto_alt avg `0.0264` n `234`; crypto_major avg `0.1639` n `8`; equity avg `0.1737` n `142`; fx avg `0.0438` n `6`; index avg `0.0396` n `26`; metal avg `-0.0956` n `20`; unknown avg `-0.1262` n `935`
- 24h: commodity avg `-0.0357` n `13`; crypto_alt avg `-0.3093` n `234`; crypto_major avg `0.1574` n `8`; equity avg `1.1395` n `142`; fx avg `-0.1842` n `6`; index avg `0.188` n `26`; metal avg `0.0295` n `20`; unknown avg `-0.0223` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
