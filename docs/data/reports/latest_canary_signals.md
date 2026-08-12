# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T20:52:27.160417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.0889` n `230`; crypto_major avg `-0.0254` n `8`; equity avg `0.0338` n `113`; fx avg `0.0032` n `6`; index avg `-0.0001` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.1315` n `786`
- 1h: commodity avg `-0.067` n `12`; crypto_alt avg `0.1941` n `230`; crypto_major avg `0.2558` n `8`; equity avg `-0.2316` n `113`; fx avg `0.002` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0186` n `20`; unknown avg `0.5464` n `786`
- 4h: commodity avg `-0.057` n `12`; crypto_alt avg `-0.11` n `230`; crypto_major avg `-0.0027` n `8`; equity avg `-0.0783` n `113`; fx avg `0.0078` n `6`; index avg `0.0089` n `25`; metal avg `-0.0109` n `20`; unknown avg `0.3316` n `786`
- 24h: commodity avg `0.0027` n `12`; crypto_alt avg `-0.7027` n `230`; crypto_major avg `0.1695` n `8`; equity avg `2.8681` n `113`; fx avg `0.0419` n `6`; index avg `0.3787` n `25`; metal avg `0.1687` n `20`; unknown avg `0.0375` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2011`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
