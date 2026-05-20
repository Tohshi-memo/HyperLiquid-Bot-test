# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T21:22:15.035344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1784` n `12`; crypto_alt avg `-0.2669` n `228`; crypto_major avg `-0.0146` n `8`; equity avg `-0.0414` n `66`; fx avg `0.0069` n `6`; index avg `-0.0179` n `23`; metal avg `0.0041` n `18`; unknown avg `-0.0222` n `384`
- 1h: commodity avg `0.2014` n `12`; crypto_alt avg `0.314` n `228`; crypto_major avg `0.2946` n `8`; equity avg `0.3756` n `66`; fx avg `0.004` n `6`; index avg `0.0392` n `23`; metal avg `-0.0172` n `18`; unknown avg `0.0475` n `384`
- 4h: commodity avg `0.6323` n `12`; crypto_alt avg `-0.1288` n `228`; crypto_major avg `-0.157` n `8`; equity avg `0.1488` n `66`; fx avg `-0.0325` n `6`; index avg `0.0799` n `23`; metal avg `-0.0496` n `18`; unknown avg `0.1463` n `384`
- 24h: commodity avg `-2.3226` n `12`; crypto_alt avg `2.4654` n `228`; crypto_major avg `1.7487` n `8`; equity avg `1.7024` n `66`; fx avg `-0.0729` n `6`; index avg `1.1406` n `23`; metal avg `1.5329` n `18`; unknown avg `0.8156` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
