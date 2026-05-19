# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T03:22:14.058162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `12`; crypto_alt avg `0.1521` n `228`; crypto_major avg `0.1294` n `8`; equity avg `0.1008` n `66`; fx avg `0.0081` n `6`; index avg `0.0348` n `23`; metal avg `0.0296` n `18`; unknown avg `-0.0263` n `383`
- 1h: commodity avg `0.1624` n `12`; crypto_alt avg `-0.2043` n `228`; crypto_major avg `-0.022` n `8`; equity avg `0.2542` n `66`; fx avg `0.019` n `6`; index avg `0.097` n `23`; metal avg `-0.1242` n `18`; unknown avg `-0.2178` n `383`
- 4h: commodity avg `0.2715` n `12`; crypto_alt avg `-0.2219` n `228`; crypto_major avg `-0.3396` n `8`; equity avg `-0.7018` n `66`; fx avg `0.1737` n `6`; index avg `-0.4431` n `23`; metal avg `-1.3095` n `18`; unknown avg `-0.4863` n `383`
- 24h: commodity avg `0.2722` n `12`; crypto_alt avg `0.6334` n `228`; crypto_major avg `0.3382` n `8`; equity avg `-0.7236` n `66`; fx avg `0.2517` n `6`; index avg `-0.2589` n `23`; metal avg `0.8787` n `18`; unknown avg `0.4234` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
