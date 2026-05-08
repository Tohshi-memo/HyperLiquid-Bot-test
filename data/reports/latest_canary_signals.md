# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T15:37:12.685970+00:00`
- Correlation status: `ready`
- Asset price records: `658`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.179` n `12`; crypto_alt avg `0.0205` n `228`; crypto_major avg `0.0509` n `8`; equity avg `0.0793` n `65`; fx avg `-0.0152` n `5`; index avg `0.0976` n `23`; metal avg `0.0432` n `18`; unknown avg `0.017` n `375`
- 1h: commodity avg `0.0444` n `12`; crypto_alt avg `-0.0757` n `228`; crypto_major avg `-0.1514` n `8`; equity avg `0.4944` n `65`; fx avg `-0.032` n `5`; index avg `0.189` n `23`; metal avg `-0.2286` n `18`; unknown avg `0.011` n `375`
- 4h: commodity avg `0.4261` n `12`; crypto_alt avg `0.3717` n `228`; crypto_major avg `-0.0` n `8`; equity avg `1.1791` n `65`; fx avg `-0.0657` n `5`; index avg `0.544` n `23`; metal avg `-0.4067` n `18`; unknown avg `0.0763` n `375`
- 24h: commodity avg `1.657` n `12`; crypto_alt avg `2.1688` n `228`; crypto_major avg `-0.1676` n `8`; equity avg `1.112` n `65`; fx avg `0.154` n `5`; index avg `0.3507` n `23`; metal avg `-0.7755` n `18`; unknown avg `0.0648` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1214`, n `650`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1174`, n `650`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `654`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `650`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `654`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0968`, n `650`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `654`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `654`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `654`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `654`, weak_sample_signal
