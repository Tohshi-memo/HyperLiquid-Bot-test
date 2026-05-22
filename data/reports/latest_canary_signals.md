# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T12:37:14.106310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.039` n `12`; crypto_alt avg `0.1004` n `228`; crypto_major avg `0.1332` n `8`; equity avg `0.0246` n `67`; fx avg `0.0037` n `6`; index avg `0.0197` n `23`; metal avg `-0.2114` n `18`; unknown avg `0.4323` n `386`
- 1h: commodity avg `-0.8438` n `12`; crypto_alt avg `0.3905` n `228`; crypto_major avg `0.6446` n `8`; equity avg `0.2573` n `67`; fx avg `-0.0069` n `6`; index avg `0.1255` n `23`; metal avg `-0.4751` n `18`; unknown avg `0.6012` n `386`
- 4h: commodity avg `-1.0484` n `12`; crypto_alt avg `0.4363` n `228`; crypto_major avg `0.7815` n `8`; equity avg `-0.294` n `67`; fx avg `-0.0411` n `6`; index avg `-0.0929` n `23`; metal avg `-0.3698` n `18`; unknown avg `0.0252` n `386`
- 24h: commodity avg `-1.6496` n `12`; crypto_alt avg `2.8453` n `228`; crypto_major avg `1.6326` n `8`; equity avg `1.4438` n `67`; fx avg `0.0974` n `6`; index avg `0.9121` n `23`; metal avg `0.4086` n `18`; unknown avg `1.3401` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0428`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0399`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0355`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0342`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0325`, n `668`, weak_sample_signal
