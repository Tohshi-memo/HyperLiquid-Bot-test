# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T11:07:14.962025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1113` n `12`; crypto_alt avg `-0.0676` n `228`; crypto_major avg `0.0527` n `8`; equity avg `0.0218` n `66`; fx avg `0.0403` n `6`; index avg `0.0356` n `23`; metal avg `0.0773` n `18`; unknown avg `0.4481` n `384`
- 1h: commodity avg `-0.2167` n `12`; crypto_alt avg `-0.0547` n `228`; crypto_major avg `0.2151` n `8`; equity avg `0.008` n `66`; fx avg `0.0431` n `6`; index avg `0.0161` n `23`; metal avg `0.1498` n `18`; unknown avg `0.8972` n `384`
- 4h: commodity avg `-0.4215` n `12`; crypto_alt avg `0.0755` n `228`; crypto_major avg `0.4433` n `8`; equity avg `0.4297` n `66`; fx avg `0.0232` n `6`; index avg `0.2815` n `23`; metal avg `0.4381` n `18`; unknown avg `0.3414` n `384`
- 24h: commodity avg `-0.5472` n `12`; crypto_alt avg `0.7834` n `228`; crypto_major avg `0.5909` n `8`; equity avg `1.4225` n `66`; fx avg `-0.0853` n `6`; index avg `0.1617` n `23`; metal avg `-0.7145` n `18`; unknown avg `0.9124` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
