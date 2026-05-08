# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T10:07:19.622317+00:00`
- Correlation status: `ready`
- Asset price records: `636`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0567` n `12`; crypto_alt avg `0.055` n `228`; crypto_major avg `0.0338` n `8`; equity avg `0.164` n `65`; fx avg `0.0016` n `5`; index avg `0.0346` n `23`; metal avg `0.0742` n `18`; unknown avg `0.0821` n `375`
- 1h: commodity avg `0.3019` n `12`; crypto_alt avg `0.15` n `228`; crypto_major avg `0.0441` n `8`; equity avg `-0.1203` n `65`; fx avg `0.024` n `5`; index avg `-0.017` n `23`; metal avg `-0.0938` n `18`; unknown avg `0.0539` n `375`
- 4h: commodity avg `0.2857` n `12`; crypto_alt avg `0.775` n `228`; crypto_major avg `0.5007` n `8`; equity avg `0.7833` n `65`; fx avg `0.0655` n `5`; index avg `0.2202` n `23`; metal avg `-0.3719` n `18`; unknown avg `0.4084` n `375`
- 24h: commodity avg `1.2181` n `12`; crypto_alt avg `1.0253` n `228`; crypto_major avg `-1.4944` n `8`; equity avg `-0.5976` n `65`; fx avg `0.2671` n `5`; index avg `-0.3405` n `23`; metal avg `-0.5432` n `18`; unknown avg `-0.2242` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1389`, n `628`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1377`, n `628`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `632`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `632`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `632`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `632`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `628`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `628`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `632`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `628`, weak_sample_signal
