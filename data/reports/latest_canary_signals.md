# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T21:52:31.372603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `0.088` n `231`; crypto_major avg `0.0061` n `8`; equity avg `-0.0057` n `128`; fx avg `0.0014` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.2254` n `778`
- 1h: commodity avg `0.0176` n `12`; crypto_alt avg `0.085` n `231`; crypto_major avg `-0.01` n `8`; equity avg `0.0005` n `128`; fx avg `-0.0019` n `6`; index avg `-0.0027` n `26`; metal avg `0.007` n `20`; unknown avg `-0.2056` n `778`
- 4h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.2433` n `231`; crypto_major avg `0.1353` n `8`; equity avg `0.1891` n `128`; fx avg `-0.0234` n `6`; index avg `0.0312` n `26`; metal avg `0.0186` n `20`; unknown avg `0.1938` n `778`
- 24h: commodity avg `-0.0374` n `12`; crypto_alt avg `1.2207` n `231`; crypto_major avg `1.3601` n `8`; equity avg `0.4024` n `128`; fx avg `-0.0745` n `6`; index avg `0.0838` n `26`; metal avg `0.1392` n `20`; unknown avg `4804.8898` n `742`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
