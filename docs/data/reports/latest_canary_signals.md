# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T17:37:27.671924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0776` n `12`; crypto_alt avg `0.3162` n `233`; crypto_major avg `0.3025` n `8`; equity avg `-0.0369` n `135`; fx avg `0.0055` n `6`; index avg `-0.0179` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.127` n `797`
- 1h: commodity avg `0.0799` n `12`; crypto_alt avg `1.1715` n `233`; crypto_major avg `0.9767` n `8`; equity avg `0.2158` n `135`; fx avg `-0.0072` n `6`; index avg `0.0131` n `26`; metal avg `0.003` n `20`; unknown avg `1.4047` n `794`
- 4h: commodity avg `0.4611` n `12`; crypto_alt avg `0.4372` n `233`; crypto_major avg `0.4042` n `8`; equity avg `0.0961` n `135`; fx avg `0.0337` n `6`; index avg `-0.0281` n `26`; metal avg `-0.1394` n `20`; unknown avg `-0.0565` n `760`
- 24h: commodity avg `0.9638` n `12`; crypto_alt avg `-4.1805` n `233`; crypto_major avg `-3.3667` n `8`; equity avg `-1.888` n `135`; fx avg `0.0764` n `6`; index avg `-0.2982` n `26`; metal avg `-1.208` n `20`; unknown avg `-0.6542` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
