# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T08:52:30.483080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0715` n `12`; crypto_alt avg `-0.1166` n `232`; crypto_major avg `-0.1945` n `8`; equity avg `-0.1015` n `133`; fx avg `-0.0231` n `6`; index avg `-0.0239` n `26`; metal avg `-0.0105` n `20`; unknown avg `0.2245` n `792`
- 1h: commodity avg `0.1293` n `12`; crypto_alt avg `0.2177` n `232`; crypto_major avg `0.2164` n `8`; equity avg `0.0168` n `133`; fx avg `-0.0708` n `6`; index avg `0.0186` n `26`; metal avg `0.0564` n `20`; unknown avg `-0.1652` n `790`
- 4h: commodity avg `0.0343` n `12`; crypto_alt avg `0.2191` n `232`; crypto_major avg `0.0928` n `8`; equity avg `-0.2835` n `133`; fx avg `-0.1141` n `6`; index avg `-0.0888` n `26`; metal avg `0.02` n `20`; unknown avg `-0.0547` n `754`
- 24h: commodity avg `0.2615` n `12`; crypto_alt avg `1.3984` n `232`; crypto_major avg `1.5928` n `8`; equity avg `1.6296` n `133`; fx avg `-0.3966` n `6`; index avg `0.1589` n `26`; metal avg `0.8765` n `20`; unknown avg `-0.1681` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0385`, n `668`, weak_sample_signal
