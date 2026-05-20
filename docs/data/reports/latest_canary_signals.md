# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T11:52:15.517623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1881` n `12`; crypto_alt avg `-0.272` n `228`; crypto_major avg `-0.16` n `8`; equity avg `-0.1239` n `66`; fx avg `-0.0155` n `6`; index avg `-0.0521` n `23`; metal avg `-0.121` n `18`; unknown avg `1.0608` n `384`
- 1h: commodity avg `0.5493` n `12`; crypto_alt avg `-0.4118` n `228`; crypto_major avg `-0.2636` n `8`; equity avg `-0.1006` n `66`; fx avg `0.0524` n `6`; index avg `0.0516` n `23`; metal avg `-0.0209` n `18`; unknown avg `1.8735` n `384`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `-0.1767` n `228`; crypto_major avg `0.2506` n `8`; equity avg `0.3768` n `66`; fx avg `0.0335` n `6`; index avg `0.2659` n `23`; metal avg `0.4094` n `18`; unknown avg `-0.3718` n `384`
- 24h: commodity avg `-0.2457` n `12`; crypto_alt avg `0.7754` n `228`; crypto_major avg `0.6364` n `8`; equity avg `1.5293` n `66`; fx avg `-0.0714` n `6`; index avg `0.2565` n `23`; metal avg `-0.6707` n `18`; unknown avg `0.4393` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
