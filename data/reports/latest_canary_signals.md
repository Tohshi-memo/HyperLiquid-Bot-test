# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T07:37:26.463836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0365` n `13`; crypto_alt avg `-0.1937` n `237`; crypto_major avg `-0.1907` n `8`; equity avg `-0.0924` n `151`; fx avg `-0.004` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0451` n `20`; unknown avg `-0.086` n `1198`
- 1h: commodity avg `0.1128` n `13`; crypto_alt avg `-0.2109` n `237`; crypto_major avg `-0.2721` n `8`; equity avg `-0.0584` n `151`; fx avg `-0.0133` n `6`; index avg `-0.0192` n `26`; metal avg `0.0221` n `20`; unknown avg `0.4571` n `1196`
- 4h: commodity avg `0.1174` n `13`; crypto_alt avg `-0.5789` n `237`; crypto_major avg `-0.5549` n `8`; equity avg `-0.7411` n `151`; fx avg `-0.0217` n `6`; index avg `-0.1035` n `26`; metal avg `-0.0699` n `20`; unknown avg `0.9015` n `1168`
- 24h: commodity avg `0.4941` n `13`; crypto_alt avg `-0.6255` n `237`; crypto_major avg `-1.2628` n `8`; equity avg `-1.683` n `151`; fx avg `0.0064` n `6`; index avg `-0.2513` n `26`; metal avg `-0.2608` n `20`; unknown avg `4.9103` n `1013`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
