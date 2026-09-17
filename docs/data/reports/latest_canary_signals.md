# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T13:22:27.019243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0282` n `12`; crypto_alt avg `0.1177` n `234`; crypto_major avg `0.1959` n `8`; equity avg `0.0123` n `137`; fx avg `-0.0025` n `6`; index avg `-0.0025` n `27`; metal avg `0.0639` n `20`; unknown avg `35.1925` n `921`
- 1h: commodity avg `0.077` n `12`; crypto_alt avg `-0.117` n `234`; crypto_major avg `0.115` n `8`; equity avg `0.2803` n `137`; fx avg `0.016` n `6`; index avg `0.0401` n `27`; metal avg `-0.0072` n `20`; unknown avg `301.6919` n `913`
- 4h: commodity avg `-0.2678` n `12`; crypto_alt avg `0.1062` n `234`; crypto_major avg `0.2618` n `8`; equity avg `0.6323` n `137`; fx avg `-0.0655` n `6`; index avg `0.195` n `27`; metal avg `0.391` n `20`; unknown avg `0.0333` n `913`
- 24h: commodity avg `-0.8172` n `12`; crypto_alt avg `3.6196` n `234`; crypto_major avg `2.5149` n `8`; equity avg `1.9588` n `137`; fx avg `0.0125` n `6`; index avg `0.2676` n `27`; metal avg `0.2263` n `20`; unknown avg `0.4684` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
