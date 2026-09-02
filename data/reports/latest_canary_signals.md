# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T12:52:30.213282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0429` n `12`; crypto_alt avg `-0.265` n `232`; crypto_major avg `-0.1849` n `8`; equity avg `-0.0953` n `132`; fx avg `0.0051` n `6`; index avg `-0.0281` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.1737` n `792`
- 1h: commodity avg `0.109` n `12`; crypto_alt avg `-0.034` n `232`; crypto_major avg `-0.008` n `8`; equity avg `0.3036` n `132`; fx avg `-0.0036` n `6`; index avg `0.019` n `26`; metal avg `0.0246` n `20`; unknown avg `0.4836` n `790`
- 4h: commodity avg `-0.1146` n `12`; crypto_alt avg `-0.6982` n `232`; crypto_major avg `-0.2958` n `8`; equity avg `0.2228` n `132`; fx avg `-0.0584` n `6`; index avg `0.0408` n `26`; metal avg `0.2214` n `20`; unknown avg `0.1115` n `790`
- 24h: commodity avg `0.5423` n `12`; crypto_alt avg `-1.1904` n `232`; crypto_major avg `-2.2292` n `8`; equity avg `-1.0111` n `131`; fx avg `-0.2582` n `6`; index avg `-0.1546` n `26`; metal avg `-0.241` n `20`; unknown avg `0.3072` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
