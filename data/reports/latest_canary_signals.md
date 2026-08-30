# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T01:22:22.638269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `-0.1595` n `231`; crypto_major avg `-0.0054` n `8`; equity avg `0.0265` n `128`; fx avg `-0.0004` n `6`; index avg `0.0032` n `26`; metal avg `0.0015` n `20`; unknown avg `0.0294` n `793`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `-0.3328` n `231`; crypto_major avg `-0.1907` n `8`; equity avg `0.0076` n `128`; fx avg `-0.0017` n `6`; index avg `-0.0155` n `26`; metal avg `-0.0122` n `20`; unknown avg `4.1065` n `793`
- 4h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.2206` n `231`; crypto_major avg `-0.0374` n `8`; equity avg `0.0388` n `128`; fx avg `0.0194` n `6`; index avg `0.0159` n `26`; metal avg `-0.0077` n `20`; unknown avg `4.1936` n `774`
- 24h: commodity avg `-0.0269` n `12`; crypto_alt avg `0.0871` n `231`; crypto_major avg `0.8572` n `8`; equity avg `0.3811` n `128`; fx avg `0.002` n `6`; index avg `0.0994` n `26`; metal avg `0.1096` n `20`; unknown avg `0.1115` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
