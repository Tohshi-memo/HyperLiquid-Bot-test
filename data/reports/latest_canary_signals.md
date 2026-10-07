# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T17:52:34.397151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.096` n `13`; crypto_alt avg `-0.3194` n `235`; crypto_major avg `-0.2329` n `8`; equity avg `-0.0704` n `150`; fx avg `-0.0015` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0442` n `20`; unknown avg `1.2041` n `1077`
- 1h: commodity avg `-0.4054` n `13`; crypto_alt avg `-0.6723` n `235`; crypto_major avg `-0.6502` n `8`; equity avg `0.0763` n `150`; fx avg `-0.0164` n `6`; index avg `0.0237` n `26`; metal avg `-0.0309` n `20`; unknown avg `1.0105` n `1074`
- 4h: commodity avg `-0.6232` n `13`; crypto_alt avg `-0.3191` n `235`; crypto_major avg `-0.6965` n `8`; equity avg `0.3635` n `150`; fx avg `-0.0189` n `6`; index avg `0.1537` n `26`; metal avg `0.1636` n `20`; unknown avg `0.0989` n `1056`
- 24h: commodity avg `0.2452` n `13`; crypto_alt avg `-5.4365` n `235`; crypto_major avg `-3.9517` n `8`; equity avg `-1.7788` n `150`; fx avg `-0.1976` n `6`; index avg `-0.2797` n `26`; metal avg `-0.648` n `20`; unknown avg `15.6845` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
