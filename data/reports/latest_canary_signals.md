# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T06:37:24.172215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `0.0578` n `232`; crypto_major avg `0.0372` n `8`; equity avg `-0.0088` n `128`; fx avg `0.0269` n `6`; index avg `0.0102` n `26`; metal avg `0.0256` n `20`; unknown avg `-0.07` n `793`
- 1h: commodity avg `-0.0928` n `12`; crypto_alt avg `0.2432` n `232`; crypto_major avg `0.1835` n `8`; equity avg `0.418` n `128`; fx avg `-0.0404` n `6`; index avg `0.0744` n `26`; metal avg `0.0586` n `20`; unknown avg `0.1326` n `773`
- 4h: commodity avg `-0.002` n `12`; crypto_alt avg `0.9888` n `231`; crypto_major avg `0.564` n `8`; equity avg `1.1626` n `128`; fx avg `-0.0431` n `6`; index avg `0.2382` n `26`; metal avg `0.2407` n `20`; unknown avg `0.499` n `773`
- 24h: commodity avg `0.4194` n `12`; crypto_alt avg `-0.0558` n `231`; crypto_major avg `-1.5724` n `8`; equity avg `-0.2124` n `128`; fx avg `-0.0964` n `6`; index avg `-0.0519` n `26`; metal avg `-0.2437` n `20`; unknown avg `-0.4782` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
