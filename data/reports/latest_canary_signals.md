# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T13:37:18.689612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1354` n `12`; crypto_alt avg `-0.1858` n `228`; crypto_major avg `-0.1187` n `8`; equity avg `0.309` n `67`; fx avg `-0.0101` n `6`; index avg `0.1876` n `23`; metal avg `-0.1628` n `18`; unknown avg `-0.0754` n `386`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `0.1305` n `228`; crypto_major avg `-0.0804` n `8`; equity avg `0.5043` n `67`; fx avg `-0.003` n `6`; index avg `0.3088` n `23`; metal avg `0.3007` n `18`; unknown avg `-0.0224` n `386`
- 4h: commodity avg `-0.7049` n `12`; crypto_alt avg `0.6067` n `228`; crypto_major avg `0.6326` n `8`; equity avg `0.6922` n `67`; fx avg `-0.0304` n `6`; index avg `0.3906` n `23`; metal avg `-0.1824` n `18`; unknown avg `0.4653` n `386`
- 24h: commodity avg `-2.3536` n `12`; crypto_alt avg `2.9121` n `228`; crypto_major avg `1.284` n `8`; equity avg `1.698` n `67`; fx avg `0.1168` n `6`; index avg `1.2385` n `23`; metal avg `0.9536` n `18`; unknown avg `1.676` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0404`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0375`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0373`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0358`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0356`, n `668`, weak_sample_signal
