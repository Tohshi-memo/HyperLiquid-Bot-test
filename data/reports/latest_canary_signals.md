# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T10:59:55.050093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1219` n `12`; crypto_alt avg `-0.1217` n `228`; crypto_major avg `-0.1096` n `8`; equity avg `0.0552` n `67`; fx avg `0.0056` n `6`; index avg `-0.0131` n `23`; metal avg `0.0214` n `18`; unknown avg `0.2034` n `396`
- 1h: commodity avg `-0.1089` n `12`; crypto_alt avg `0.0744` n `228`; crypto_major avg `0.0471` n `8`; equity avg `0.0603` n `67`; fx avg `0.0081` n `6`; index avg `-0.1034` n `23`; metal avg `-0.0519` n `18`; unknown avg `-0.1824` n `396`
- 4h: commodity avg `-0.1448` n `12`; crypto_alt avg `-1.367` n `228`; crypto_major avg `-0.9151` n `8`; equity avg `-0.098` n `67`; fx avg `-0.0197` n `6`; index avg `-0.1835` n `23`; metal avg `-0.0913` n `18`; unknown avg `0.0274` n `386`
- 24h: commodity avg `-0.3761` n `12`; crypto_alt avg `-5.4382` n `228`; crypto_major avg `-3.8338` n `8`; equity avg `-1.4552` n `67`; fx avg `0.059` n `6`; index avg `-0.1112` n `23`; metal avg `-0.7708` n `18`; unknown avg `-2.1558` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0437`, n `668`, weak_sample_signal
