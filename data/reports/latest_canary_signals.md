# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T03:07:31.785886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0527` n `13`; crypto_alt avg `-0.0528` n `235`; crypto_major avg `-0.1497` n `8`; equity avg `-0.1381` n `150`; fx avg `-0.008` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0207` n `20`; unknown avg `0.4896` n `1076`
- 1h: commodity avg `-0.0169` n `13`; crypto_alt avg `-0.0311` n `235`; crypto_major avg `0.0787` n `8`; equity avg `-0.1553` n `150`; fx avg `-0.0082` n `6`; index avg `0.0055` n `26`; metal avg `0.0157` n `20`; unknown avg `0.1892` n `1076`
- 4h: commodity avg `-0.1026` n `13`; crypto_alt avg `0.6555` n `235`; crypto_major avg `0.3445` n `8`; equity avg `0.2072` n `150`; fx avg `0.0271` n `6`; index avg `0.0695` n `26`; metal avg `0.367` n `20`; unknown avg `0.7323` n `1069`
- 24h: commodity avg `0.1768` n `13`; crypto_alt avg `-2.3111` n `235`; crypto_major avg `-2.8818` n `8`; equity avg `-2.2265` n `150`; fx avg `0.0956` n `6`; index avg `-0.233` n `26`; metal avg `0.0818` n `20`; unknown avg `6.6702` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
