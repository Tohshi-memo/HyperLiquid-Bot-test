# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T16:52:30.048283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.1694` n `232`; crypto_major avg `-0.2298` n `8`; equity avg `-0.1578` n `133`; fx avg `0.0002` n `6`; index avg `-0.0113` n `26`; metal avg `-0.0234` n `20`; unknown avg `0.5478` n `792`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `0.159` n `232`; crypto_major avg `0.0394` n `8`; equity avg `0.0184` n `133`; fx avg `-0.0057` n `6`; index avg `-0.0014` n `26`; metal avg `-0.0373` n `20`; unknown avg `-0.1129` n `790`
- 4h: commodity avg `0.2882` n `12`; crypto_alt avg `0.5101` n `232`; crypto_major avg `0.6132` n `8`; equity avg `0.4482` n `133`; fx avg `-0.1108` n `6`; index avg `0.1454` n `26`; metal avg `0.2428` n `20`; unknown avg `0.3182` n `789`
- 24h: commodity avg `0.4712` n `12`; crypto_alt avg `-0.4236` n `232`; crypto_major avg `-1.0155` n `8`; equity avg `-0.2435` n `133`; fx avg `-0.3432` n `6`; index avg `0.0102` n `26`; metal avg `0.0629` n `20`; unknown avg `0.1173` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0437`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0415`, n `668`, weak_sample_signal
