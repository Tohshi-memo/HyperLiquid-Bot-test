# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T19:22:31.259761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.1131` n `231`; crypto_major avg `-0.1209` n `8`; equity avg `0.0118` n `127`; fx avg `0.0037` n `6`; index avg `0.01` n `26`; metal avg `-0.0399` n `20`; unknown avg `-0.0495` n `792`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `0.3094` n `231`; crypto_major avg `0.7317` n `8`; equity avg `0.1819` n `127`; fx avg `0.0068` n `6`; index avg `0.0264` n `26`; metal avg `0.0438` n `20`; unknown avg `0.0082` n `792`
- 4h: commodity avg `0.2706` n `12`; crypto_alt avg `-0.2049` n `231`; crypto_major avg `0.2404` n `8`; equity avg `0.2416` n `127`; fx avg `0.0174` n `6`; index avg `0.003` n `26`; metal avg `0.2435` n `20`; unknown avg `0.2575` n `792`
- 24h: commodity avg `0.4234` n `12`; crypto_alt avg `3.0845` n `231`; crypto_major avg `4.2836` n `8`; equity avg `1.4543` n `127`; fx avg `-0.0332` n `6`; index avg `0.1207` n `26`; metal avg `0.2376` n `20`; unknown avg `1.1943` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
